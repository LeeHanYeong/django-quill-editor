from rest_framework import serializers

from django_quill.fields import FieldQuill

__all__ = (
    "QuillFieldMixin",
    "QuillHtmlField",
    "QuillPlainField",
)


class QuillFieldMixin:
    pass


class QuillHtmlField(QuillFieldMixin, serializers.Field):
    def to_representation(self, value: FieldQuill):
        return value.quill.html


class QuillPlainField(QuillFieldMixin, serializers.Field):
    def to_representation(self, value: FieldQuill):
        return value.quill.plain
