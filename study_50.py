class A:
    a = 1

    def change1(self, a):  # 显然不合理
        A.a = a

    def change2(a):  # 可行，但不规范
        A.a = a

    @classmethod
    def change3(cls, a):  # cla表示一个类对象，是类对象的默认参数
        cls.a = a

    @staticmethod
    def change4(a):
        A.a = a

    @staticmethod
    def change5(a):
        return a


A.change3(4)
print(A.change5(5))

# python中类方法和静态方法不一样

# 同样也可以用对象调用类方法和静态方法
o = A()
o.change3(3)
o.change4(4)
