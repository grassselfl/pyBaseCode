# py继承中的一个十分开放的问题

class A:
    def __init__(self, a):
        self.a = a
    def func(self):
        print("A")

class B(A):
    def __init__(self,b):
        self.b = b

b = B(2)
b.func()

# 上述程序完全没有问题，尽管没有初始化b.a，也能调用A的方法func，说明继承关系是真的，但却可以没有实例化链，这一点说明了py十分开放


class C:
    def __init__(self, c):
        self.c = c

class D(C):
    def __init__(self,c,d):
        super().__init__(c)
        self.d = d


d = D(1,2)

# 实例化链