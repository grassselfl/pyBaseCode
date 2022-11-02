"""
元组推导式（生成器表达式）
列表推导式
集合推导式
字典推导式
"""
# 元组推导式（生成器表达式）
g = (i ** 2 for i in range(100) if i % 3 == 0)
print(g, type(g))

# 列表推导式
data = [i ** 2 for i in range(100) if i % 3 == 0]
print(data, type(data))

# 集合推导式，集合推导式结果会去重
data = {i ** 2 for i in range(100) if i % 3 == 0}
print(data, type(data))

# 字典推导式
data = {i: i ** 2 for i in range(100) if i % 3 == 0}
print(data, type(data))


# 许多函数使用迭代器方式访问对象，而生成器是一种迭代器，所以可以直接
print(sum(i ** 2 for i in range(100) if i % 3 == 0))
print(sum([i ** 2 for i in range(100) if i % 3 == 0]))