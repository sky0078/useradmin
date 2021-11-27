from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msgs = models.TextField(blank=True)
    

@receiver(post_save, sender=User)
def create_user_Messages(sender, instance, created, **kwargs):
    if created:
        Messages.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_Messages(sender, instance, **kwargs):
    instance.messages.save()

    
    