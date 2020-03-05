from django.urls import reverse_lazy
from django.views.generic import CreateView

from posts.forms import QuillPostForm


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = QuillPostForm
    success_url = reverse_lazy('posts:quill-post-list')
