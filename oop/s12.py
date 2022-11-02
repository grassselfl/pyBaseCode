"""
关于多继承的一个解析顺序
"""
class A:
    pass
    # def func(self): print("A")


class B(A):
    def func(self): print("B")


class C(A):
    def func(self): print("C")

class D(B,C):
    pass

d = D()
d.func()# D、B、C、A

# java不能存在这种问题，cpp使用类名限定解决？，py使用就近原则