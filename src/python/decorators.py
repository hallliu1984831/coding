# def custom_decorator(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
#
# @custom_decorator
# def print_name():
#     print('hi')
#
# print_name()

import functools
def custom_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@custom_decorator1
def add_x(x):
    return x + 5

result = add_x(10)
print(result)
print(help(add_x))
print(add_x.__name__)