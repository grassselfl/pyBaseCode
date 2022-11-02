"""
多进程
JoinableQueue
"""
import time
import random
from multiprocessing import JoinableQueue, Process


def producer(q, name, food):
    for i in range(5):
        time.sleep(random.random())
        fd = '%s%s' % (food, i + 1)
        q.put(fd)
        print('%s生产了一个%s' % (name, food))
    q.join()  # (3)生产者for循环生产完所有产品，需要q.join()阻塞一下，对这个队列进行阻塞。


# (5)我启动了生产者之后，生产者函数一直在生成数据，直到生产完所有数据将队列q.join()一下，意思是当我生产的数据都被消费者消费完之后 队列的阻塞才结束。
def consumer(q, name):  # (1)消费者不需要像Queue那样判断从队列里拿到None再退出执行消费者函数了
    while True:
        food = q.get()
        time.sleep(random.random())
        print('%s吃了%s' % (name, food))
        q.task_done()  # (2)消费者每次从队列里面q.get()一个数据，处理过后就使用队列.task_done()


if __name__ == '__main__':
    jq = JoinableQueue()
    p = Process(target=producer, args=(jq, '喜洋洋', '包子'))  #
    p.start()  # (4)启动一个生产者，启动一个消费者，并且这个消费者做成守护进程，然后生产者需要p.join()阻塞一下。
    c = Process(target=consumer, args=(jq, '灰太狼'))
    c.daemon = True  #
    c.start()
    p.join()
