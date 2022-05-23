from threading import Thread, current_thread, Lock
import time
from queue import Queue
# db_count = 0
#
# def increase(lock):
#     global db_count
#     with lock:
#         local_count = db_count
#         local_count += 1
#         time.sleep(0.1)
#         db_count = local_count
#
# if __name__ == '__main__':
#     lock = Lock()
#     print('start value:', db_count)
#     thread1 = Thread(target=increase, args=(lock, ))
#     thread2 = Thread(target=increase, args=(lock, ))
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     print('end value', db_count)

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} process {value}')
        q.task_done()

if __name__ == '__main__':
    queue = Queue()
    num_threads = 10
    lock = Lock()
    for i in range(num_threads):
        thread = Thread(target = worker, args=(queue, lock))
        thread.daemon=True
        thread.start()

    for i in range(1, 21):
        queue.put(i)

    queue.join()
    print('end main')