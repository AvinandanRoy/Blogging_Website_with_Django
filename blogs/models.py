from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length= 100 , unique= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)     
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('Draft' , 'Draft'),
    ('Published' , 'Published'),
)
    
class Blog(models.Model):
    title = models.CharField(max_length= 200)
    slug = models.SlugField(max_length=300 , unique= True, blank= True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete= models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=10000)
    status = models.CharField(choices=STATUS_CHOICES, default='Draft' ,max_length=20)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title