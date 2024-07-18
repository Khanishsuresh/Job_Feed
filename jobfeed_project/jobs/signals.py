from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Job

@receiver(post_save, sender=Job)
def update_feed(sender, instance, **kwargs):
    # Logic to regenerate the feed if needed
    pass