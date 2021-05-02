from django.contrib import admin

from .models import QuillPost, \
    QuillMaster, QuillDetail, QuillDetail2  # In order to validate the Quill Support on Inlines


class QuillDetailInlines(admin.StackedInline):
    model = QuillDetail
    extra = 0


class QuillDetail2Inlines(admin.TabularInline):
    model = QuillDetail2
    extra = 1


@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass


@admin.register(QuillMaster)
class QuillMasterAdmin(admin.ModelAdmin):
    inlines = (QuillDetailInlines, QuillDetail2Inlines)

