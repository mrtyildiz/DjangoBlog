from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from app.models import Socials
from app.models import About
from app.models import Topics
from app.models import Blog
def index(request):
    Social = Socials.objects.all()
    Abouts = About.objects.all()
    Topic = Topics.objects.all()
    Blogs = Blog.objects.all()
    context = {
        'Social': Social,'Abouts': Abouts, 'Topic':Topic, 'Blogs':Blogs
    }
    return render(request, 'index.html', context)

def BlogDetails(request, pk):
    BlogID = Blog.objects.get(id=pk)
    context = {
        'BlogID': BlogID
    }
    return render(request, 'Blog-details.html', context)
