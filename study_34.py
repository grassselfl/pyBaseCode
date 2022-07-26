# python类中的属性与方法

class Person:
    uuid = 1
    s = [1, 2, 3]

    def func(self): pass


a = Person()
b = Person()

print(id(a.uuid), id(b.uuid))


def func(): pass


print(func)
print(Person.func)
print(a.func)  # 绑定方法，表示要把对象a的数据传递给func
print(a)
