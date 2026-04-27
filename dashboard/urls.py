from django.urls import  path

from dashboard import views

urlpatterns= [
    path('',views.dashboard ,name='dashboard'),
    
    # category CRUD
    path('view_category/',views.view_category ,name='view_category'),
    path('add_category/',views.add_category ,name='add_category'),
    path('edit_category/<str:category_name>/',views.edit_category ,name='edit_category'),
    path('delete_category/<str:category_name>/',views.delete_category ,name='delete_category'),
    
    # Blog CRUD
    path('add_blog/',views.add_blog ,name='add_blog'),
    path('view_blog_list/',views.view_blog_list ,name='view_blog_list'),
    path('edit_blog/<slug:slug>/',views.edit_blog ,name='edit_blog'),
    path('delete_blog/<slug:slug>/',views.delete_blog ,name='delete_blog'),
    
    # User CRUD
    path('view_users_list/',views.view_users_list ,name='view_users_list'),
    path('add_user/',views.add_user ,name='add_user'),
    
]