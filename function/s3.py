# 装饰器标准模板
# 装饰器函数\装饰器类,以函数作为装饰器\以类作为装饰器
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
