# 线程锁
# 递归锁==可重入锁

from threading import Lock, RLock, Condition, Thread

# 信号量
from threading import Semaphore, Event

# Condition
def func(condition,i):
    condition.acquire()
    condition.wait()
    print("在第%s个循环里"%i)
    condition.release()

condition = Condition()
for i in range(10):
    Thread(target=func,args=(condition,i)).start()
while True:
    num = int(input(">>>"))
    condition.acquire()
    condition.notify(num)
    condition.release()