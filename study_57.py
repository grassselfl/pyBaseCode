# 更正 __init__为初始化方法，并非构造方法，构造方法为__new__，析构方法确实是__del__

class A:
    def __init__(self,a):
        self.a = a
        print("初始化")
    def __new__(cls, *args, **kwargs):
        print("构造函数")


o = A(1)

print(o.a)