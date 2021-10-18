import json
from functools import wraps
from django.http import JsonResponse, HttpRequest


def decorator(func):
    @wraps(func)
    def wrapper(request: HttpRequest):
        ret = {}
        try:
            res = func(request)
            ret['Status'] = True
            ret['Message'] = None
            ret['Data'] = res
            return JsonResponse(ret)
        except Exception as exp:
            ret['Status'] = False
            ret['Message'] = exp.args[0]
            ret['Data'] = None
            return JsonResponse(ret)

    return wrapper
