# print(id([]))
# print(id([123]))
# print(id([12]))
#
# m = [23]
# print(id(m))
# print(id([]))


def add(a=[]):
    a.append(1)
    print(a)
    print(id([]))
    b = []
    print(id(b))
    v = []
    print(id(v))


# f = add
#
# f()
#
# b = []
add()
g = [1]
print(id(g))
# []可能与缓存机制有关
# 函数中的默认参数会在加载函数时保存在堆中，如果默认参数是可变参数，就会在多次调用函数间有累积作用
# 两种情况是不同机制

