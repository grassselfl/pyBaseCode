o = object()

print(repr(1))  # 实质上在调用该方法的对应双下方法
print(repr('1'))


# 验证

class A:

    def __init__(self,a):
        pass

    def __str__(self):
        return "A is str"

    def __call__(self, *args, **kwargs):
        print("is __call__")

print(str(A(1)))

print(A(1), "1")  # 打印对象本身都是打印__str__的返回值，该返回值必然是一个字符串，所以print本质上是打印的字符串

print(o.__str__())
print(o.__repr__())

# object类方法与builtins方法


# 格式化输出本质是调用的双下方法
# s% str() __str__
# r% repr() __repr__

# 关于print(obj)如果没有__str__，则使用__repr__，没有就找父类，直至object

# str()如果作用对象无__str__实现，就使用__repr__，若只能实现一个，就是先repr，因为str()可以用，repr也可以用

# __len__ len()同理

# len(A())#可以验证

# del执行的是__del__，析构函数？？？，__init__构造函数，所以程序结束时会自动调用析构函数


# 上述就体现出面向过程和面向对象结合的玄妙之处了

a = A(1)
a()

A(0)()#将对象地址作为函数地址使用的一个范例！！？？？？？

# type()
# def __call__(self, *args, **kwargs):  # real signature unknown
#     """ Call self as a function. """
#     pass
# type类与object类   Class类与Object类