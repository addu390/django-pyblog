from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.order_by('-updated_at')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context=context)


def post(request, post_id):
    post_detail = get_object_or_404(Post, post_id=post_id)
    context = {
        'post': post_detail
    }
    print(context)
    return render(request, 'post.html', context=context)
