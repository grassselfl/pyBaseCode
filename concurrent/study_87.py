"""
协程
"""

# 协程
# 轻量级线程、用户级线程
# 在单线程下完成任务，但是多个任务交替进行规避IO浪费
# 代码单纯发出指令？？？CPU发出，具体设备执行耗时

# yield实现携程
import time


def eat():
    while True:
        print("eat")
        yield
        time.sleep(0.5)


def drink():
    while True:
        print("drink")
        yield
        time.sleep(0.5)


if __name__ == "__main__":
    e = eat()
    d = drink()
    while True:
        e.__next__()
        d.__next__()
