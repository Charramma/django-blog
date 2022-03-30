from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag


def index(request):
    """ 博客主页视图 """
    post_list = Post.objects.all()
    # category_list = Category.objects.all()
    return render(request, 'blog/index.html', locals())


def post_detail(request, post_id):
    """ 博客详情页视图 """
    # post_id对应的博客模型对象
    post = get_object_or_404(Post, id=post_id)

    # 前一篇的博文 id__lt=post_id  id>post_id last()查询最后一个对象
    prev_post = Post.objects.filter(id__lt=post_id).last()
    # 后一篇的博文
    next_post = Post.objects.filter(id__gt=post_id).first()

    return render(request, 'blog/detail.html', locals())