class A:
    __key = 1

class B(A):
    print(A._A__key)
    print(A.__key)

# 1.可以执行语句，也许与装饰器有点关系，就抽象方法那个

# 2.因为转换机制的原因，不能直接访问该属性