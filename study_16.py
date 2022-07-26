# list
# dict
# str
# set
# tuple
# range()
# enumerate()

result = set(dir([])) & set(dir({})) & set(dir(dict())) & set(dir(1)) & set(dir(set()))
print([].__class__)
print(result)
print(dir(int))
print(dir(list()))
print(enumerate([]))
print(dir(bool))
print(dir(float))

print(set(dir([].__iter__())) - set(dir([])))

l = [1, 2, 3]
print(l.__iter__().__next__())
print(l.__iter__().__next__())
iterator = l.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__length_hint__())
print(iterator.__next__())
# print(iterator.__next__())

# 含有__iter__函数方法即可迭代

from collections.abc import Iterable, Iterator

print(isinstance([], Iterator))
print(isinstance([], Iterable))


# 可迭代，__iter__
# 迭代器，__iter__，__next__

class A():
    def __iter__(self): pass

    def __next__(self): pass


a = A()
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# for循环循环的是可迭代对象的迭代器

# 迭代器并不会直接在内存中生成所有的数据，节省内存
print(range(3))
print(list(range(3)))
print(range(10000000000))
print(list(range(10000000000)))  # MemoryError

# 可以重写迭代器