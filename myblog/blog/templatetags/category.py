#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/3/30 16:22
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: category.py
# @Software: PyCharm

from django import template
from blog.models import Category, Sidebar, Post

register = template.Library()


@register.simple_tag
def get_category_list():
    """获取分类列表"""
    return Category.objects.all()


@register.simple_tag
def get_sidebar_list():
    """ 获取侧边栏模块 """
    return Sidebar.get_sidebar()


@register.simple_tag
def get_new_post():
    """ 获取最新文章 """
    return Post.objects.order_by('-mod_date')[:5]


@register.simple_tag
def get_archives():
    """文章归档"""
    # 按月份归档
    return Post.objects.dates('add_date', 'month', order='DESC')[:12]


@register.simple_tag
def get_hot_post():
    """ 按浏览量排名 """
    return Post.objects.order_by('-pv')[:10]
