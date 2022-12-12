from django.shortcuts import render, get_object_or_404
from post.models import Post
from .forms import PostForm
from author.models import Author


# Create your views here.


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, "post/posts.html", locals())


def detail_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "post/detail.html", locals())


def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        author = get_object_or_404(Author, id=data.get("author"))
        Post.objects.create(title=data.get("title"),
                            description=data.get("description"),
                            author=author)
    return render(request, "post/create.html", locals())
