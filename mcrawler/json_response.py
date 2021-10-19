"""
mcrawler.json_response.py
"""
from django.http import JsonResponse, HttpRequest

from functools import wraps


def decorator(func):
    """
    for return true json response
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(request: HttpRequest):
        ret = {}
        try:
            res = func(request)
            ret['Status'] = True
            ret['Message'] = None
            ret['Data'] = res
        except Exception as exp:
            ret['Status'] = False
            ret['Message'] = exp.args[0]
            ret['Data'] = None
        finally:
            return JsonResponse(ret)

    return wrapper
