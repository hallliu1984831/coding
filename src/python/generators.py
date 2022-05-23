# def mygenerator():
#     yield 1
#     yield 2
#     yield 3
#
# g = mygenerator();
# for i in g:
#     print(i)

# value = next(g)
# print(f'--{value}')
# print(sorted(g, reverse=True))

# import sys
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums
#
# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# print(sum(firstn(10)))
# print(sum(firstn_generator(10)))
# print(sys.getsizeof(firstn(10)))
# print(sys.getsizeof(firstn_generator(10)))

# def fibnacci(n):
#     a,b = 0,1
#     while a < n:
#         yield a
#         a, b = b, a+b
# fib = fibnacci(5)
# for i in fib:
#     print(i)
import sys

number = (i for i in range(100) if i % 2 == 0)
print(list(number))
print(sys.getsizeof(list(number)))

number1 = [i for i in range(100) if i % 2 == 0]
print(number1)
print(sys.getsizeof(number1))