from django.urls import path
from facebook.api.views import *

app_name = 'facebook_crawler_api'
urlpatterns = [

    path('set-cookies', set_cookies_api_view, name='set_cookies_api_view'),
    path('get-profile', get_profile_api_view, name='get_profile_api_view'),
    path('get-friends', get_friends_api_view, name='get_friends_api_view'),
    path('get-page-info', get_page_info_api_view, name='get_page_info_api_view'),
    path('get-group-info', get_group_info_api_view, name='get_group_info_api_view'),
    path('get-posts', get_posts_api_view, name='get_posts_api_view'),
    path('get-photos', get_photos_api_view, name='get_photos_api_view'),
]
