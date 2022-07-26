# 反射进阶
# setattr、getattr、hasattr、delattr
s = 10
class A:
    a = 1
    def func(self):
        print(1)

    @classmethod
    def func1(cls):
        print(2)

    @staticmethod
    def func2():
        print(3)
print(A.__dict__)

# 下述方式很相似于反射
print(A.__dict__['a'])
A.__dict__['func'](A())

# 这里似乎不能直接用字典调用该方法，因为使用了装饰器？？

# A.__dict__['func1'](A)#TypeError: 'classmethod' object is not callable

# A.__dict__['func2']()#TypeError: 'staticmethod' object is not callable

# python中反射分为对对象的反射和对类的反射，两者是不一样的，对类可以反射类属性、静态方法、类方法，对对象可以反射，对象属性、对象方法