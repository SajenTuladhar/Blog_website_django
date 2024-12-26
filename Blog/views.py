from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def mainpage(request):
    return render(request,"blog/mainPage.html")

def posts(request):
    return render(request,"blog/postsPage.html")
 
def post_details(request):
    return HttpResponse("the detail of this post is here")