from django.shortcuts import render
from apps.base.models import Settings
from .models import *

# Create your views here.
def blog(request):
    settings = Settings.objects.latest('id')
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', locals())

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    settings = Settings.objects.latest('id')
    return render(request, 'blog/blog-details.html', locals())