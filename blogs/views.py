from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category

# Create your views here.


def post_by_category(request, category_id):
    
    posts = Blog.objects.filter(status= 'Published' , category__id= category_id)
    category = get_object_or_404(Category ,id = category_id)
    # try:
    #     category = Category.objects.get(id = category_id)
    # except Category.DoesNotExist:
    #     category = None 
    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'post_by_category.html' , context )

def single_post_view(request,category_name, slug ):
    
    try:
        post = Blog.objects.get( status = 'Published' ,slug = slug , category__category_name = category_name)
    except Blog.DoesNotExist:
        post = None
        
    
    context ={
        'post': post,
    }
    
    return render(request , 'single_post_view.html' , context,)