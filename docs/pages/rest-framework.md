# Integration with DRF

## Serializer Fields

- `django_quill.drf.fields.QuillHtmlField`  
  HTML content of QuillField
- `django_quill.drf.fields.QuillPlainField`  
  Plain text of QuillField

example:

**models.py**

```python
from django_quill.fields import QuillField

class QuillPost(models.Model):
    content = QuillField()
```

**serializers.py**

```python
from rest_framework import serializers
from django_quill.drf.fields import QuillHtmlField, QuillPlainField
from posts.models import QuillPost

class QuillPostSerializer(serializers.ModelSerializer):
    content = QuillHtmlField()
    content_plain = QuillPlainField(source='content')

    class Meta:
        model = QuillPost
        fields = "__all__"

```



