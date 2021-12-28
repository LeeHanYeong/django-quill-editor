from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.UEPostListView.as_view(), name="ueditor-post-list"),
    path("create/", views.UEPostCreateView.as_view(), name="ueditor-post-create"),
    path(
        "create/normal/",
        views.UEFieldFormView.as_view(),
        name="ueditor-post-create-normal",
    ),
    path(
        "create/normal/html/",
        views.UEFieldFormHtmlInitialView.as_view(),
        name="ueditor-post-create-normal-html",
    ),
    path(
        "create/normal/text/",
        views.UEFieldFormTextInitialView.as_view(),
        name="ueditor-post-create-normal-text",
    ),
    path("<int:pk>/", views.UEPostDetailView.as_view(), name="ueditor-post-detail"),
    path(
        "<int:pk>/update/",
        views.UEPostUpdateView.as_view(),
        name="ueditor-post-update",
    ),
]
