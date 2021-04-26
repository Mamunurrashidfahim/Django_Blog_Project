from django.urls import path

from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>', views.blog_details, name='blog_details'),
    path('my-blogs/', views.MyBLogs.as_view(), name='my_blogs'),
    path('edit-blogs/<pk>', views.UpdateBlog.as_view(), name='edit_blogs'),
    path('delete-blogs/<pk>', views.DeleteBlogs.as_view(), name='delete_blogs'),
    path('liked/<pk>', views.liked, name='liked_post'),
    path('unliked/<pk>', views.unliked, name='unliked_post'),

]