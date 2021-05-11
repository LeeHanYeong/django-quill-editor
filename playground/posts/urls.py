from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.QuillPostListView.as_view(), name="quill-post-list"),
    path("create/", views.QuillPostCreateView.as_view(), name="quill-post-create"),
    path(
        "create/normal/",
        views.QuillFieldFormView.as_view(),
        name="quill-post-create-normal",
    ),
    path(
        "create/normal/html/",
        views.QuillFieldFormHtmlInitialView.as_view(),
        name="quill-post-create-normal-html",
    ),
    path(
        "create/normal/text/",
        views.QuillFieldFormTextInitialView.as_view(),
        name="quill-post-create-normal-text",
    ),
    path("<int:pk>/", views.QuillPostDetailView.as_view(), name="quill-post-detail"),
    path(
        "<int:pk>/update/",
        views.QuillPostUpdateView.as_view(),
        name="quill-post-update",
    ),
]
