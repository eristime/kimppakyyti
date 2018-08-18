from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    '''Model for user public information.'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=100, blank=True) 
    photo = models.CharField(max_length=1000, blank=True) # URL for picture

    def __str__(self):
        return self.owner.username + "public profile"


class PrivateProfile(models.Model):
    '''Model for user private information.'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='private_profile',)
    phone_number = models.CharField(max_length=100, blank=True) # for account management purposes?
    #email = models.EmailField(blank=True)

    def __str__(self):
        return self.owner.username + " private profile"


class StaffProfile(models.Model):
    '''Model for user information which only staff can see.'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile',)
    reported_count = models.PositiveIntegerField(default=0)  # not in use
    deleted = models.BooleanField(default=False) # not in use
    is_active = models.BooleanField(default=True) # not in use
    #token = models.CharField(max_length=100, unique=True)  # TODO: is this needed somewhere?

    def __str__(self):
        return self.owner.username + " staff profile"


#TODO add first and last_name automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
        PrivateProfile.objects.create(owner=instance)
        StaffProfile.objects.create(owner=instance)