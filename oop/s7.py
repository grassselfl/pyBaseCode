"""
反射
"""

class A:
    a = 1



    @classmethod
    def func1(cls):
        print(1)

    @staticmethod
    def func2(a):
        print(a)


    def func3(self):
        print(3)

a = getattr(A, 'a')
print(a)
delattr(A, 'a')
print(hasattr(A, 'a'))

print(hasattr(A, 'func1'))
method = getattr(A, 'func1')
method()

print(hasattr(A, 'func2'))
method = getattr(A, 'func2')
method(2)

# 上述是类级别的反射，可以用类反射到一般方法，但是逃不过self参数

# 下面是对象级别的反射

a = A()
print(hasattr(a, 'func3'))
method = getattr(a, 'func3')
method()# 此时才可以忽略参数self


# 通过反射
# 对象名 获取对象属性 和 普通方法
# 类名 获取静态属性 和 类方法 和 静态方法