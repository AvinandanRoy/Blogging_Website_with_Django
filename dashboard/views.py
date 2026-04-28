from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from django.utils.text import slugify
from blogs.models import Blog, Category
from .forms import BlogForm, CategoryForm, UserForm, EditUserForm


# Create your views here.

@login_required(login_url="login")
def dashboard(req):
    category_count = Category.objects.all().count()
    if req.user.is_superuser or req.user.groups.filter(name='Manager').exists():
        blog_count = Blog.objects.all().count()
    elif req.user.groups.filter(name='Editor').exists():
        blog_count = Blog.objects.filter(author=req.user).count()
    else:
        blog_count = Blog.objects.filter(author=req.user).count()
                
    context ={
        "category_count": category_count,
        "blog_count": blog_count,
    }
    return render(req , "dashboard/dashboard.html", context)

@login_required(login_url="login")
@permission_required('blogs.view_category', raise_exception=True)
def view_category(req):
    categories = Category.objects.annotate(blog_count=Count('blog')).all()
    
    context ={
        "categories": categories,
    }
    return render(req , "dashboard/view_category.html",context)

@login_required(login_url="login")
@permission_required('blogs.add_category', raise_exception=True)
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
@permission_required('blogs.change_category', raise_exception=True)
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
@permission_required('blogs.delete_category', raise_exception=True)
def delete_category(req, category_name):
    category = get_object_or_404(Category , category_name = category_name)
    
    if req.method == 'POST':
        category.delete()
        messages.success(req, "Category deleted successfully!")
        return redirect("view_category")
        
    
    context ={"category":category,}
    return render(req ,"dashboard/delete_category.html" , context)

@login_required(login_url="login")
@permission_required('blogs.view_blog', raise_exception=True)
def view_blog_list(req):
    # ১. ইউজার যদি সুপার ইউজার (Admin) হয় অথবা 'Manager' গ্রুপের সদস্য হয়
    if req.user.is_superuser or req.user.groups.filter(name='Manager').exists():
        blogs = Blog.objects.all().order_by('-id')
        
    # ২. ইউজার যদি 'Editor' গ্রুপের সদস্য হয় (সে শুধু নিজের পোস্ট দেখবে)
    elif req.user.groups.filter(name='Editor').exists():
        blogs = Blog.objects.filter(author=req.user).order_by('-id')
        
    # ৩. অন্য কোনো সাধারণ ইউজার হলে (Optional: আপনি চাইলে খালি রাখতে পারেন বা শুধু নিজেরটা দেখাতে পারেন)
    else:
        blogs = Blog.objects.filter(author=req.user).order_by('-id')
        
    context ={
       'blogs': blogs, 
    }
    return render(req , "dashboard/view_blog_list.html", context)

@login_required(login_url="login")
@permission_required('blogs.change_blog', raise_exception=True)
def edit_blog(req, slug):
    blog = get_object_or_404(Blog, slug = slug)
    if req.method == 'POST':
        form =BlogForm(req.POST,req.FILES, instance= blog)
        if form.is_valid():
            new_blog = form.save(commit=False)
            # টাইটেল পরিবর্তন হলে স্লাগও নতুন করে তৈরি হবে
            new_blog.slug = slugify(new_blog.title) 
            new_blog.save()
            return redirect("single_post_view", new_blog.category, new_blog.slug)
    form =BlogForm(instance= blog)
    context ={
        "form": form,
        "blog": blog,
    }
    return render(req, "dashboard/edit_blog.html" ,context)

@login_required(login_url="login")
@permission_required('blogs.delete_blog', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('blogs.add_blog', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('auth.view_user', raise_exception=True)
def view_users_list(req):
    users = User.objects.all().order_by('-id')

    context ={
        "users": users,
    }
    return render(req, "dashboard/view_users_list.html" , context )


@login_required(login_url="login")
@permission_required('auth.add_user', raise_exception=True)
def add_user(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("view_users_list")
    else:
        form = UserForm()
    context ={
      'form': form,  
    }
    return render(req, "dashboard/add_user.html" , context )

@login_required(login_url="login")
@permission_required('auth.change_user', raise_exception=True)
def edit_user(req, username):
    user = get_object_or_404(User , username = username)
    print(user)
    if req.method == "POST":
        form = EditUserForm(req.POST ,instance = user)
        if form.is_valid():
            form.save()
            return redirect("view_users_list")
    form = EditUserForm(instance = user)
    context ={
      'form': form,
      'user': user ,  
    }
    return render(req, "dashboard/edit_user.html" , context )

@login_required(login_url="login")
@permission_required('auth.delete_user', raise_exception=True)
def delete_user(req, username):
    user = get_object_or_404(User , username = username)
    
    if req.method == 'POST':
        user.delete()
        messages.success(req, "User deleted successfully!")
        return redirect('view_users_list')
    
    context ={
      'user': user ,  
    }
    return render(req , "dashboard/delete_user.html", context )

