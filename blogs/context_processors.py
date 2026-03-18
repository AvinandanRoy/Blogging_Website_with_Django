

from blogs.models import Category


def get_categories(request):
    
    categories = Category.objects.all()
    
    # always return dictionary, otherwise it will cause error
    return dict( categories = categories )