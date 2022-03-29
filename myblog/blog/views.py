from django.shortcuts import render
from .models import Category, Post, Tag


def index(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', locals())