# GIL 全局解释器锁 Global Interpreter Lock
# CPython解释器中 在CPython解释器中执行的每一个Python线程，都会先锁住自己，以阻止别的线程执行
# 解释型语言本身问题
# CPython不支持并行，仅支持并发
# 在CPython解释器下的Python程序，同一时刻某一进程下的多个线程中只能有一个线程被CPU执行，即利用不了多核，只能用单核
# 所以要用的话还是用多进程或者分布式计算
# thread包不完善
import threading
import time

print(threading.current_thread())
print(threading.currentThread())
# 命名兼容666

def func():
    print(threading.currentThread())
    print(threading.get_ident())
    time.sleep(1)

for i in range(10):
    t =  threading.Thread(target=func)
    # t.run()#???
    t.setName(i.__str__())
    t.start()
print()
print(threading.active_count())
print(threading.currentThread())