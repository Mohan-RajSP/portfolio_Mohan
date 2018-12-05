from django.shortcuts import render, get_object_or_404
from .models import BlogModel

def Home(request):
    Blog_Model = BlogModel.objects
    return render(request, "blog/home.html", {'BlogMod': Blog_Model})

def blogNo(request,blog_ID):
    blogNo = get_object_or_404(BlogModel, pk=blog_ID)
    return render(request,"blog/blog_ID.html",{'blogNo':blogNo})

# Create your views here.
