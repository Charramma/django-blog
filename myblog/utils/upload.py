#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2022/5/12 15:05
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: upload.py
# @Software: PyCharm


import os
import uuid
from django.conf import settings    # 配置文件
from django.views.decorators.csrf import csrf_exempt    # 取消csrftoken
from django.http import JsonResponse    # 访问json格式的数据


# 该装饰器用于csrf_token合法性验证
@csrf_exempt
def upload_file(request):
    # 获取表单上传的图片
    upload = request.FILES.get('upload')
    # 生成随机字符串，作为图片名
    uid = "".join(str(uuid.uuid4()).split('-'))
    # 修改图片名
    names = str(upload.name).split('.')
    names[0] = uid
    # 返回修改过的图片格式
    upload.name = '.'.join(names)

    # 拼接上传路径
    new_path = os.path.join(settings.MEDIA_ROOT, 'upload', upload.name)
    with open(new_path, 'wb+') as f:
        for chunk in upload.chunks():
            f.write(chunk)

    # 构造返回的数据
    filename = upload.name
    url = '/media/upload/' + filename
    response = {
        'url': url,
        'uploaded': '1',
        'fileName': filename
    }
    return JsonResponse(response)