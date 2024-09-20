"""
Django settings for django-quill-editor-playground project.
"""

import os
from pathlib import Path

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "er8-=^6ym+!t&r#4-=3cq3!25%3hw=9n+5bp1i2549ltqfg=xp"
DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "quill.localhost",
    "quill.lhy.kr",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://quill.localhost",
    "https://quill.lhy.kr",
]

# Static
STATIC_DIR = BASE_DIR / "static"
STATIC_ROOT = BASE_DIR / ".static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [STATIC_DIR]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ".media"

# Quill
QUILL_CONFIGS = {
    "default": {
        "theme": "snow",
        "modules": {
            "syntax": True,
            "toolbar": [
                [
                    {"font": []},
                    {"header": []},
                    {"align": []},
                    "bold",
                    "italic",
                    "underline",
                    "strike",
                    "blockquote",
                    {"color": []},
                    {"background": []},
                ],
                ["code-block", "link", "image"],
                ["clean"],
            ],
            # quill-image-compress
            "imageCompressor": {
                "quality": 0.8,
                "maxWidth": 2000,
                "maxHeight": 2000,
                "imageType": "image/jpeg",
                "keepImageTypes": [],
                "ignoreImageTypes": ["image/webp"],
                "debug": False,
                "suppressErrorLogging": True,
            },
            # quill-resize
            "resize": {
                "showSize": True,
                "locale": {},
            },
        },
    },
}

# Custom
LOGIN_URL = "admin:login"
LOGIN_REDIRECT_URL = "admin:index"
LOGOUT_REDIRECT_URL = "index"
DATA_UPLOAD_MAX_MEMORY_SIZE = 2 * 1024 * 1024  # 2MB
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
AUTHENTICATION_BACKENDS = [
    "config.backends.StaticBackend",
]
TITLE_IMG = (
    "https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/"
    "master/_assets/django-quill-editor-sample.png"
)

INSTALLED_APPS = [
    "posts",
    "config.apps.AdminConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django_quill",
    "rest_framework",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# django-extensions
SHELL_PLUS_IMPORTS = [
    "from posts.apis import *",
    "from posts.forms import *",
    "from posts.models import *",
    "from posts.serializers import *",
]
