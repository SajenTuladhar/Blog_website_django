from django.urls import path
from . import views

urlpatterns = [
    path("",views.mainpage, name="main-page"),
    path("posts/",views.posts, name="posts-page"),
    path("posts/<slug:slug>",views.post_details,name="post-detail-page") #takes dynamic value (my-first-post)
]
