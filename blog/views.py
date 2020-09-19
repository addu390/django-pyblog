from django.shortcuts import render, get_object_or_404
from .models import Post
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    posts = Post.objects.order_by('-updated_at')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context=context)


@cache_page(CACHE_TTL)
def post(request, post_id):
    post_detail = get_object_or_404(Post, post_id=post_id)
    context = {
        'post': post_detail
    }
    print(context)
    return render(request, 'post.html', context=context)
