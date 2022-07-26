# python继承

# 抽象与继承、封装与多态


class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b

    def func(self):
        print("func")


class C(A, B):
    pass


class D(A):
    def __init__(self, a, d):
        A.__init__(self, a)
        self.d = d


class E(B):
    def __init__(self, b, e):
        super().__init__(b)
        self.e = e

    def func(self):
        print("func")


print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

e = E(1, 2)
e.func()
print(e)
super(E, e).func()  # 好像不会提示
# print(super(E, e).)
