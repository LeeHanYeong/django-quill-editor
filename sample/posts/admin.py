from django.contrib import admin

from .models import QuillPost


@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
