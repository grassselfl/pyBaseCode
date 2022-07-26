# python内置模块

# collections
import collections

print(collections.__all__)  # 为什么会有warning

# namedtuple
from collections import namedtuple

Card = namedtuple('card', ['suits', 'number'])
c1 = Card('红桃', 2)
print(c1, c1.number, c1.suits)

import queue

q = queue.Queue()
q.put(10)
print(q.qsize())
print(q.get())

# deque
from collections import deque

dq = deque()
dq.append(1)
dq.append(2)
print(dq.popleft())
print(dq.pop())

# OrderedDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# defaultdict
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)  # 会有一个None到[]的自动变换
# default_factory是可调用的函数？
print(sorted(d.items()))

dd = defaultdict(lambda: 0)
print(dd['key'])


from collections import Counter
# 计数可哈希对象
l = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(Counter(l))