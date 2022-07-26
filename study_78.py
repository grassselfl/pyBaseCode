# 线程
# 用户级线程、内核级线程
import os
import time
from multiprocessing import Process


def func(n):
    time.sleep(1)
    print(n,os.getpid())

if __name__ == "__main__":
    for i in range(10):
        t = Process(target=func, args=(i,))
        t.start()
