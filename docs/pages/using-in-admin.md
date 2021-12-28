# Using in Django admin

Add `UEField` to the **Model class** you want to use

```python
# models.py
from django.db import models
from django_ueditor.fields import UEField

class UEPost(models.Model):
    content = UEField()
```



Just register the Model in **admin.py** of the app

```python
from django.contrib import admin
from .models import UEPost

@admin.register(UEPost)
class UEPostAdmin(admin.ModelAdmin):
    pass
```

![admin-sample](https://raw.githubusercontent.com/LeeHanYeong/django-ueditor-editor/master/_assets/admin-sample.png)

