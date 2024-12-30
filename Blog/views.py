from django.shortcuts import render,get_object_or_404,redirect
from .models import Posts
from .models import Posts, Comment
from .forms import CommentForm


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
 
def post_details(request, slug):
    # Fetch the specific post
    identified_post = get_object_or_404(Posts, slug=slug)

    # Handle POST request to save a new comment
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create a comment object but don't save it yet
            new_comment = comment_form.save(commit=False)
            new_comment.post = identified_post  # Link the comment to the current post
            new_comment.save()  # Save the comment
            return redirect("post-detail-page", slug=slug)  # Redirect to the same page to avoid duplicate submissions

    # If GET request, just display the post and an empty form
    else:
        comment_form = CommentForm()

    # Fetch all comments for the current post
    comments = identified_post.comment.all()

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
        "form": comment_form,
        "comments": comments,
    })