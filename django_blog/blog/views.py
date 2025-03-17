from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post

dummy_posts = [
    
]




def starting_page(request):
    # sorted_posts = sorted(dummy_posts,key=(lambda x: x['date']))
    # latest_posts = sorted_posts[-3:]
    # return render(request,'blog/index.html', {
    #     "posts":latest_posts
    # }) 
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,'blog/index.html', {
        "posts":latest_posts
    })



def posts(request):
    posts = Post.objects.all()
    return render(request,'blog/all-posts.html',{
        "all_posts": posts
    }) 


def post_detail(request, slug):
    # slug_post = next(post for post in dummy_posts if post['slug'] == slug)
    slug_post = get_object_or_404(Post,slug=slug)

    return render(request,'blog/post-details.html',{
        "post": slug_post,
        "post_tags": slug_post.tags.all()
    }) 