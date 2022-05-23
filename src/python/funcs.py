# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     # *args: tuple
#     for i in args:
#         print(i)
#     # **kwargs
#     for key in kwargs:
#         print(key, kwargs[key])
#
# foo(1,2,3,4,5,six=6,seven=7)
# foo(1,2,3,4)
# foo(1,2,six=6,seven=7)

# def foo(a, b, *, c, d):
#     # * means the params which after that must be key-word args
#     print(a, b, c, d)
# foo(1, 2, c=4, d=5)

# def foo(*args, last):
#     for i in args:
#         print(i)
#     print(last)
# foo(1,2, last=3)

# unpack
# def foo(a, b, c):
#     print(a, b, c)
#
# my_list = [0, 1, 2]
# foo(*my_list)
#
# my_tuple = (0, 1, 2)
# foo(*my_tuple)
#
# my_dict = {'a':1, 'b':2, 'c':3}
# foo(**my_dict)

# global
# def foo():
#     global number
#     number = 3
#
# number = 0
# foo()
# print(number)

# def foo(list):
#     list.append(4)
#     list[0] = -2
#
# list = [1,2,3]
# foo(list)
# print(list)

# my_list = (1,2,3,4,5)
# begin, *middle, last = my_list
# print(begin)
# print(middle)
# print(last)

# my_list=(1,2,3)
# my_array=[7,8,9]
# my_set={4,5,6}
# new_list=[*my_list, *my_set, *my_array]
# print(new_list)

my_dict1={'a':1, 'b':2}
my_dict2={'c':3, 'd':4}
new_dict={**my_dict1, **my_dict2}
print(new_dict)