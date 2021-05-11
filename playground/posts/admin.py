from django.contrib import admin

from .models import QuillPost

__all__ = ("QuillPostAdmin",)


@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
