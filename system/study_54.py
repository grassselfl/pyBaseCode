import sys

from oop import s8

g = 10

# 反射模块

s = getattr(s8, 's')
print(s)

f = getattr(s8, 'A')

a = f()
print(a)
print(sys.getrefcount(a))
print(sys.modules)
print(sys.modules['__main__'])
print(sys.modules['__main__'].g)

# !!!!!!一切的一切都是用一个内存地址来调用！！！！！！，一切都是地址
# 一切是地址、一切皆对象

# 666
print(getattr(sys.modules['__main__'], 'g'))
f = getattr(sys.modules['study_53'], 'A')
a = f()
print(a)
