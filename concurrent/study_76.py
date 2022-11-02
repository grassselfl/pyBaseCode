"""
多进程
进程池、回调函数
"""

# 回调函数
import os
from multiprocessing import Pool


def func1(n):
    print("in func1")
    print(n, os.getpid())
    return n


def func2(n):
    print("in func2")
    print(n * n, os.getpid())
    return n * n


if __name__ == "__main__":
    print(os.getpid())
    p = Pool(5)
    # for i in range():
    p.apply_async(func1, args=(10,), callback=func2)
    p.close()
    p.join()
    # p.map()自带close和join
# 回调函数是在主进程进行执行的
