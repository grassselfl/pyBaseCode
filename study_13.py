# Python 会自动将多个返回值封装成元组

def calc(i=0):
    return i


def sum1(*args):  # 默认为元组,无法接受关键字传参
    res = 0
    for i in args:
        res += i
    return res


def sum2(**kwargs):
    '''
    函数注释是三个单引号
    :param kwargs:
    :return:
    '''
    print(kwargs, type(kwargs))


a = [1, 2, 3, 4, 5]
a1, a2, a3, a4, a5 = a
print(sum1(*a))


# 位置参数必须在关键字参数之前

# 默认参数为可变类型数据容器,会共享
# 不要使用可变类型的数据容器作为默认参数（包括列表，字典），但是可以作为位置参数使用


# 全局明明空间(包含内置builtins)\局部命名空间

def input():
    global a  # 全局变量
    a = 9
    print("123")


input()
print(input)  # 函数的内存地址

# 命名空间
a, b = 1, 2

print(globals())  # 无fun,因为一行一行执行


def fun():
    x, y = 1, 2
    print(locals())


print(locals())
fun()

# scope问题
for i in range(10):
    print(i)
print(i)  #


# 命名空间
# 作用域
# 内置命名空间
# 全局命名空间
# 局部命名空间
# 全局作用域
# 局部作用域: 函数作用域

# 函数嵌套定义
def outer():
    print("outer")

    def inner():
        print("inner")

    inner()


outer()

# 报错从下往上找


a = 1


def ff():
    a = 2

    def fff():
        global a
        a = 3
        print(a)

    fff()
    print(a)


ff()
print(a)


# 函数名就是内存地址,
def f1():
    print(100)


def f2(f):
    f()
    return f


f2(f1)


# 函数名可以作为一般值使用, 函数参数\函数返回值\容器元素


# 闭包函数,闭包函数通过将函数名作为返回值使得不释放局部变量引用而保留局部变量
def nth_power(n):
    def power(base):
        return base ** n

    return power


power = nth_power(3)
print(power.__closure__)
print(power(2))
