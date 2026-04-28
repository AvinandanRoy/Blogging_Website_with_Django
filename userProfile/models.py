from django.db import models
from django.contrib.auth.models import User


# --- New Profile Model for the UI in image ---

class UserProfile(models.Model):
    # Links to the User who writes the Blogs
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Matching the UI Fields
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.png')
    job_title = models.CharField(max_length=100, blank=True, help_text="e.g. Full Stack Developer")
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    
    # Social Links
    website_url = models.URLField(max_length=255, blank=True)
    github_username = models.CharField(max_length=100, blank=True)
    twitter_username = models.CharField(max_length=100, blank=True)
    instagram_username = models.CharField(max_length=100, blank=True)
    facebook_username = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"