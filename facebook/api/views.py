"""
facebook.api.views.py
"""
from django.http import HttpRequest
from django.views.decorators.http import require_POST

from mcrawler.json_response import decorator as returner
from facebook.controller import *


@returner
@require_POST
def get_profile_api_view(request: HttpRequest):
    return get_profile_controller(request)


@returner
@require_POST
def get_friends_api_view(request: HttpRequest):
    return get_friends_controller(request)


@returner
@require_POST
def get_page_info_api_view(request: HttpRequest):
    return get_page_info_controller(request)


@returner
@require_POST
def get_group_info_api_view(request: HttpRequest):
    return get_group_info_controller(request)


@returner
@require_POST
def get_posts_api_view(request: HttpRequest):
    return get_account_posts_controller(request)


@returner
@require_POST
def get_photos_api_view(request: HttpRequest):
    return get_photos_controller(request)
