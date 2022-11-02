"""
gevent
"""

import threading

from gevent import monkey

import time
import gevent

monkey.patch_all()


def eat():
    while True:
        print("eat", threading.current_thread().name, threading.current_thread())
        time.sleep(0.5)


def drink():
    while True:
        print("drink", threading.current_thread().name, threading.current_thread())
        time.sleep(0.5)


if __name__ == "__main__":
    g1 = gevent.spawn(eat)
    g2 = gevent.spawn(drink)
    g1.join()
    g2.join()
# 协程由用户进行切换，该过程对操作系统透明
