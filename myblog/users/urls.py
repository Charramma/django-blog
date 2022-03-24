from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('forget_pwd/', views.forget_pwd, name='forget_pwd'),
    path('logout/', views.logout_view, name='logout'),
    path('reset_pwd/<code>/', views.reset_pwd, name='reset_pwd'),
    path('user_profile/', views.user_profile, name='user_profile')
]