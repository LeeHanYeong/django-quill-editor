from rest_framework import serializers

from django_quill.drf.fields import QuillHtmlField, QuillPlainField
from posts.models import QuillPost

__all__ = ("QuillPostSerializer",)


class QuillPostSerializer(serializers.ModelSerializer):
    content = QuillHtmlField()
    content_plain = QuillPlainField(source="content")

    class Meta:
        model = QuillPost
        fields = "__all__"
