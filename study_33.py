# python机制下类变量的特殊点
class Person:
    uuid = 1
    s = [1, 2, 3]

    def __init__(self):
        pass


a = Person()
b = Person()
print(a.uuid, b.uuid, Person.uuid)

Person.uuid = 2
print(a.uuid, b.uuid, Person.uuid)

a.uuid = 3  # 此时py会在对象中创建新的属性uuid
b.uuid = 4  # 此时py会在对象中创建新的属性uuid
print(a.uuid, b.uuid, Person.uuid)

del a.uuid, b.uuid  # 除非删除对象中的uuid
print(a.uuid, b.uuid, Person.uuid)
# 也正是由于这种原因有时候对象会偷偷多出来许多类中不曾有的属性


# 指针
a.s[0:1] = '1'
print(Person.s)
