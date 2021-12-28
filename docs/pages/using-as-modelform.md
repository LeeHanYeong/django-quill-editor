# Using as ModelForm

Add `UEField` to the **Model class** you want to use

```python
# models.py
from django.db import models
from django_ueditor.fields import UEField

class UEPost(models.Model):
    content = UEField()
```



Just define and use **ModelForm** of Model class (with UEField)

```python
# forms.py
from django import forms
from .models import UEPost

class UEPostForm(forms.ModelForm):
    class Meta:
        model = UEPost
        fields = (
            'content',
        )
```



Set the **view** and **template** in the same way as when using a **normal Form**

```python
# views.py
from django.shortcuts import render
from .forms import UEPostForm

def model_form_view(request):
    return render(request, 'form_view.html', {'form': UEPostForm()})
```

```html
<!-- form_view.html -->
<form action="" method="POST">{% csrf_token %}
    {{ form.content }}
</form>
```

