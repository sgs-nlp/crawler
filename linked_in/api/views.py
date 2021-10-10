from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


def crawler(request: HttpRequest):
    print('sfddddddddddddddddddd')
    return JsonResponse({'test': 'test'})
