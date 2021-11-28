# django-quill-editor-ng

![PyPI](https://img.shields.io/pypi/v/django-quill-editor)

**django-quill-editor** makes [Quill.js](https://quilljs.com/) easy to use on Django Forms and admin sites

- **No configuration required for static files!**
- The entire code for inserting WYSIWYG editor is less than 30 lines
- It can be used in both admin and Django views
- It is a Forked version of the original `django-quill-editor` with some improvements.
  - The main difference is that I performed some changes in order to get this supported inside django inlines;
  - Also, I added compatibility with `django-jazzmin`

Actually the following versions are supported

| Django | Quill | Python |
| ---    | ---   | ---    |
| 3.2+   | 1.3.7 | 3.6+   |


![django-quill-editor](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/django-quill-editor-sample.png)

## Documentation

The full document is in [https://django-quill-editor.readthedocs.io/](https://django-quill-editor.readthedocs.io/), including everything about how to use the Form or ModelForm, and where you can add custom settings.

Please refer to the **QuickStart** section below for simple usage.


## QuickStart

### Setup

- Install `django-quill-editor` to your Python environment

  > Requires Python 3.7 or higher and Django 3.1 or higher.

  ```shell
  pip install django-quill-editor
  ```

- Add `django_quill` to `INSTALLED_APPS` in `settings.py`

  ```python
  # settings.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      ...
      'django_quill',
  ]
  ```

### Making Model

Add `QuillField` to the **Model class** you want to use.

> 1. App containing models.py must be added to INSTALLED_APPS
> 2. After adding the app, you need to run makemigrations and migrate to create the DB table.

```python
# models.py
from django.db import models
from django_quill.fields import QuillField

class QuillPost(models.Model):
    content = QuillField()
```

### Using in admin

Just register the Model in **admin.py** of the app.

```python
from django.contrib import admin
from .models import QuillPost

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
```

![admin-sample](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/admin-sample.png)

## Contributing

As an open source project, we welcome contributions.
The code lives on [GitHub](https://github.com/joepreludian/django-quill-editor-ng)


## Developing the library locally

First of all, install all the dependencies used by this repo by using poetry. Make sure that `poetry` is installed accordingly.

```shell
$ cd testproject
$ ./start_development.sh  # it will do all the magic for you
```
