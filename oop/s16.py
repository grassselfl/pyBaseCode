"""
抽象基类
抽象方法
python中无接口概念，毕竟支持多继承，但是有抽象类的概念
"""
from abc import abstractmethod, ABCMeta


# Abstract Base Class
class A(metaclass=ABCMeta):
    @abstractmethod
    def func_1(self):
        pass


class A_1(A):
    def func_1(self):
        pass


a = A_1()

# python中抽象类不能实例化，接口类不能实例化

# python中抽象类可以单继承和多继承，但一般根据相关规范编程
