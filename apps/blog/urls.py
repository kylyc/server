from django.urls import path
from .views import *

urlpatterns = [
    path('blog', blog, name="blog"),
    path('blog_details/<int:id>/', blog_details, name="blog_details")
]