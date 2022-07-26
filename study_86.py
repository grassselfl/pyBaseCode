# concurrent
import time
from concurrent.futures import ThreadPoolExecutor


def func(n):
    time.sleep(2)
    return n * n

def call_back(n):
    print("结果是"+n.result().__str__())

tpool = ThreadPoolExecutor()
t_list = []
for i in range(20):
    t = tpool.submit(func,i)
    t.add_done_callback(call_back)
    t_list.append(t)

# tpool.shutdown()#可以不等部分获取结果
print("主线程")
for t in t_list:print(t.result())
