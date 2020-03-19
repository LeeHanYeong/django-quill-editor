from django.views.generic import ListView, UpdateView, DetailView

from .models import QuillPost


class QuillPostListView(ListView):
    model = QuillPost


class QuillPostDetailView(DetailView):
    model = QuillPost


class QuillPostUpdateView(UpdateView):
    model = QuillPost
    fields = ['content']
