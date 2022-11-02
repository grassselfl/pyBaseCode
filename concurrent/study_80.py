import os
from threading import Thread


def func(a, b):
    global g
    g = 0
    print(g, os.getpid())


g = 100
f = g
t_list = []
for i in range(10):
    t = Thread(target=func, args=(i, 5))
    t.start()
    t_list.append(t)
for t in t_list: t.join()
print(g)
print(g, f)
# 全局变量在多个线程之间共享
