from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView

from .forms import QuillFieldForm
from .models import QuillPost


class QuillPostListView(ListView):
    model = QuillPost


class QuillPostDetailView(DetailView):
    model = QuillPost


class QuillPostUpdateView(UpdateView):
    model = QuillPost
    fields = ['content']


def quill_post_normal_form_initial_view(request):
    url_img = 'https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/' \
              'master/_assets/django-quill-editor-sample.png'
    initial = {
        'normal_content': f'<h1>django-quill-editor</h1><br>'
                          f'<img src="{url_img}">',
        'normal_content2': 'django-quill-editor makes Quill.js easy to use on Django Forms and admin sites',
    }
    form = QuillFieldForm(initial=initial)
    context = {'form': form}
    return render(request, 'posts/quillpost_normal_form.html', context)
