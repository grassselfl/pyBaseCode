# 生成器
# generator
# 生成器函数 生成器表达式

# 含有yield关键字的函数为生成器函数
# yield不可与return共用

# 生成器函数
def generator_func():
    print("generator")
    yield 'a'


result = generator_func()
print(result)

print(dir(result))
print(result.__next__())


def generator_func2():
    print("generator1")
    yield 'a'
    print("generator2")
    yield 'b'


result = generator_func2()

print(result.__next__())
print(result.__next__())
# print(result.__next__())  # StopIteration

l = [1, 2, 3]

for i in l:
    print(i)

for i in l:
    print(i)

# 两个迭代器

# 从生成器取值方法，利用迭代器next或者for，转换为一般可迭代数据类型，如列表进行使用
