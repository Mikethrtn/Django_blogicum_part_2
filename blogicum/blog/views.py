from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    # Получаем 5 последних опубликованных постов
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {
        'active_page': 'index',
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    # Получаем пост или возвращаем 404
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        id=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

    context = {
        'id': post_id,
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    # Получаем категорию или возвращаем 404
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    # Получаем посты для этой категории
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category_slug': category_slug,
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
