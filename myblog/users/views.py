from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend   # django默认身份验证后端
from .forms import LoginForm, ForgetForm, ModifyPwdForm, ModifyUserForm, ModifyUserProfileForm
from django.db.models import Q
from .models import EmailVerifyRecord, UserProfile
from django.utils import timezone
import datetime
from utils.email_send import send_resetpwd_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required   # django鉴权模块

# Create your views here.

class MyBackend(ModelBackend):
    """ 重写django身份验证后端，实现邮箱登录 """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def login_view(request):
    """ 登录视图 """
    if request.method != 'POST':
        # 不是POST请求就获取空表单
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
           
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('登录失败')
    
    return render(request, 'users/login.html', context={'form': form})


def forget_pwd(request):
    """ 忘记密码 """
    if request.method != 'POST':
        form = ForgetForm()
    else:
        form = ForgetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            exist = User.objects.filter(email=email).exists()
            if exist:
                send_resetpwd_mail(email)
                return render(request, 'users/forget.html', {'form': form, 'msg': '邮件已发送，请注意查收。'})
            else:
                err_info = '该邮箱未注册！请检查输入是否有误。'
                return render(request, 'users/forget.html', {'form': form, 'err_info': err_info})
    return render(request, 'users/forget.html', {'form': form})


def logout_view(request):
    """ 退出登录 """
    logout(request)
    return redirect('users:login')


def reset_pwd(request, code):
    """ 重置密码 """
    record = EmailVerifyRecord.objects.get(code=code)
    # 判断是否在一个小时内点击链接
    if timezone.now()-record.ge_date < datetime.timedelta(hours=1):
        if request.method != 'POST':
            form = ModifyPwdForm()
            return render(request, 'users/reset_pwd.html', {'form': form})
        else:
            form = ModifyPwdForm(request.POST)
            if form.is_valid():
                email = record.email
                user = User.objects.get(email=email)
                user.password = make_password(form.cleaned_data.get('password'))
                user.save()
                return HttpResponse('密码修改成功！')
            else:
                return HttpResponse('密码修改失败！')
    else:
        return HttpResponse('链接超时！')


@login_required(login_url='users:login')
def reset_pwd_inner(request):
    """ 登录后在个人主页重置密码 """
    user = User.objects.get(id=request.user.id)
    if request.method != 'POST':
        form = ModifyPwdForm()
        return render(request, 'users/reset_pwd.html', {'form': form})
    else:
        form = ModifyPwdForm(request.POST)
        if form.is_valid():
            user.password = make_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponse('密码修改成功！')
        else:
            return HttpResponse('密码修改失败！')




# 如果没有登录，跳转到登录界面
@login_required(login_url='users:login')
def user_profile(request):
    """ 用户信息展示 """
    user = User.objects.get(username=request.user)
    return render(request, 'users/user_profile.html', {'user': user})

@login_required(login_url='users:login')
def editor_users(request):
    """ 修改用户信息 """
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        try:
            # 如果userprofile存在
            user_profile = user.userprofile
            # 获取表单数据
            user_form = ModifyUserForm(request.POST, instance=user)
            userprofile_form = ModifyUserProfileForm(request.POST, request.FILES, instance=user_profile)
            # 保存
            if user_form.is_valid() and userprofile_form.is_valid():
                user_form.save()
                userprofile_form.save()
                # 转到个人信息展示页面
                return redirect('users:user_profile')
        except UserProfile.DoesNotExist:
            # 该用户在userprofile表中还没有对应的数据

            # 获取表单信息
            user_form = ModifyUserForm(request.POST, instance=user)
            userprofile_form = ModifyUserProfileForm(request.POST, request.FILES)
            # 保存
            if user_form.is_valid() and userprofile_form.is_valid():
                user_form.save()
                # commit=False 先不保存，放在内存中，然后再重新给指定字段赋值
                new_userprofile = userprofile_form.save(commit=False)
                new_userprofile.owner = request.user
                new_userprofile.save()
                return redirect('users:user_profile')
    else:
        try:
            user_profile = user.userprofile
            user_form = ModifyUserForm(instance=user)
            userprofile_form = ModifyUserProfileForm(instance=user_profile)
        except UserProfile.DoesNotExist:
            user_form = ModifyUserForm(instance=user)
            userprofile_form = ModifyUserProfileForm()
    return render(request, 'users/editor_users.html', locals())