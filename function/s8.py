"""
不给生成器传参
"""

# 生成器，generator
# 生成器函数 生成器表达式

# 含有yield关键字的函数为生成器函数
# yield不可与return共用


def generator_func2():
    print("generator1")
    yield 'a'
    print("generator2")
    yield 'b'


result = generator_func2()
print(result)

print(dir(result))
print(result.__next__())
print(result.__next__())
# print(result.__next__())  # StopIteration

# 生成器只能遍历一遍元素，获取完毕之后必须重新new
# 而对于列表来说，可以使用for i in l: print(i)遍历多次，但是生成器会报异常
