class A:
    __uuid = 1
    def __init__(self, a, a1):
        self.a = a
        self.__a1 = a1

    def get_a1(self):
        print(self.__dict__)
        self.__func()
        return self.__a1

    def __func(self):
        print("私有方法__func")

o = A(1, 2)
print(o.a)
print(o._A__a1)
print(o.get_a1())
o.__a2 = 3
print(o.__a2)
print(o.__dict__)  # _A转换只在内部进行。不能直接调用是因为这个自动转换
print(A.__dict__)
o._A__func()


# python类的访问权限控制，python只分为public和private，用__进行区分
# 类静态属性
# 类属性
# 类方法

# _类名__名字
# 鸭子类型