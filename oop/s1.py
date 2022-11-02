"""
类和对象
函数和变量
方法与属性

"""

class Person:
    uuid = 1
    def __init__(self, name, age, sex):
        print(self.__dict__)
        self.name = name
        self.age = age
        self.sex = sex

    def walk(self, n):
        print(self.name + "走路" + str(n) + "步")

    def run(s):
        print(str(s) + "跑路")


p = Person("张三", 18, "男")
print(p.__dict__)
print(p.__class__)
print(object.__class__)
print(Person.__dict__)
Person.walk(p, 5)  # 关注过程
p.walk(5)  # 关注对象

Person.run("p")
p.run()



# python实例化，会创建self以调用__init__方法

p.__dict__['name'] = 'zhangsan'
print(p.__dict__['name'])
Person.uuid=2
print(Person.uuid)

# 对象可以通过__dict__进行更改，但是类不能通过__dict__进行更改，都可以通过.进行访问

# 类有自己的命名空间、对象有自己的命名空间