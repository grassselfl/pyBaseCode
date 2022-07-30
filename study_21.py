# 匿名函数
def pow2(n):
    return n ** 2


print(pow2(10))
calc = lambda n: n ** 2
print(calc(10))

add = lambda x, y: x + y

l = [-2, 4, -9, 4, 7, 8]
print(max(l, key=lambda n: n * n))

# 内置函数带key
# max、min、filter、map、sorted


# 推导式、生成器、装饰器
