# from facebook_scraper import get_posts, get_profile, set_cookies
# from typing import Any, Dict, Iterator, Optional, Set, Union
# from facebook_scraper.fb_types import Credentials, Post, RawPost, Profile
#
#
# def cookies_setter(cookies: dict = None):
#     default_cookies = {
#         'c_user': '100073774174685',
#         'xs': '15%3Aa71rNkIU64Jlhw%3A2%3A1633929122%3A-1%3A-1%3A%3AAcUDlLcTfHPCKqwzId7KMYOctgyu4nbhrV4ef3aSPA',
#     }
#     cookies = cookies if cookies is not None else default_cookies
#     set_cookies(cookies)
#
#
# def posts(
#         account: Optional[str] = None,
#         group: Union[str, int, None] = None,
#         post_urls: Optional[Iterator[str]] = None,
#         credentials: Optional[Credentials] = None,
#         **kwargs,
# ):
#     temp = get_posts(account, group, post_urls, credentials)
#
#
#     return JsonResponse({'test': 'test'})
