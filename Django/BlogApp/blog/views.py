from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
# Create your views here.

# def home(request):
#     return render(request, "blog/index.html")

def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 4)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request, "blog/list.html", {"posts": posts, "page_obj": posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, status=Post.Status.PUBLISHED, slug=post,
        publish__year=year, publish__month=month, publish__day=day
    )
    return render(request, 'blog/detail.html', {'post': post})
