from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('sobre/', about, name='sobre'),
    path('contato/', contact, name='contato'),
]
