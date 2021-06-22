from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from posts.forms import QuillPostForm, QuillFieldForm
from posts.models import QuillPost

__all__ = (
    "IndexView",
    "ResetView",
)


class IndexView(CreateView):
    template_name = "index.html"
    form_class = QuillPostForm
    success_url = reverse_lazy("posts:quill-post-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["normal_form"] = QuillFieldForm()
        context["title_img"] = settings.TITLE_IMG
        return context


class ResetView(View):
    def post(self, request):
        QuillPost.objects.all().delete()
        return redirect(reverse("posts:quill-post-list"))
