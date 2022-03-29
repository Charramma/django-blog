from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('forget_pwd/', views.forget_pwd, name='forget_pwd'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_pwd/<code>/', views.reset_pwd, name='reset_pwd'),
    path('reset_pwd_inner/', views.reset_pwd_inner, name='reset_pwd_inner'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('editor_users/', views.editor_users, name='editor_users')
]