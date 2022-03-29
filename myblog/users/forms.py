from django import forms

from django.contrib.auth.models import User
from users.models import UserProfile

class LoginForm(forms.Form):
    """ 登录表单 """
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(auto_id=False, *args, **kwargs)
    
    username = forms.CharField(label='', max_length=22,  widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': '用户名/邮箱'
    }))
    password = forms.CharField(label='', min_length=5, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': '密码'
    }))


class ForgetForm(forms.Form):
    """ 忘记密码表单 """

    def __init__(self, *args, **kwargs):
        super(ForgetForm, self).__init__(auto_id=False, *args, **kwargs)

    email = forms.EmailField(label='', min_length=4, widget=forms.EmailInput(attrs={
        'class': 'input',
        'placeholder': '请输入注册邮箱地址'
    }))


class ModifyPwdForm(forms.Form):
    """ 修改密码表单 """

    def __init__(self, *args, **kwargs):
        super(ModifyPwdForm, self).__init__(auto_id=False, *args, **kwargs)

    password = forms.CharField(label='', min_length=5, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': '请输入新密码'
    }))
    password2 = forms.CharField(label='', min_length=5, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': '请再次输入密码'
    }))

    def clean_password2(self):
        """ 检查两次输入的密码是否一致 """
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("两次输入的密码不一致！")
        return self.cleaned_data['password']


class ModifyUserForm(forms.ModelForm):
    """ 修改用户信息表单 """
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input'
    }))
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ('email', 'username')
    

class ModifyUserProfileForm(forms.ModelForm):
    
    desc = forms.CharField(label='个人简介', widget=forms.TextInput(attrs={
        'class': 'input'
    }))
    sign = forms.CharField(label='个性签名', widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    class Meta:
        model = UserProfile
        fields = ('desc', 'sign', 'image')