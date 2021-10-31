"""
facebook.api.views.py
"""
from django.http import HttpRequest
from django.views.decorators.http import require_POST

from mcrawler.json_response import decorator as returner
from facebook.controller import *

from data_sample import cookie


@returner
@require_POST
def get_profile_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_profile_controller(data)


@returner
@require_POST
def get_friends_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_friends_controller(data)


@returner
@require_POST
def get_page_info_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_page_info_controller(data)


@returner
@require_POST
def get_group_info_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_group_info_controller(data)


@returner
@require_POST
def get_posts_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_account_posts_controller(data)


@returner
@require_POST
def get_photos_api_view(request: HttpRequest):
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return get_photos_controller(data)
