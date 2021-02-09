import json

from django.db import models

from .forms import QuillFormJSONField
from .quill import Quill, QuillParseError

__all__ = (
    'FieldQuill',
    'QuillDescriptor',
    'QuillField',
    'QuillTextField',
    'QuillJSONField'
)


class FieldQuill:
    def __init__(self, instance, field, data):
        self.instance = instance
        self.field = field
        self.data = data or dict(delta="", html="")

        assert isinstance(self.data, (str, dict)), (
                "FieldQuill expects dictionary or string as data but got %s(%s)." % (type(data), data)
        )
        if isinstance(self.data, str):
            try:
                self.data = json.loads(data)
            except json.JSONDecodeError:
                raise QuillParseError(data)

        self._committed = True

    def __eq__(self, other):
        if hasattr(other, 'data'):
            return self.data == other.data
        return self.data == other

    def __hash__(self):
        return hash(self.data)

    def _require_quill(self):
        if not self:
            raise ValueError("The '%s' attribute has no Quill JSON String associated with it." % self.field.name)

    def _get_quill(self):
        self._require_quill()
        self._quill = Quill(self.data)
        return self._quill

    def _set_quill(self, quill):
        self._quill = quill

    def _del_quill(self):
        del self._quill

    quill = property(_get_quill, _set_quill, _del_quill)

    @property
    def html(self):
        self._require_quill()
        return self.quill.html

    @property
    def delta(self):
        self._require_quill()
        return self.quill.delta

    def save(self, json_string, save=True):
        setattr(self.instance, self.field.name, json_string)
        self._committed = True
        if save:
            self.instance.save()


class QuillDescriptor:
    def __init__(self, field):
        self.field = field

    def __get__(self, instance, cls=None):
        if instance is None:
            return self

        if self.field.name in instance.__dict__:
            quill = instance.__dict__[self.field.name]
        else:
            instance.refresh_from_db(fields=[self.field.name])
            quill = getattr(instance, self.field.name)

        if isinstance(quill, str) or quill is None:
            attr = self.field.attr_class(instance, self.field, quill)
            instance.__dict__[self.field.name] = attr

        elif isinstance(quill, Quill) and not isinstance(quill, FieldQuill):
            quill_copy = self.field.attr_class(instance, self.field, quill.data)
            quill_copy.quill = quill
            quill_copy._committed = False
            instance.__dict__[self.field.name] = quill_copy

        elif isinstance(quill, FieldQuill) and not hasattr(quill, 'field'):
            quill.instance = instance
            quill.field = self.field

        elif isinstance(quill, FieldQuill) and instance is not quill.instance:
            quill.instance = instance

        return instance.__dict__[self.field.name]

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = value


class QuillFieldMixin:
    attr_class = FieldQuill
    descriptor_class = QuillDescriptor

    def formfield(self, **kwargs):
        kwargs.update({'form_class': self._get_form_class()})
        return super().formfield(**kwargs)

    @staticmethod
    def _get_form_class():
        return QuillFormJSONField

    def pre_save(self, model_instance, add):
        quill = super().pre_save(model_instance, add)
        if quill and not quill._committed:
            quill.save(quill.data, save=False)
        return quill

    def to_python(self, value):
        if isinstance(value, Quill):
            return value
        if isinstance(value, FieldQuill):
            return value.quill
        if value is None or isinstance(value, str):
            return value
        return Quill(value)

    def get_prep_value(self, value):
        if value is None or isinstance(value, str):
            return value
        if isinstance(value, (Quill, FieldQuill)):
            value = value.data

        return json.dumps(value, cls=getattr(self, 'encoder', None))

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class QuillTextField(QuillFieldMixin, models.TextField):
    pass


def QuillField(*args, **kwargs):
    return QuillTextField(*args, **kwargs)


class QuillJSONField(QuillFieldMixin, models.JSONField):

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def validate(self, value, model_instance):
        value = self.get_prep_value(value)
        super(QuillJSONField, self).validate(value, model_instance)
