from django.urls import path
from linked_in.api.views import *

app_name = 'linkedin_crawler_api'
urlpatterns = [
    path('', crawler),
]
