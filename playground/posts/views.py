from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView, FormView, CreateView

from .forms import QuillFieldForm, QuillPostForm
from .models import QuillPost

__all__ = (
    "QuillPostListView",
    "QuillPostCreateView",
    "QuillPostDetailView",
    "QuillPostUpdateView",
    "QuillFieldFormView",
    "QuillFieldFormHtmlInitialView",
    "QuillFieldFormTextInitialView",
)


class QuillPostListView(ListView):
    model = QuillPost


class QuillPostCreateView(CreateView):
    form_class = QuillPostForm
    template_name = "posts/quillpost_create.html"


class QuillPostDetailView(DetailView):
    model = QuillPost


class QuillPostUpdateView(UpdateView):
    model = QuillPost
    fields = ["content"]


# NormalForm
class QuillFieldFormView(FormView):
    form_class = QuillFieldForm
    template_name = "posts/quillpost_normal_form.html"

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("posts:quill-post-detail", args=(self.object.pk,))


class QuillFieldFormHtmlInitialView(QuillFieldFormView):
    initial = {
        "content": f"<h1>django-quill-editor</h1><br>"
        f'<img src="{settings.TITLE_IMG}">',
    }


class QuillFieldFormTextInitialView(QuillFieldFormView):
    initial = {
        "content": "django-quill-editor makes Quill.js easy to use on Django Forms and admin sites",
    }
