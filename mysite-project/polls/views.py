
from django.shortcuts import render
from .models import Posts
def index(request):
    posts = Posts.objects.all()
    context = {
        'title':'Latest Posts',
        'posts':posts
    }
    return render(request,'polls/index.html',context)