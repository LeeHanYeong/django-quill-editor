from django import forms
from .widgets import QuillWidget

__all__ = (
    'QuillFormField',
    'QuillFormJSONField'
)


class QuillFormJSONField(forms.JSONField):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': QuillWidget(),
        })
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        if hasattr(value, "data"):
            return value.data

    def has_changed(self, initial, data):
        if hasattr(initial, 'data'):
            initial = initial.data
        return super(QuillFormJSONField, self).has_changed(initial, data)


def QuillFormField(*args, **kwargs):
    return QuillFormJSONField(*args, **kwargs)
