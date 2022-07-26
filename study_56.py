# __getitem__ __setitem__ __delitem__



class Foo:
    def __init__(self, name):
        self.name = name

    # python相比于java在get set上简化了许多
    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("del obj[key]时执行")
        self.__dict__.pop(key)

    def __delattr__(self, item):
        print("del obj.key时执行")
        self.__dict__.pop(item)


f = Foo("张三")

f.age = 18

del f.age
del f['name']