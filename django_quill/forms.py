from django import forms
from .widgets import QuillWidget


class QuillFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'widget': QuillWidget(),
        })
        super().__init__(*args, **kwargs)
