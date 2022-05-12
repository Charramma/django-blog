"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d@t@pq6!s3jb=j0gm7kb@p0i-6e%52ocqdceh(zxm^j5pt*tuc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 自定义验证
# https://docs.djangoproject.com/zh-hans/3.2/topics/auth/customizing/
AUTHENTICATION_BACKENDS = {
    "users.views.MyBackend",
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    # django-ckeditor
    'ckeditor',
    'ckeditor_uploader'
]

# 定制化django-ckeditor
CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        # 'width':'auto',
        'height': '250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 文本属性
            ['Styles', 'Format', 'Font', 'FontSize'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色和背景颜色
            ['TextColor', 'BGColor'],
            # 文本对齐方式
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            # 链接
            ['Link', 'Unlink'],
            # 列表、单选、复选框
            ['NumberedList', 'BulletedList', 'Checkbox', 'Radio'],
            # 图片、表格、水平线、特殊符号、表情
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'Smiley'],
            # 引用块、代码块
            ['Blockquote', 'CodeSnippet'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        # 'extraPlugins': ','.join(['codesnippet']),
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'blogApp',
        'PASSWORD': 'blogApp1234#',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 发送邮件所需参数
EMAIL_HOST = 'smtp.qq.com'  # 所使用的smtp服务器
EMAIL_HOST_USER = 'huang.zyn@qq.com'  # 发件人邮箱
EMAIL_HOST_PASSWORD = 'xhflqxclunjfbfha'  # 密钥
EMAIL_PORT = 465
EMAIL_USE_SSL = True  # 是否使用隐式的安全连接
