"""
多进程
事件
"""
from multiprocessing import Event

e = Event()  # 通过socket通信？？
print(e.is_set())
e.set()
print(e.is_set())
e.clear()
print(e.is_set())
e.wait(3)
print("12345")


