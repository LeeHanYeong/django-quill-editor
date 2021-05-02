from django.db import models
from django.urls import reverse

from django_quill.fields import QuillField


class QuillPost(models.Model):
    content = QuillField()

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('posts:quill-post-detail', args=[self.pk])


class QuillMaster(models.Model):
    name = models.CharField(max_length=64)


class QuillDetail(models.Model):
    master = models.ForeignKey(QuillMaster, on_delete=models.CASCADE)
    content = QuillField()


class QuillDetail2(models.Model):
    master = models.ForeignKey(QuillMaster, on_delete=models.CASCADE)
    content = QuillField()