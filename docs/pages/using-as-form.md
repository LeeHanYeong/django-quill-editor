# Using as Form

Add the CSS and JS to the `<head>` of the template or base template. 

There are two ways to add CSS and JS files to a template.

  - If there is a **Form** with QuillField added, add `{{ form.media }}` to the `<head>` tag.  

    ```django
    <head>
        {{ form.media }}
    </head>
    ```

  - Or, import CSS and JS files directly using `{% include %}` template tags.

    ```django
    <head>
        <!-- django-quill-editor Media -->
        {% include 'django_quill/media.html' %}
    </head>
    ```

    

Add `QuillFormJSONField` to the **Form class** you want to use.

```python
# forms.py
from django import forms
from django_quill.forms import QuillFormJSONField

class QuillFieldForm(forms.Form):
    content = QuillFormJSONField()
```



Add a **Form instance** containing **QuillFormJSONField** to the template context in the view.

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

