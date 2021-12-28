from django.db import models

from .forms import UEFormField
from .ueditor import UE

__all__ = (
    "FieldUE",
    "UEDescriptor",
    "UEField",
)


class FieldUE:
    def __init__(self, instance, field, json_string):
        self.instance = instance
        self.field = field
        self.json_string = json_string or '{"delta":"","html":""}'
        self._committed = True

    def __eq__(self, other):
        if hasattr(other, "json_string"):
            return self.json_string == other.json_string
        return self.json_string == other

    def __hash__(self):
        return hash(self.json_string)

    def _require_ueditor(self):
        if not self:
            raise ValueError(
                "The '%s' attribute has no UE JSON String associated with it."
                % self.field.name
            )

    def _get_ueditor(self):
        self._require_ueditor()
        self._ueditor = UE(self.json_string)
        return self._ueditor

    def _set_ueditor(self, ueditor):
        self._ueditor = ueditor

    def _del_ueditor(self):
        del self._ueditor

    ueditor = property(_get_ueditor, _set_ueditor, _del_ueditor)

    @property
    def html(self):
        self._require_ueditor()
        return self.ueditor.html

    @property
    def delta(self):
        self._require_ueditor()
        return self.ueditor.delta

    def save(self, json_string, save=True):
        setattr(self.instance, self.field.name, json_string)
        self._committed = True
        if save:
            self.instance.save()


class UEDescriptor:
    def __init__(self, field):
        self.field = field

    def __get__(self, instance, cls=None):
        if instance is None:
            return self

        if self.field.name in instance.__dict__:
            ueditor = instance.__dict__[self.field.name]
        else:
            instance.refresh_from_db(fields=[self.field.name])
            ueditor = getattr(instance, self.field.name)

        if isinstance(ueditor, str) or ueditor is None:
            attr = self.field.attr_class(instance, self.field, ueditor)
            instance.__dict__[self.field.name] = attr

        elif isinstance(ueditor, UE) and not isinstance(ueditor, FieldUE):
            ueditor_copy = self.field.attr_class(instance, self.field, ueditor.json_string)
            ueditor_copy.ueditor = ueditor
            ueditor_copy._committed = False
            instance.__dict__[self.field.name] = ueditor_copy

        elif isinstance(ueditor, FieldUE) and not hasattr(ueditor, "field"):
            ueditor.instance = instance
            ueditor.field = self.field

        elif isinstance(ueditor, FieldUE) and instance is not ueditor.instance:
            ueditor.instance = instance

        return instance.__dict__[self.field.name]

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = value


class UEField(models.TextField):
    attr_class = FieldUE
    descriptor_class = UEDescriptor

    def formfield(self, **kwargs):
        kwargs.update({"form_class": UEFormField})
        return super().formfield(**kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _get_form_class():
        return UEFormField

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        """
        Expect a JSON string with 'delta' and 'html' keys
        ex) b'{"delta": "...", "html": "..."}'
        :param value: JSON string with 'delta' and 'html' keys
        :return: UE's 'Delta' JSON String
        """
        if isinstance(value, UE):
            return value
        if isinstance(value, FieldUE):
            return value.ueditor
        if value is None or isinstance(value, str):
            return value
        return UE(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None:
            return value
        if isinstance(value, UE):
            return value.json_string
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
