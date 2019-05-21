from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register'),
    path('manage/', manage, name='manage'),
]
