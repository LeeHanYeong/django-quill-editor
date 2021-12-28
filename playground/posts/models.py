from django.db import models
from django.urls import reverse

from django_ueditor.fields import UEField

__all__ = ("UEPost",)


class UEPost(models.Model):
    content = UEField()

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return reverse("posts:ueditor-post-detail", args=[self.pk])
