from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('detalhes/', blog_details, name='blog_detalhes'),
]
