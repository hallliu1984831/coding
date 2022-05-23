# from multiprocessing import Process, Value, Array, Lock
import os
import time

# def square_num():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)
#
# processes = []
# num_process = os.cpu_count()
#
# # create processes
# for i in range(num_process):
#     p = Process(target=square_num)
#     processes.append(p)
#
# # start process
# for p in processes:
#     p.start()
#
# # join
# for p in processes:
#     p.join()
#
# print('end main')

# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1
#
# if __name__ == '__main__':
#     share_num = Value('i', 0)
#     print('start', share_num.value)
#     lock = Lock()
#     p1 = Process(target=add_100, args=(share_num, lock))
#     p2 = Process(target=add_100, args=(share_num, lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('end', share_num.value)

# def add_100(share_array, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#             for i in range(len(share_array)):
#                 share_array[i] += 1
#
# if __name__ == '__main__':
#     share_array = Array('d', [0.0, 100.0, 200.0])
#     print('start', share_array[:])
#     lock = Lock()
#     p1 = Process(target=add_100, args=(share_array, lock))
#     p2 = Process(target=add_100, args=(share_array, lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('start', share_array[:])
#
# from multiprocessing import Queue
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i * i)
#
# def negative(numbers, queue):
#     for i in numbers:
#         queue.put(-1 * i)
#
# if __name__ == '__main__':
#     numbers = range(1, 6)
#     queue = Queue()

    # p1 = Process(target=square, args=(numbers, queue))
    # p2 = Process(target=negative, args=(numbers, queue))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # while not queue.empty():
    #     print(queue.get())

from multiprocessing import Pool
def cube(number):
    return number ** 3
if __name__ == '__main__':
    numbers = range(10)
    pool = Pool()
    # map, close, apply, join
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()
    print(result)

    # pool.apply(cube, numbers[0])

