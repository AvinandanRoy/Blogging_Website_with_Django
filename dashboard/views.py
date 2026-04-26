from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from django.utils.text import slugify
from blogs.models import Blog, Category
from .forms import BlogForm, CategoryForm

# Create your views here.

@login_required(login_url="login")
def dashboard(req):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context ={
        "category_count": category_count,
        "blog_count": blog_count,
    }
    return render(req , "dashboard/dashboard.html", context)

@login_required(login_url="login")
def view_category(req):
    categories = Category.objects.annotate(blog_count=Count('blog')).all()
    
    context ={
        "categories": categories,
    }
    return render(req , "dashboard/view_category.html",context)

@login_required(login_url="login")
def add_category(req):
    if req.method == 'POST':
        form =CategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("view_category")
    form =CategoryForm()
    context ={
        "form": form ,
    }
    
    return render(req , "dashboard/add_category.html", context)

@login_required(login_url="login")
def edit_category(req, category_name):
    category = get_object_or_404(Category , category_name = category_name)
    if req.method == 'POST':
        form =CategoryForm(req.POST, instance= category)
        if form.is_valid():
            form.save()
            return redirect("view_category")
    form =CategoryForm(instance= category)
    
    context ={
        "form": form ,
        "category" : category ,
    }
    return render(req, "dashboard/edit_category.html" , context)

@login_required(login_url="login")
def delete_category(req, category_name):
    category = get_object_or_404(Category , category_name = category_name)
    
    if req.method == 'POST':
        category.delete()
        messages.success(req, "Category deleted successfully!")
        return redirect("view_category")
        
    
    context ={"category":category,}
    return render(req ,"dashboard/delete_category.html" , context)

@login_required(login_url="login")
def view_blog_list(req):
    blogs = Blog.objects.all()
    context ={
       'blogs': blogs, 
    }
    return render(req , "dashboard/view_blog_list.html", context)

@login_required(login_url="login")
def edit_blog(req, slug):
    blog = get_object_or_404(Blog, slug = slug)
    if req.method == 'POST':
        form =BlogForm(req.POST,req.FILES, instance= blog)
        if form.is_valid():
            form.save()
            return redirect("single_post_view" ,blog.category , blog.slug)
    form =BlogForm(instance= blog)
    context ={
        "form": form,
        "blog": blog,
    }
    return render(req, "dashboard/edit_blog.html" ,context)

def delete_blog(req , slug):
    blog = get_object_or_404(Blog , slug = slug)
    
    if req.method == 'POST':
        blog.delete()
        messages.success(req, "Category deleted successfully!")
        return redirect('view_blog_list')
    
    context ={
        "blog": blog ,
    }
    return render(req , "dashboard/delete_blog.html", context)

def add_blog(req):
    if req.method == 'POST':
        form = BlogForm(req.POST, req.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = req.user

            # ✅ generate slug
            base_slug = slugify(blog.title)
            slug = base_slug
            counter = 1

            # ✅ ensure unique slug
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            blog.slug = slug
            blog.save()
            return redirect("view_blog_list")
    else:
        form = BlogForm()
    context ={"form": form,}
    return render(req, "dashboard/add_blog.html", context)