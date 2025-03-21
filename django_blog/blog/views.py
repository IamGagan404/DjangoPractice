from django.shortcuts import render,get_object_or_404
from .models import Post
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import CommentForm

dummy_posts = []

# def starting_page(request):
#     # sorted_posts = sorted(dummy_posts,key=(lambda x: x['date']))
#     # latest_posts = sorted_posts[-3:]
#     # return render(request,'blog/index.html', {
#     #     "posts":latest_posts
#     # }) 
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request,'blog/index.html', {
#         "posts":latest_posts
#     })

class IndexView(View):
    def get(self,request):
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request,'blog/index.html', {
            "posts":latest_posts
        })


# def posts(request):
#     posts = Post.objects.all()
#     return render(request,'blog/all-posts.html',{
#         "all_posts": posts
#     }) 

class PostListView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"] 


def post_detail(request, slug):
    # slug_post = next(post for post in dummy_posts if post['slug'] == slug)
    slug_post = get_object_or_404(Post,slug=slug)

    return render(request,'blog/post-details.html',{
        "post": slug_post,
        "post_tags": slug_post.tags.all()
    }) 

# class PostDetailView(DetailView):
#     template_name = 'blog/post-details.html'
#     model = Post
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] =  self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context
    
class PostDetailView(View):

    def is_stored_posts(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self,request,slug):

        
        post = Post.objects.get(slug=slug)
        
        post_tags = post.tags.all()
        commentform = CommentForm()
        return render(request,'blog/post-details.html',{
            "post":post,
           "post_tags": post_tags,
           "comment_form": commentform ,
           "comments": post.comments.all().order_by("-datetime"),
           "saved_for_later" : self.is_stored_posts(request,post.id)
        })
    
    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            # user will not tag the post on comment, as we have given post field in exclude option.
            # therefore extra steps need to be performed to save the post in form and model
            # commit = False will not hit the databse directly instead create a model instance
            # then we can perform modeifications to instance and save manually after.
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        
        post_tags = post.tags.all()
        commentform = comment_form
        return render(request,'blog/post-details.html',{
            "post":post,
           "post_tags": post_tags,
           "comment_form": commentform , 
           "comments": post.comments.all().order_by("-datetime"),
           "saved_for_later" : self.is_stored_posts(request,post.id)
        })
    
class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request,"blog/stored-posts.html",context)
    
    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")


