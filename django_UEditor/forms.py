from django import forms
from .widgets import UEWidget

__all__ = ("UEFormField",)


class UEFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "widget": UEWidget(),
            }
        )
        super().__init__(*args, **kwargs)
