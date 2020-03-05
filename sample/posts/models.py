from django.db import models

from django_quill.fields import QuillField


class QuillPost(models.Model):
    content = QuillField()
