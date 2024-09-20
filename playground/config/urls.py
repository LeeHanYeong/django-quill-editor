"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import importlib.util

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

__all__ = ("urlpatterns",)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("reset/", views.ResetView.as_view(), name="reset"),
    path("posts/", include("posts.urls")),
]
urlpatterns_apis = []

if (spec := importlib.util.find_spec("rest_framework")) is not None:
    from posts import apis

    router = SimpleRouter()
    router.register(r"", apis.QuillPostViewSet)
    urlpatterns_apis.append(path("posts/", include(router.urls)))

if urlpatterns_apis:
    urlpatterns.append(path("api/", include(urlpatterns_apis)))
