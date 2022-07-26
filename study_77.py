# 线程
# 用户级线程、内核级线程
import os
import time
from threading import Thread


def func(n):
    time.sleep(1)
    print(n,os.getpid())

for i in range(10):
    t = Thread(target=func, args=(i,))
    t.start()
