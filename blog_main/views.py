

from django.shortcuts import render
from aboutSocialLink.models import About
from blogs.models import Blog,Category
from .forms import RegistrationForms

def home(req):
    featured_posts = Blog.objects.filter(is_featured = True , status='Published').order_by('-created_at')
    
    recent_posts = Blog.objects.filter(is_featured = False , status= 'Published').order_by('-created_at')
    
    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None 
    
    context={
        'featured_posts' : featured_posts ,
        'recent_posts': recent_posts,
        'about': about,
    }
    
    return render(req, 'home.html' , context)

def register(req):
    form = RegistrationForms
    context = {
        'form' : form,
    }
    return render(req , 'register.html', context)