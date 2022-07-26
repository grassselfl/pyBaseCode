# 队列
import queue

q = queue.Queue()
q.put("1")
q.get()
q.put_nowait("2")
q.get_nowait()

queue.LifoQueue()  # 后进先出队列
pq = queue.PriorityQueue()  # 这里优先队列似乎有些问题
pq.put(1)
pq.put(3)
pq.put(4)
print(pq.get())
