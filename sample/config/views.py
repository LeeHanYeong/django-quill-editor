from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from posts.forms import QuillPostForm, QuillFieldForm


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = QuillPostForm
    success_url = reverse_lazy('posts:quill-post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['normal_form'] = QuillFieldForm()
        return context
