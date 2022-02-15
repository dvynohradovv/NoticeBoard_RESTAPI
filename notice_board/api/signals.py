from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from .models import UserDetail


@receiver(post_save, sender=User)
def userdetails_create(sender, instance=None, created=False, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
