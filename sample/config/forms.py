from django import forms

from django_quill.forms import QuillFormField


class QuillForm(forms.Form):
    quill = QuillFormField()
