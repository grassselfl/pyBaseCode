"""
装饰器的一个例子
有参装饰器
"""


def logging(level):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):  # 本质调用,所以参数在这
            # print(args,kwargs)
            print("[{}]: function {}".format(level, func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return outer_wrapper  # 决定


# @logging(level="DEBUG")相当于先调用函数outer_wrapper=logging(level="DEBUG")得到@outer_wrapper
# @outer_wrapper相当于inner_wrapper=outer_wrapper(func)
# 最终执行inner_wrapper
@logging(level="DEBUG")
def add(a, b, *args):
    res = a + b
    for i in args:
        res += i
    return res


print(add(1, 2, 3, 4))
