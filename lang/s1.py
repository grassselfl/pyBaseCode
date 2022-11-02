"""
命名空间与作用域
"""

# 命名空间
# 作用域
# 内置命名空间
# 全局命名空间
# 局部命名空间
# 全局作用域
# 局部作用域: 函数作用域
# 全局命名空间(包含内置builtins)\局部命名空间
a = 1


def input():
    global a  # 全局变量
    a = 9
    print("123")


def laa():
    global a

    def input():
        nonlocal a  # 非本地变量(外面直接是模块是不行的)
        a += 9
        print("123")
