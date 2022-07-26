# 列表推导式、集合推导式、字典推导式
data = [i ** 2 for i in range(100) if i % 3 == 0]
print(data, type(data))

g = (i ** 2 for i in range(100) if i % 3 == 0)
print(g, type(g))

# 许多函数使用迭代器方式访问对象，而生成器是一种迭代器，所以可以直接
print(sum(i ** 2 for i in range(100) if i % 3 == 0))
print(sum([i ** 2 for i in range(100) if i % 3 == 0]))


# 集合推导式结果会去重

# 生成器深入理解1
def demo():
    for i in range(4):
        yield i


g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g1))  # [0, 1, 2, 3]
print(list(g2))  # []


# 生成器深入理解2
def add(n, i):
    return n + i


def wtest1():
    for i in range(4):
        yield i


g = wtest1()
for n in [1, 10]:
    g = (add(n, i) for i in g)
print(list(g))
# g = wtest1()
# n = 1
# g = (add(n, i) for i in g)
# n = 10
# g = (add(n, i) for i in g)
# list(g)

# n取最后一个
# 生成器不作用
