import cProfile


def fun():
    fun1()


def fun1():
    for i in range(10):
        fun2()


def fun2():
    for i in range(4):
        fun3()
    fun4()


def fun3():
    import time
    time.sleep(0.1)


def fun4():
    import time
    time.sleep(0.01)


if __name__ == "__main__":
    cProfile.run('fun()')
