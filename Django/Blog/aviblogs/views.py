from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.decorators.http import require_POST
from .forms import CommentForm, EmailPostForm
from taggit.models import Tag
from django.db.models import Count


# Create your views here.
def post_list(request, tag_slug=None):
    post_list = Post.objects.all(filter=Status.PUBLISHED)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])  # Pagination with 3 posts per
        paginator = Paginator(post_list, 9)
        page_number = request.GET.get("page", 1)
        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    return render(request, "aviblogs/blogs.html", {"posts": posts, "tag": tag})


def home(request):
    return render(request, "index.html")


class PostList(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "aviblogs/blogs.html"


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid:
            cd = form.cleaned_data
        else:
            form = EmailPostForm()
    return render(request, "aviblogs/share.html", {"post": post, "form": form})


def post_detail(request, year, month, day, post):
    ost = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    post_tags_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )[:4]
    return render(
        request,
        "aviblog/post.html",
        {
            "post": post,
            "comments": comments,
        },
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return render(
            request,
            "blog/post/comment.html",
            {"post": post, "form": form, "comment": comment},
        )
