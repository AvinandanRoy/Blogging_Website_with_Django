

from aboutSocialLink.models import Social_Media_Link
from blogs.models import Category


def get_categories(request):
    
    categories = Category.objects.all()
    
    # always return dictionary, otherwise it will cause error
    return dict( categories = categories )

def get_social_Links(request):
    
    social_links = Social_Media_Link.objects.all()
    return dict(social_links = social_links)