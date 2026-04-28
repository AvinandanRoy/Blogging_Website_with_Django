from django.urls import include, path

from userProfile import views

urlpatterns = [
    path('', views.profile, name='profile'),
    
] 