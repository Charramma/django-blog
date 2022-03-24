from django.core.mail import send_mail
from users.models import EmailVerifyRecord
import random
import string


def send_resetpwd_mail(email):
    # 生成6位随机验证码
    code = "".join(random.choices(string.ascii_letters+string.digits, k=6))
    
    # 存储本次生成的验证码
    emailverifyrecord = EmailVerifyRecord()
    emailverifyrecord.code = code
    emailverifyrecord.email = email
    emailverifyrecord.save()
    
    # 邮件主题
    title = "密码重置邮件"
    # 邮件内容
    msg = f"请点击如下链接重置密码，链接一小时内有效。\nhttp://1.117.234.26:8001/users/reset_pwd/{code}/"
    # 寄件人
    sender = 'huang.zyn@qq.com'
    send_mail(title, msg, sender, [email])

    