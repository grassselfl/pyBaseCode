# 深入分析study_41问题

class O:

    def func(self):
        s = "O"
        print(s+"()")
        return s


class A(O):
    def func(self):
        s = "A"
        print(s + "(" + super().func() + ")"+"  （这里好像有问题）")
        return s


class B(O):
    def func(self):
        s = "B"
        print(s + "(" + super().func() + ")")
        return s


class C(A):
    def func(self):
        s = "C"
        print(s + "(" + super().func() + ")")
        return s


class D(B):
    def func(self):
        s = "D"
        print(s + "(" + super().func() + ")")
        return s


class E(C, D):
    def func(self):
        s = "E"
        print(s + "(" + super().func() + ")")
        return s


e = E()
e.func()  # D、B、C、A
print(E.__mro__)
# java不能存在这种问题，cpp使用类名限定解决？，py使用C3算法


# 新式类，旧式类
# C3算法
# py3只有新式类
# py2早期版本是旧式类，后期加入了新式类
# mro 方法解析顺序
# 单继承没有此类问题


# 验证study_52的问题
print(issubclass(A,O))
print(issubclass(A,D))
print(issubclass(E,A))
