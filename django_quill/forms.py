from django import forms
from .widgets import QuillWidget

__all__ = (
    'QuillFormField',
)


class QuillFormField(forms.fields.JSONField):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': QuillWidget(),
        })
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        return value.json_string if value else None
