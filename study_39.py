class A:
    pass
    # def func(self): print("A")


class B:
    def func(self): print("B")


class C:
    def func(self): print("C")

class D(A,B,C):
    pass

d = D()
d.func()

# java不能存在这种问题，cpp使用类名限定解决？，py单继承下使用就近原则