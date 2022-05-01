from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('user/signup', views.CreateUserView.as_view(), name='signup'),
    path('user/login', views.LoginView.as_view(), name='login'),
]
