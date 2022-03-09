from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名/邮箱", max_length=22, widget=forms.TextInput())
    password = forms.CharField(label='密码', min_length=5, widget=forms.PasswordInput())

class ForgetForm(forms.Form):
    email = forms.EmailField(label='请输入注册邮箱地址', min_length=4, widget=forms.EmailInput())