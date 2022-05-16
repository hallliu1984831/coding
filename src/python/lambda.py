# my_list=[(5, 10), (3, -1), (7, 8), (6, 3)]
# print(my_list)
#
# my_sorted_list=sorted(my_list, key=lambda x : x[1])
# print(my_sorted_list)
from functools import reduce

# num_list = [1, 3, 5, 7]
# new_list = [x ** 2 for x in num_list if x > 4]
# print(new_list)
#
# map_list = map(lambda x : x ** 2, num_list)
# print(list(map_list))
# map_list = filter(lambda x : x > 4, num_list)
# print(list(map_list))
# result = reduce(lambda x, y : x * y, num_list)
# print(result)

# try:
#     a = 5 / 0
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('nothing')
# finally:
#     print('ok')

class ValueTooBigError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
    pass

def compare(x):
    if x > 100:
        raise ValueTooBigError('value too big')
    elif x < 10:
        raise ValueTooSmallError('Value too small', x)
    else:
        print('ok')

try:
    compare(1)
except ValueTooBigError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)