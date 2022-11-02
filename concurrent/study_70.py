"""
多进程
红绿灯例子
"""

import random
import time
from multiprocessing import Event, Process


def car_process(e, i):
    if not e.is_set():
        print("car%i在等待" % i)
        e.wait()
    print("\033[0;32;40mcar%i通过\033[0m" % i)


def light_process(e):
    while True:
        if not e.is_set():
            time.sleep(5)
            e.set()
            print("\033[32m绿灯亮了\033[0m")
        else:
            time.sleep(2)
            e.clear()
            print("\033[31m红灯亮了\033[0m")



if __name__ == "__main__":
    e = Event()
    traffic = Process(target=light_process, args=(e,))
    traffic.start()
    for i in range(20):
        car = Process(target=car_process, args=(e, i))
        car.start()
        time.sleep(random.random())
