# 深入分析study_40问题

class A:
    def func(self): print("A")


class B:
    def func(self): print("B")


class C(A):
    pass
    # def func(self): print("C")


class D(B):
    def func(self): print("D")

class E(C,D):
    pass

e = E()
e.func()  # D、B、C、A
print(E.__mro__)
# java不能存在这种问题，cpp使用类名限定解决？，py使用就近原则（直观上），广度优先（实质上）
