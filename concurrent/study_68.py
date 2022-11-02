"""
多进程
信号量
"""

from multiprocessing import Semaphore

sem = Semaphore(4)
sem.acquire()
sem.acquire()
sem.acquire()
sem.acquire()
sem.acquire()
sem.release()