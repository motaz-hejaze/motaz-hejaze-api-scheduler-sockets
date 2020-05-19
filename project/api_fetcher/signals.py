from .models import Item
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers
from .views import background_thread

@receiver(post_save, sender=Item)
def print_item_saved(sender, instance, created, **kwargs):
    if created:
        background_thread(instance)
