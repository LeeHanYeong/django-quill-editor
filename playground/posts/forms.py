from django import forms

from django_ueditor.forms import UEFormField
from .models import UEPost

__all__ = (
    "UEFieldForm",
    "UEPostForm",
)


class UEFieldForm(forms.Form):
    content = UEFormField()

    def save(self):
        return UEPost.objects.create(content=self.cleaned_data["content"])


class UEPostForm(forms.ModelForm):
    class Meta:
        model = UEPost
        fields = ("content",)
