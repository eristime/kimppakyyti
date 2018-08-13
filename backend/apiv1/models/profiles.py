from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=1000, blank=True) 
    photo = models.CharField(max_length=50, blank=True) # URL for picture

    
    def __str__(self):
        return self.first_name + " - " + self.last_name + "public profile"


class PrivateProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='private_profile',)
    reported = models.PositiveIntegerField(default=0)  # not in use
    deleted = models.BooleanField(default=False) # not in use
    is_active = models.BooleanField(default=True) # not in use
    token = models.CharField(max_length=100, unique=True)  # TODO: find a better place, probably not needed

    phone_number = models.CharField(max_length=1000, default=None) # for account management purposes?


    def __str__(self):
        return self.user.username + " private profile"


#TODO add first and last_name automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)