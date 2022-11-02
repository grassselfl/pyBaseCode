"""
给生成器传参
"""


def generator():
    print(1)
    content = yield 111
    print(2, content)
    content = yield 222
    print(3, content)
    yield


g = generator()
print(g.__next__())
print(g.send("content"))  # 需要给上一个yield位置传参，第一个需要用__next__，同理最后一个yield无法获取到值，不过可以yield空
print(g.send("content666"))


# 一个动态系统
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


avg = average()
print(avg.__next__())
print(avg.send(10))
print(avg.send(12))
print(avg.send(10))
print(avg.send(20))


def f():
    a = '123456'
    for i in a:  # 一般写法
        yield i
    yield from a  # 简写


g = f()
for i in g:
    print(i)
