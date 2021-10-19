"""
users.urls.py
"""
from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('login', login_view, name='login_url'),
    path('login/done', login_done, name='login_done_url'),
    path('logout', logout_done, name='logout_url'),
]
