from django.db import models
from django.urls import reverse

from django_quill.fields import QuillField


class QuillPost(models.Model):
    content = QuillField()

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('posts:quill-post-detail', args=[self.pk])
