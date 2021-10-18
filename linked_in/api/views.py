from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from facebook_scraper import get_posts, get_profile, set_cookies
import json


def crawler(request: HttpRequest):
    import requests
    from http import cookies
    cookie = {
        'c_user': '100073774174685',
        # 'datr': 'SLFiYepZhxQhaH87uBvNYwYh',
        # 'fr': '0rh3mHvX63KgVWvts.AWWhQ8hdrQUQGCZsfyIc94bKq7M.BhY9Xs.pA.AAA.0.0.BhY9Xs.AWVlpIZA9Nw',
        # 'local': 'en_US',
        # 'sb': 'SLFiYX4nKlFkmKH3L40NlCzi',
        # 'spin': 'r.1004529891_b.trunk_t.1633929126_s.1_v.2_',
        # 'wd': '1920x969',
        'xs': '15%3Aa71rNkIU64Jlhw%3A2%3A1633929122%3A-1%3A-1%3A%3AAcUDlLcTfHPCKqwzId7KMYOctgyu4nbhrV4ef3aSPA',
    }

    # set_cookies(cookie)
    # temp = get_posts("Nintendo")
    # jt = list(temp)
    # print(jt)
    aList = [41, 58, 63]
    jsonStr = json.dumps(aList)
    print(jsonStr)
    # print('**************')
    # for i in temp:
    #     print(i['text'][:10])

    return HttpResponse(aList)
