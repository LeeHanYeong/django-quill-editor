from django import forms

from django_quill.forms import QuillFormField
from .models import QuillPost

__all__ = (
    "QuillFieldForm",
    "QuillPostForm",
)


class QuillFieldForm(forms.Form):
    content = QuillFormField()

    def save(self):
        return QuillPost.objects.create(content=self.cleaned_data["content"])


class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = ("content",)
