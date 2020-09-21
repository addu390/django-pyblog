from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .search import search_match, search_term

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
CATEGORIES = {'categories': [list(item) for item in Post.categories]}


# @cache_page(CACHE_TTL)
def index(request):
    # [OFFSET:OFFSET+LIMIT]
    posts = Post.objects.order_by('-updated_at')[:5]
    context = {
        'posts': posts
    }
    context.update(CATEGORIES)
    return render(request, 'index.html', context=context)


# @cache_page(CACHE_TTL)
def post(request, post_id):
    post_detail = get_object_or_404(Post, post_id=post_id)
    context = {
        'post': post_detail
    }
    context.update(CATEGORIES)
    print(context)
    return render(request, 'post.html', context=context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context=context)


def search(request):
    match_id = request.GET.get('q')
    posts = search_match(match_id)
    context = {
        'posts': posts
    }
    context.update(CATEGORIES)
    if posts:
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'no-results.html', context=context)


def search_category(request):
    category_id = request.GET.get('q')
    posts = search_term(category_id)
    context = {
        'posts': posts
    }
    context.update(CATEGORIES)
    if posts:
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'no-results.html', context=context)


def home(request):
    return redirect("/posts")
