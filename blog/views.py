from django.shortcuts import render
from .models import Post


def index(request):
    num_books = Post.objects.order_by('-updated_at')[:5]
    context = {
        'posts': num_books
    }
    print(context)
    return render(request, 'index.html', context=context)
