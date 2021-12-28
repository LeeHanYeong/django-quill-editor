from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import UEPost


@receiver(post_save, sender=UEPost)
def posts_limit_10(sender, **kwargs):
    recent_posts = sender.objects.order_by("-id")[:10]
    sender.objects.exclude(id__in=recent_posts.values("id")).delete()
