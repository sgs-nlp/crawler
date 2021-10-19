from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST

from base_settings.models import APPLICATIONS


@require_POST
def get_all_application_name(request: HttpRequest):
    """

    :param request:
    :return:
    """
    apps_name = APPLICATIONS.keys()
    return JsonResponse({'apps_name': apps_name})


@require_POST
def get_all_application_api_name(request: HttpRequest):
    """

    :param request:
    :return:
    """
    app_name = request.POST['app_name']
    apis_name = APPLICATIONS[app_name].keys()
    return JsonResponse({'apis_name': apis_name})


@require_POST
def get_all_application_api_input_field_name(request: HttpRequest):
    """

    :param request:
    :return:
    """
    app_name = request.POST['app_name']
    api_name = request.POST['api_name']
    input_fields_name = APPLICATIONS[app_name][api_name]
    return JsonResponse({'input_fields_name': input_fields_name})
