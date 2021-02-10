# Using in Django admin

Add `QuillTextField` or `QuillJSONField` to the **Model class** you want to use. 

```python
# models.py
from django.db import models
from django_quill.fields import QuillField, QuillTextField, QuillJSONField

class QuillPost(models.Model):
    content = QuillField()              # Deprecated. It is same with QuillTextField.
    content = QuillTextField()
    content = QuillJSONField()
```



Just register the Model in **admin.py** of the app

```python
from django.contrib import admin
from .models import QuillPost

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
```

![admin-sample](https://raw.githubusercontent.com/LeeHanYeong/django-quill-editor/master/_assets/admin-sample.png)

