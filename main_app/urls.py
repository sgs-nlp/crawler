"""
main_app.urls.py
"""
from django.urls import path

from main_app.views import *

app_name = 'main_application'

urlpatterns = [
    path('', index_view, name='index_url'),
    path('changer', changer_view, name='changer_url'),
]
