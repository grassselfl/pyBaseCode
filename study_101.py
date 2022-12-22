d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['d'] = 4
d1['c'] = 3  # 此时的d1 = {'a':'A','b':'B','c':'C','d':'D'}
for k, v in d1.items():
    print(k, v)

import collections

d1 = collections.OrderedDict()  # 将普通字典转换为有序字典
d1['a'] = 1
d1['b'] = 2
d1['d'] = 4
d1['c'] = 3
for k, v in d1.items():
    print(k, v)

d1 = {'a': '1', 'b': '2', 'd': '4', 'c': '3'}
d1 = collections.OrderedDict(d1)
for k, v in d1.items():
    print(k, v)


# Python3.6 改写了 dict 的内部算法，Python3.6 版本以后的 dict 是有序的，所以也就无须再关注 dict 顺序性的问题