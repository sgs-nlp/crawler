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
    """
    for selected true function
    :param request:
    :return:
    """
    data = dict(request.POST)
    data['c_user'] = cookie['c_user']
    data['xs'] = cookie['xs']
    return facebook_switch_control(data)
