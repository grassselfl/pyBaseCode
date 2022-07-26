def debug(func):
    def wrapper(*args):
        print("[DEBUG]: function {}".format(func.__name__))
        return func(*args)

    return wrapper


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


# add_ = debug(add)
print(add(1, 2, 3, 4))


# 装饰器函数\装饰器类,以函数作为装饰器\以类作为装饰器,装饰函数


def wrapper():
    def outer(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res

        return inner

    return outer


@wrapper()
def user():
    print("use")


user()
