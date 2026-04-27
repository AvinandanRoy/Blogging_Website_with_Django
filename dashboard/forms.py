

from django import forms

from blogs.models import Blog, Category 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title','category', 'featured_image', 'short_description', 'blog_body', 'status','is_featured', ]  
        exclude = ['author', 'slug', 'created_at', 'updated_at']

class UserForm(UserCreationForm): 
    class Meta:
        model = User 
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )