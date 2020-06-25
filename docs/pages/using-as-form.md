# Using as Form

Add `QuillFormField` to the **Form class** you want to use.

```python
# forms.py
from django import forms
from django_quill.forms import QuillFormField

class QuillFieldForm(forms.Form):
    content = QuillFormField()
```



Add a **Form instance** containing **QuillFormField** to the template context in the view.

```python
# views.py
from django.shortcuts import render
from .forms import QuillFieldForm

def form_view(request):
    return render(request, 'form_view.html', {'form': QuillFieldForm()})
```



In the template, use the received **Form instance** variable. (in the above case, **'form'**) 

```html
<!-- form_view.html -->
<form action="" method="POST">{% csrf_token %}
    {{ form.content }}
</form>
```

