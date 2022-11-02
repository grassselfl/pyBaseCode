"""
多进程
Queue
"""
from multiprocessing import Queue, Process  # 进程安全？

def producer(q):
    q.put("food")
def consumer(q):
    q.get()

if __name__ == "__main__":
    q = Queue()
    p = Process(target=producer,args=(q,))
    c = Process(target=consumer,args=(q,))
    p.start()
    c.start()