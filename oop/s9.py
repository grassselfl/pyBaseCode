"""
实例化链
"""
class A:
    def __init__(self):
        print("A __init__")
        self.func()
    def func(self):
        print("A func")

class B(A):
    def func(self):
        print("B func")

b= B() # 显然使用继承的__init__方法，调用的自己的func

print(b.__dict__)
print(B.__dict__)
print(A.__dict__)