from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.QuillPostListView.as_view(), name='quill-post-list'),
    path('<int:pk>/', views.QuillPostDetailView.as_view(), name='quill-post-detail'),
    path('<int:pk>/update/', views.QuillPostUpdateView.as_view(), name='quill-post-update'),
]
