from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.QuillPostListView.as_view(), name='quill-post-list'),
]
