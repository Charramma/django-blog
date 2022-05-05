from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Tag
from django.db.models import Q
from django.core.paginator import Paginator


def index(request):
    """ 博客主页视图 """
    post_list = Post.objects.all()

    # 分页方法, 每页显示10条
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj})


def post_detail(request, post_id):
    """ 博客详情页视图 """
    # post_id对应的博客模型对象
    post = get_object_or_404(Post, id=post_id)

    # 前一篇的博文 id__lt=post_id  id>post_id last()查询最后一个对象
    prev_post = Post.objects.filter(id__lt=post_id).last()
    # 后一篇的博文
    next_post = Post.objects.filter(id__gt=post_id).first()

    return render(request, 'blog/detail.html', locals())


def search(request):
    """ 搜索视图 """
    # 获取表单
    keyword = request.GET.get('keyword')
    if not keyword:  # 如果没有搜索，显示所有的文章
        post_list = Post.objects.all()
    else:
        # 如果标题、描述、内容里包含所搜索的关键字，则显示出来
        post_list = Post.objects.filter(
            Q(title__icontains=keyword) | Q(desc__icontains=keyword) | Q(content__icontains=keyword))

    content = {
        'post_list': post_list
    }
    # 和首页保持一致
    return render(request, 'blog/index.html', content)


def archives(request, year, month):
    """ 文章归档视图 """
    # 按年和月筛选文章
    post_list = Post.objects.filter(add_date__year=year, add_date__month=month)

    context = {
        "year": year,
        "month": month,
        "post_list": post_list
    }
    return render(request, 'blog/archives_list.html', context=context)