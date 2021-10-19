"""
facebook.controller.py
"""
from facebook_scraper import set_cookies, get_posts, get_profile, get_friends, get_page_info, get_group_info, get_photos
from mcrawler.data_cleaner import checker as data_cleaner_checker


@data_cleaner_checker(['c_user', 'xs', ])
def set_cookies_controller(data):
    """

    :param data:
    :return:
    """
    cookie = {
        'c_user': data['c_user'],
        'xs': data['xs'],
    }
    set_cookies(cookie)
    return cookie


@data_cleaner_checker(['account', ])
def get_profile_controller(data):
    """

    :param data:
    :return:
    """
    account = data['account']
    set_cookies_controller(data)
    return get_profile(account)


@data_cleaner_checker(['account', ])
def get_friends_controller(data):
    """

    :param data:
    :return:
    """
    account = data['account']
    set_cookies_controller(data)
    return list(get_friends(account))


@data_cleaner_checker(['account', ])
def get_page_info_controller(data):
    """

    :param data:
    :return:
    """
    account = data['account']
    set_cookies_controller(data)
    return get_page_info(account)


@data_cleaner_checker(['group', ])
def get_group_info_controller(data):
    """

    :param data:
    :return:
    """
    group = data['group']
    set_cookies_controller(data)
    return get_group_info(group=group)


@data_cleaner_checker(['account', ])
def get_account_posts_controller(data):
    """

    :param data:
    :return:
    """
    account = data['account']
    set_cookies_controller(data)
    return list(get_posts(account=account))


@data_cleaner_checker(['group', ])
def get_group_posts_controller(data):
    """

    :param data:
    :return:
    """
    group = data['group']
    set_cookies_controller(data)
    return list(get_posts(group=group))


@data_cleaner_checker(['account', ])
def get_photos_controller(data):
    """

    :param data:
    :return:
    """
    account = data['account']
    set_cookies_controller(data)
    return list(get_photos(account))


@data_cleaner_checker(['app_name', 'api_name'])
def switch_controller(data):
    """

    :param data:
    :return:
    """
    if data['app_name'] == 'FaceBook':
        if data['api_name'] == 'Profile':
            return get_profile_controller(data)
        if data['api_name'] == 'Friends':
            return get_friends_controller(data)
        if data['api_name'] == 'Page Information':
            return get_page_info_controller(data)
        if data['api_name'] == 'Group Information':
            return get_group_info_controller(data)
        if data['api_name'] == 'Posts':
            return get_account_posts_controller(data)
        if data['api_name'] == 'Photos':
            return get_photos_controller(data)
        else:
            raise Exception('Select api.')
    else:
        raise Exception('Select application.')
