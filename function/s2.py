"""
函数闭包
"""


def outer():
    print("outer")

    def inner():
        print("inner")

    inner()


outer()

# 报错从下往上找


a = 1


def ff():
    a = 2  # 这是一个局部的a，赋值不影响，但是使用值时会有不同情况

    def fff():
        global a
        a = 3
        print(a)

    fff()
    print(a)


ff()
print(a)


# 函数名可以作为一般值使用, 函数参数\函数返回值\容器元素、函数名就是内存地址,
# 闭包函数,闭包函数通过将函数名作为返回值使得不释放局部变量引用而保留局部变量
def nth_power(n):
    def power(base):
        return base ** n

    return power


power = nth_power(3)
print(power.__closure__)
print(power(2))
