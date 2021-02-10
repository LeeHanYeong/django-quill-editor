## Image uploads

If you want to upload images instead of storing encoded images in your database. You need to add `imageUploader` module
to your configuration. If you set a `uploadURL` for this modules, it registers
[quill-image-uploader](https://www.npmjs.com/package/quill-image-uploader) to Quill.
You can add a view to upload images to your storage service. Response of the view must contain `image_url` field.

```python
# urls.py
from django.urls import path
from .views import EditorImageUploadAPIView

urlpatterns = [
   ...
   path('admin/quill/upload/', EditorImageUploadAPIView.as_view(), name='quill-editor-upload'),
   ...
]
```

```python
# You don't have to use Django Rest Framework. This is just an example.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import EditorImageSerializer


class EditorImageUploadAPIView(CreateAPIView):
    serializer_class = EditorImageSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        # image_url = handle image upload
        return Response({'image_url': "https://xxx.s3.amazonaws.com/xxx/x.png"}, status=status.HTTP_200_OK)
```

```json
{
  ...
  "image_url": "https://xxx.s3.amazonaws.com/xxx/x.png"
  ...
}
```