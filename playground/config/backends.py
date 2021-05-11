from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = ("StaticBackend",)


class StaticBackend:
    def authenticate(self, request):
        user = User.objects.get_or_create(
            username="django-quill-editor",
            is_staff=True,
            is_superuser=True,
        )[0]
        return user

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None
