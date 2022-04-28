from django.urls import path
from . import views

urlpatterns = [
    path('user/signup', views.CreateUserView.as_view()),
    path('user/login', views.LoginView.as_view()),
]
