"""
多进程
启动一个进程
"""
import os
import time
from multiprocessing import Process


def func(args, io):  # 元组元素与函数参数对应
    print(args)


if __name__ == "__main__":
    p = Process(target=func, args=('lm', 12))
    p.start()
    print(os.getpid())  # 任务管理器详细信息可以查看PID
    print(os.getppid())
