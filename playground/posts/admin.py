from django.contrib import admin

from .models import UEPost

__all__ = ("UEPostAdmin",)


@admin.register(UEPost)
class UEPostAdmin(admin.ModelAdmin):
    pass
