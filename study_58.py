class A:
    def __init__(self, a):
        self.a = a
        print("初始化")

    def __new__(cls, *args, **kwargs):
        print("构造函数")
        return object.__new__(cls)


o = A(1)
print(o.a)

# 可以和study_57相比较


# __new__
# __init__
# __init__中self.a= 1调用__setitem__
# 完成了