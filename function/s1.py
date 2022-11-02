"""
函数
"""


# 函数的参数：位置参数（基本参数）、默认参数、可变参数、关键字参数和命名关键字参数
# 解释器处理顺序？ 基本参数、默认参数、可变参数、命名关键字参数和关键字参数
# （基本）可变参数、命名关键字参数、（命名）关键字（可变）参数


# 默认参数，要放在最左边

def calc(i=0):
    return i


# 可变参数，可变参数将以元组方式传递

def sum1(a, b, *args):  # 默认为元组,无法接受关键字传参
    print(a, b)
    res = 0
    for i in args:
        res += i
    return res


# 函数参数的自动装包与拆包
# *args会把多余参数打包
# 打包之后的类型为元组
# 即元组与列表的打印拆包中总结，只能默认拆包元组，如果是列表就先转换成元组在拆包
a = [1, 2, 3, 4, 5]
a1, a2, a3, a4, a5 = a
print(sum1(*a))


# 关键字参数，关键字参数将以字典方式传递
def sum2(**kwargs):
    print(kwargs, type(kwargs))


# 默认参数为可变类型数据容器,会共享
# 不要使用可变类型的数据容器作为默认参数（包括列表，字典），但是可以作为位置参数使用


print(print)  # 函数的内存地址

# locals 与 globals
print(globals())  # 无fun,因为一行一行执行


def fun():
    x, y = 1, 2
    print(locals())


print(locals())
fun()


# 匿名函数
# 匿名函数
def pow2(n):
    return n ** 2


print(pow2(10))
calc = lambda n: n ** 2
print(calc(10))

add = lambda x, y: x + y

l = [-2, 4, -9, 4, 7, 8]
print(max(l, key=lambda n: n * n))

# 内置函数带key
# max、min、filter、map、sorted
