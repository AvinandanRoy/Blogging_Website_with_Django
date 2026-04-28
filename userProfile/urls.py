from django.urls import include, path

from userProfile import views

urlpatterns = [
    path('user/', views.profile, name='profile'),
    path('user/editUserProfile/', views.editUserProfile, name='editUserProfile'),
    
    
    path('user/view_user_profile/<str:username>/', views.view_user_profile, name='view_user_profile'),
    
] 