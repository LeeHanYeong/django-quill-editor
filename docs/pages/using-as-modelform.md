# Using as ModelForm

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



Just define and use **ModelForm** of Model class (with QuillField)

```python
# forms.py
from django import forms
from .models import QuillPost

class QuillPostForm(forms.ModelForm):
    class Meta:
        model = QuillPost
        fields = (
            'content',
        )
```



Set the **view** and **template** in the same way as when using a **normal Form**

```python
# views.py
from django.shortcuts import render
from .forms import QuillPostForm

def model_form_view(request):
    return render(request, 'form_view.html', {'form': QuillPostForm()})
```

```html
<!-- form_view.html -->
<form action="" method="POST">{% csrf_token %}
    {{ form.content }}
</form>
```

