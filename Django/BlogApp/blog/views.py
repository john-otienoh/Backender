from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

def home(request):
    return render(request, "blog/index.html")

def post_list(request):
    posts = Post.published.all()
    return render(
        request, "blog/pages/list.html", {"posts": posts}
    )

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
