# django-quill-editor

![PyPI](https://img.shields.io/pypi/v/django-quill-editor)

**django-quill-editor** makes [Quill.js](https://quilljs.com/) easy to use on Django Forms and admin sites

- **No configuration required for static files!**
- The entire code for inserting WYSIWYG editor is less than 30 lines
- It can be used in both admin and Django views

![django-quill-editor](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/django-quill-editor-sample.png)

## Live Demo

#### https://quill.lhy.kr/

- Form | https://quill.lhy.kr/posts/create/normal/
- ModelForm | https://quill.lhy.kr/posts/create/
- Form (Initial HTML) | https://quill.lhy.kr/posts/create/normal/html/
- Form (Initial Text) | https://quill.lhy.kr/posts/create/normal/text/
- Admin | https://quill.lhy.kr/admin/login/



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





## Running the Live Demo project in local

The live demo is a deployment of the **"playground"** package, which is a django application within this library.  
After cloning or downloading the repository, you can try running the live demo locally.

**A Python virtual environment is required to run the project.**

```shell
# [Optional] We recommend that you start after creating a folder for your project.
mkdir ~/projects
cd projects

# Clone repository
git clone git@github.com:LeeHanYeong/django-quill-editor.git

# Go to the project directory and apply the virtual environment
cd django-quill-editor
# [apply venv]

# Install requirements
pip install -r requirements.txt

# Go to the playground package
cd playground

# Run migrate and runserver
python manage.py migrate
python manage.py runserver
```

After the above operation, the live demo site works at localhost:8000.



## Contributing

As an open source project, we welcome contributions.
The code lives on [GitHub](https://github.com/LeeHanYeong/django-quill-editor)



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

 

### docker-compose up

1. Create network

```shell
docker network create proxy \
  --subnet=172.20.0.0/16 \
  --gateway=172.20.0.1
```

2. run docker

```shell
# local
docker compose --env-file .deploy/.env.local up --build --force-recreate --remove-orphans
# production
docker compose --env-file .deploy/.env.production up --build --force-recreate --remove-orphans
```

