"""
mcrawler.data_cleaner.py
"""

from functools import wraps


def checker(input_data):
    """

    :param input_data: required fields at python list.
    :return:
    """

    def decorator(func):

        @wraps(func)
        def wrapper(data):
            for key in input_data:
                if not (key in data and len(data[key]) != 0):
                    raise Exception(f'{key} value not entered.')
            return func(data)

        return wrapper

    return decorator

