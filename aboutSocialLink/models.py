from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True) 
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'About' 
        verbose_name_plural = 'About'

class Social_Media_Link(models.Model):
    platform_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name
    
    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = 'Social Media Links'