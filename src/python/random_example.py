import random
import secrets
import numpy as np

# # print value between 0 and 1
# a = random.random()
# print(a)
# a = random.uniform(0, 10)
#
# my_list = list("ABCDEFG")
# print(my_list)
# a = random.choice(my_list)
# print(a)
# a = random.sample(my_list, 3)
# print(a)
# a = random.choices(my_list, k=3)
# print(a)
# random.shuffle(my_list)
# print(my_list)

# my_list = list("ABCDEFG")
# a = secrets.choice(my_list)
# print(a)
# # maximum value is 1111
# a = secrets.randbits(4)
# print(a)
a = np.random.rand(3,3)
print(a)
a = np.random.randint(0, 10, (3, 4))
print(a)
