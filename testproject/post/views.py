from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, FormView, CreateView, View

from .forms import QuillFieldForm, QuillPostForm
from .models import QuillPost

__all__ = (
    'QuillPostListView',
    'QuillPostCreateView',
    'QuillPostDetailView',
    'QuillPostUpdateView',
    'QuillFieldFormView',
    'QuillFieldFormHtmlInitialView',
    'QuillFieldFormTextInitialView',
)


class QuillPostListView(ListView):
    model = QuillPost


class QuillPostCreateView(CreateView):
    form_class = QuillPostForm
    template_name = 'post/quillpost_create.html'


class QuillPostDetailView(DetailView):
    model = QuillPost


class QuillPostUpdateView(UpdateView):
    model = QuillPost
    fields = ['content']


# NormalForm
class QuillFieldFormView(FormView):
    form_class = QuillFieldForm
    template_name = 'post/quillpost_normal_form.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:quill-post-detail', args=(self.object.pk,))


class QuillFieldFormHtmlInitialView(QuillFieldFormView):
    initial = {
        'content': f'<h1>django-quill-editor</h1><br>'
                   f'<img src="{settings.TITLE_IMG}">',
    }


class QuillFieldFormTextInitialView(QuillFieldFormView):
    initial = {
        'content': 'django-quill-editor makes Quill.js easy to use on Django Forms and admin sites',
    }


'''
Django Index views
'''
class IndexView(CreateView):
    template_name = 'index.html'
    form_class = QuillPostForm
    success_url = reverse_lazy('post:quill-post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['normal_form'] = QuillFieldForm()
        context['title_img'] = settings.TITLE_IMG
        return context


class ResetView(View):
    def post(self, request):
        QuillPost.objects.all().delete()
        return redirect(reverse('post:quill-post-list'))