from django.db import models
from django.db.models import CharField, TextField
from django.urls import reverse

from django_quill.fields import QuillField

__all__ = (
    "QuillPost",
    "NonQuillPost",
)


class QuillPost(models.Model):
    content = QuillField()

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse("posts:quill-post-detail", args=[self.pk])


class NonQuillPost(models.Model):
    content_char = CharField(max_length=300, blank=True)
    content_text = QuillField()
