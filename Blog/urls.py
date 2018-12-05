from django.urls import path
import Blog.views


urlpatterns = [

    path("",Blog.views.Home, name="BlogsHome"),
    path("<int:blog_ID>/", Blog.views.blogNo, name='blogNo')]