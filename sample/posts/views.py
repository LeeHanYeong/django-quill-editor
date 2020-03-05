from django.views.generic import ListView

from .models import QuillPost


class QuillPostListView(ListView):
    model = QuillPost
