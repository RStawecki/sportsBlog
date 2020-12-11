from django.shortcuts import render, get_object_or_404
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
