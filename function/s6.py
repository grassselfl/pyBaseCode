"""
多层装饰器执行顺序
"""


# 多个修饰器修饰函数
def wrapper1(func):
    def inner1():
        print("inner1 before")
        func()
        print("inner1 after")

    return inner1


def wrapper2(func):
    def inner2():
        print("inner2 before")
        func()
        print("inner2 after")

    return inner2


def wrapper3(func):
    def inner3():
        print("inner3 before")
        func()
        print("inner3 after")

    return inner3


@wrapper1
@wrapper2
@wrapper3
def do():
    print("fun")


do()
