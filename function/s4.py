"""
debug的一个例子

无参装饰器
"""


def debug(func):
    def wrapper(*args):
        print("[DEBUG]: function {}".format(func.__name__))
        return func(*args)

    return wrapper


@debug
def add(a, b):
    return a + b

# add_ = debug(add)？？？
add(1, 2)
