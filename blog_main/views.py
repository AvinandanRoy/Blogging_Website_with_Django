

from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import redirect, render
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
    if req.method == 'POST':
        form = RegistrationForms(req.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}!')
            return redirect("home")
    else:
        form = RegistrationForms()
    context = {
        'form' : form,
    }
    return render(req , 'register.html', context,)

def login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req , data=req.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = auth.authenticate(username = username , password = password)
            
            if user is not None:
                auth.login(req, user )
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    
    
    context ={
        "form": form,
    }
    return render(req , "login.html", context)

def logout(req):
    auth.logout(req)
    return redirect('home')