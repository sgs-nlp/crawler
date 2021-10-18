from django.http import HttpRequest, HttpResponse, JsonResponse
from facebook_scraper import set_cookies, get_posts, get_profile, get_friends, get_page_info, get_group_info, get_photos
from mcrawler.json_response import decorator as returner
from mcrawler.to_dict import todict
from django.views.decorators.http import require_GET, require_POST

cookie = {
    'c_user': '100002423197632',
    'xs': '44%3Ag6UTHg8W4ZdUdA%3A2%3A1634555056%3A-1%3A9726',
}


@returner
@require_POST
def set_cookies_api_view(request: HttpRequest):
    cookie = {
        'c_user': '100073774174685',
        'xs': '10%3AETf3okldRYv5_Q%3A2%3A1634018864%3A-1%3A-1',
    }

    set_cookies(cookie)
    return HttpResponse(True)


@returner
@require_POST
def get_profile_api_view(request: HttpRequest):
    account = None
    if 'account' in request.POST and len(request.POST['account']) != 0:
        account = request.POST['account']
    else:
        raise Exception('Set one of the following values:\n- account')
    set_cookies(cookie)
    profile = get_profile(account)
    return profile


@returner
@require_POST
def get_friends_api_view(request: HttpRequest):
    account = None
    if 'account' in request.POST and len(request.POST['account']) != 0:
        account = request.POST['account']
    else:
        raise Exception('Set one of the following values:\n- account')
    set_cookies(cookie)
    profile = get_friends(account)
    return list(profile)


@returner
@require_POST
def get_page_info_api_view(request: HttpRequest):
    account = None
    if 'account' in request.POST and len(request.POST['account']) != 0:
        account = request.POST['account']
    else:
        raise Exception('Set one of the following values:\n- account')
    set_cookies(cookie)
    profile = get_page_info(account)
    return profile


@returner
@require_POST
def get_group_info_api_view(request: HttpRequest):
    group = None
    if 'group' in request.POST and len(request.POST['group']) != 0:
        group = request.POST['group']
    else:
        raise Exception('Set one of the following values:\n- group')
    set_cookies(cookie)
    profile = get_group_info(group)
    return profile


@returner
@require_POST
def get_posts_api_view(request: HttpRequest):
    account = None
    group = None
    if 'account' in request.POST and len(request.POST['account']) != 0:
        account = request.POST['account']
    elif 'group' in request.POST and len(request.POST['group']) != 0:
        group = request.POST['group']
    else:
        raise Exception('Set one of the following values:\n- account\n- group')
    set_cookies(cookie)
    posts = get_posts(account=account, group=group)
    posts = list(posts)
    return posts


@returner
@require_POST
def get_photos_api_view(request: HttpRequest):
    account = None
    if 'account' in request.POST and len(request.POST['account']) != 0:
        account = request.POST['account']
    else:
        raise Exception('Set one of the following values:\n- account')
    set_cookies(cookie)
    profile = get_photos(account)
    return list(profile)
