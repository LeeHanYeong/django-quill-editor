# django-ueditor-editor

![PyPI](https://img.shields.io/pypi/v/django-ueditor-editor)

**django-ueditor-editor** makes [UE.js](https://ueditorjs.com/) easy to use on Django Forms and admin sites

- **No configuration required for static files!**
- The entire code for inserting WYSIWYG editor is less than 30 lines
- It can be used in both admin and Django views

![django-ueditor-editor](https://raw.githubusercontent.com/LeeHanYeong/django-ueditor-editor/master/_assets/django-ueditor-editor-sample.png)

## Live Demo

#### https://ueditor.lhy.kr/

- Form | https://ueditor.lhy.kr/posts/create/normal/
- ModelForm | https://ueditor.lhy.kr/posts/create/
- Form (Initial HTML) | https://ueditor.lhy.kr/posts/create/normal/html/
- Form (Initial Text) | https://ueditor.lhy.kr/posts/create/normal/text/
- Admin | https://ueditor.lhy.kr/admin/login/



## Documentation

The full document is in [https://django-ueditor-editor.readthedocs.io/](https://django-ueditor-editor.readthedocs.io/), including everything about how to use the Form or ModelForm, and where you can add custom settings.

Please refer to the **QuickStart** section below for simple usage.



## QuickStart

### Setup

- Install `django-ueditor-editor` to your Python environment

  > Requires Python 3.7 or higher and Django 3.1 or higher.

  ```shell
  pip install django-ueditor-editor
  ```

- Add `django_ueditor` to `INSTALLED_APPS` in `settings.py`

  ```python
  # settings.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      ...
      'django_ueditor',
  ]
  ```

### Making Model

Add `UEField` to the **Model class** you want to use.

> 1. App containing models.py must be added to INSTALLED_APPS
> 2. After adding the app, you need to run makemigrations and migrate to create the DB table.

```python
# models.py
from django.db import models
from django_ueditor.fields import UEField

class UEPost(models.Model):
    content = UEField()
```

### Using in admin

Just register the Model in **admin.py** of the app.

```python
from django.contrib import admin
from .models import UEPost

@admin.register(UEPost)
class UEPostAdmin(admin.ModelAdmin):
    pass
```

![admin-sample](https://raw.githubusercontent.com/LeeHanYeong/django-ueditor-editor/master/_assets/admin-sample.png)





## Running the Live Demo project in local

The live demo is a deployment of the **"playground"** package, which is a django application within this library.  
After cloning or downloading the repository, you can try running the live demo locally.

**A Python virtual environment is required to run the project.**

```shell
# [Optional] We recommend that you start after creating a folder for your project.
mkdir ~/projects
cd projects

# Clone repository
git clone git@github.com:LeeHanYeong/django-ueditor-editor.git

# Go to the project directory and apply the virtual environment
cd django-ueditor-editor
# [apply venv]

# Go to the playground package
cd playground

# Install requirements
pip install -r requirements.txt

# Run migrate and runserver
python manage.py migrate
python manage.py runserver
```

After the above operation, the live demo site works at localhost:8000.



## Contributing

As an open source project, we welcome contributions.
The code lives on [GitHub](https://github.com/LeeHanYeong/django-ueditor-editor)



## Distribution tips (for owners)

### Installation

```shell
# black
brew install black

# pre-commit
brew install pre-commit
pre-commit install
```

### PyPI Release

```shell
poetry install  # Install PyPI distribution packages
python deploy.py
```

### Sphinx docs

```shell
brew install sphinx-doc  # macOS
```

#### Local

```
cd docs
make html
# ...
# The HTML pages are in _build/html.

cd _build/html
python -m http.server 3001
```

 

### docker-compose up (in local)

```shell
docker-compose -f docker-compose-local.yml up --build --force-recreate --remove-orphans
```

