"""
生成器深入理解
"""


# 生成器深入理解1
def demo():
    for i in range(4):
        yield i


g = demo()
g1 = (i for i in g)
print(g1, type(g1))
g2 = (i for i in g1)
print(g2, type(g2))
print(list(g1))  # [0, 1, 2, 3]
print(list(g2))  # [] 因为执行的时候g1只是一个能产生[0, 1, 2, 3]的迭代器，并不同于值本身


# 生成器深入理解2
def add(n, i):
    return n + i


def wtest1():
    for i in range(4):
        yield i


g = wtest1()
for n in [1, 10]:
    g = (add(n, i) for i in g)  # 生成器表达式，不实际取元素的时候是不会列出元素的
print(list(g))
# g = wtest1()
# n = 1
# g = (add(n, i) for i in g)
# n = 10
# g = (add(n, i) for i in g)
# list(g)

# n取最后一个
# 生成器不作用
