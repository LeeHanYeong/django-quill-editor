from django import forms
from .widgets import QuillWidget

__all__ = (
    'QuillFormField',
)


class QuillFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': QuillWidget(),
        })
        super().__init__(*args, **kwargs)
