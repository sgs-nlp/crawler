"""
main_app.views.py
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from base_settings.models import APPLICATIONS
from facebook.controller import switch_controller as facebook_switch_control
from mcrawler.json_response import decorator as returner
from data_sample import cookie


@require_GET
@login_required
def index_view(request: HttpRequest):
    """

    :param request:
    :return: render index.html
    """
    apps_name = APPLICATIONS.keys()
    apis_name = APPLICATIONS['FaceBook'].keys()
    return render(request, 'main_app/index.html', context={
        'apps_name': apps_name,
        'apis_name': apis_name,
    })


@returner
@require_POST
@login_required
def changer_view(request: HttpRequest):
    socks1 = request.POST['socks1']
    socks2 = request.POST['socks2']

    username = request.POST['username']
    password = request.POST['password']

    account_id = request.POST['account_id']

    app_name = request.POST['app_name']
    api_name = request.POST['api_name']
    return switch(app_name, api_name, account_id)


def switch(app_name, api_name, account_id):
    if app_name == 'FaceBook':
        set_cookies(cookie)
        if api_name == 'Profile':
            return get_profile(account=account_id)
        if api_name == 'Friends':
            return get_friends(account=account_id)
        if api_name == 'Page Information':
            return get_page_info(account=account_id)
        if api_name == 'Group Information':
            return get_group_info(group=account_id)
        if api_name == 'Posts':
            return get_posts(account=account_id)
        if api_name == 'Photos':
            return get_photos(account=account_id)
        else:
            return None
    else:
        return None
