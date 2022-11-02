"""
适用于类中方法的一些装饰器
"""
from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def length(self):
        return pi * 2 * self.r

    @length.setter
    def length(self,l):
        print(l)


    @property
    def n(self):
        pass

    def area(self):
        return pi * self.r ** 2


c = Circle(1)
print(c.area())
print(c.length)
print(c.n)  # 会报错
print(c.__dict__)
print(Circle.__dict__)
c.length = 1  # 不能直接修改，需要借助另一个装饰器函数，尽管这里实质是调用函数，并未进行赋值
print(c.length)



# 自己把自己封了起来，又通过装饰器函数解开，相当于能换个名字。。
