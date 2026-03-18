

from django.shortcuts import render
from blogs.models import Blog,Category

def home(req):
    featured_posts = Blog.objects.filter(is_featured = True , status='Published').order_by('-created_at')
    
    recent_posts = Blog.objects.filter(is_featured = False , status= 'Published').order_by('-created_at')
    
    context={
        'featured_posts' : featured_posts ,
        'recent_posts': recent_posts,
    }
    
    return render(req, 'home.html' , context)