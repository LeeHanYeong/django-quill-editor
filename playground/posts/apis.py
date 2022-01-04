from rest_framework import viewsets

from posts.models import QuillPost
from posts.serializers import QuillPostSerializer

__all__ = ("QuillPostViewSet",)


class QuillPostViewSet(viewsets.ModelViewSet):
    queryset = QuillPost.objects.all()
    serializer_class = QuillPostSerializer
