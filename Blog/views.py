from django.shortcuts import render,get_object_or_404
from .models import Posts

# Create your views here.

def mainpage(request):
    latest_post=Posts.objects.all().order_by("-date")[:3]
    return render(request,"blog/mainPage.html",{
        "posts":latest_post
    })

def posts(request):
    all_posts = Posts.objects.all().order_by("-date") 
    return render(request,"blog/postsPage.html",{
        "all_posts":all_posts
    })
 
def post_details(request,slug):
    identified_post= get_object_or_404(Posts,slug=slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    }) 