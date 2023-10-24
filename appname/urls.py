# appname/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.user_list, name='user-list'),
    path('user-input/', views.user_input, name='user-input'),
]
