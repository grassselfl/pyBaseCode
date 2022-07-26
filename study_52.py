class A:
    pass


class B(A):
    pass


a = A()

print(isinstance(a, A))  # 是否对象
print(issubclass(B, A))  # 是否子类

# 那么有一个mro问题，在study_42验证，并没有出现该问题，mro不愧是方法解析顺序，那么super到底是什么？
#也许issubclass仅仅是单线分析