from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    """
    Handles both creation and saving of the UserProfile.
    Using get_or_create prevents IntegrityErrors during login or manual saves.
    """
    if created:
        # For a brand new user
        UserProfile.objects.get_or_create(user=instance)
    else:
        # For an existing user (like during Admin login)
        # We use filter().first() to check existence without crashing
        profile = UserProfile.objects.filter(user=instance).first()
        if profile:
            profile.save()
        else:
            # Fallback if an old user exists but has no profile
            UserProfile.objects.create(user=instance)