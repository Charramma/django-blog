from django import forms

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
    re_password = forms.CharField(label='', min_length=5, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': '请再次输入密码'
    }))

    def sim_check(self):
        """ 检查两次输入的密码是否一致 """
        if self.cleaned_data['password'] != self.cleaned_data['re_password']:
            raise forms.validationError("两次输入的密码不一致！")
        return self.cleaned_data['password']
