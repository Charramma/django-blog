from django.db import models
# Django内置用户user模型
from django.contrib.auth.models import User


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    desc = models.TextField('个人简介', max_length=200, blank=True, default='')
    sign = models.TextField('个性签名', max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100, verbose_name='用户头像')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.owner.username