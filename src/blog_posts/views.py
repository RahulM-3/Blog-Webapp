from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def home_page(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def blog_details(request, post_id=-1):
    if(post_id == -1):
        details = "no data available"
    else:
        obj = BlogPost.objects.get(post_id=post_id)
        details = obj.title+obj.content
    return render(request, "blogs.html", {"details":details})