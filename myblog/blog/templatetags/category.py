#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/3/30 16:22
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: category.py
# @Software: PyCharm

from django import template
from blog.models import Category

register = template.Library()


@register.simple_tag
def get_category_list():
    """获取分类列表"""
    return Category.objects.all()