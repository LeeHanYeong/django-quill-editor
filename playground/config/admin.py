from django.contrib.admin import AdminSite as BaseAdminSite
from django.contrib.auth import authenticate
from django.forms import forms

__all__ = ("AdminSite",)


class LoginForm(forms.Form):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        self.user_cache = authenticate(self.request)
        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class AdminSite(BaseAdminSite):
    login_form = LoginForm
    login_template = "admin/login_without_credentials.html"
