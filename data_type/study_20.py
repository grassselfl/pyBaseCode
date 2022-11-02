# python关键字
# global a
# nonlocal b

# 内置函数

# 数据类型

print(bytes())
print(bool())
print(int())
print(float())
print(complex())

print(list())
print(tuple())
print(str())
print(dict())
print(set())

len([])
range(10)
slice(1, 6, 19)
sorted([])
reversed([])
# map(function, iterable)
enumerate([])
frozenset([])
zip([], [])
all([])
any([])
l = 100
hash(l)
id(l)


def func(i):  # 判断奇数
    return i % 2 == 1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = filter(func, lst)  # l1是迭代器
print(l1)  # <filter object at 0x000001CE3CA98AC8>
print(list(l1))  # [1, 3, 5, 7, 9]

# 进制转换
print(bin(10))  # 二进制:0b1010
print(hex(10))  # 十六进制:0xa
print(oct(10))  # 八进制:0o12

# 数学
print(abs(-2))  # 绝对值:2
print(divmod(20, 3))  # 求商和余数:(6,2)
print(round(4.50), round(4.51))  # 五舍六入:4,5
print(pow(10, 2, 3))  # 如果给了第三个参数. 表示最后取余:1
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))  # 求和:65
print(min(5, 3, 9, 12, 7, 2, -10, key=abs))  # 求最小值:2
print(max(7, 3, 15, 9, 4, -13, key=abs))  # 求最大值:15

# 作用域相关
print(locals())
print(globals())

# IO
print("IO")
# input()

# 文件操作
# open("")

# 模块
sys = __import__('sys')  # 动态导入模块import
print(sys.path)

# 帮助
# help(str)
print(dir(int))

# 对象
a = 1
print(callable(a))
# callable() : 用于检查一个对象是否是可调用的. 如果返回True, object有可能调用失败, 但如果返回False. 那调用绝对不会成功

# 动态代码、compile()、exec()、eval()
code = """
for i in range(3):
    print(i)
"""
com = compile(code, "", "exec")  # 一次编译，多次运行，直接执行默认进行编译，多次执行就进行多次编译，compile可以减少编译次数
exec(com)

exec("""
c = 10
def func():
    print("动态代码")
""")
func()  # 我是周杰伦
print(c)

# 编码相关
print(ord('a'))
print(ord('宗'))
print(chr(65))
print(chr(19999))
print(ascii('\n'), ascii('发'))  # 是ascii码中的返回该值 不是就返回u


class B:
    def __init__(self):
        pass


# str()将对象转换为适用于人阅读的形式，repr()将对象转换为供解释器读取的形式
print(str(B()))
print(repr(B()))  # repr() 函数将对象转化为供解释器读取的形式。
print(repr("12\t12\n12"))
print("12\t12\n12")

g = (i for i in range(10))
next(g)
iter(g)

f = open('../file1.txt', 'w')
print("123", end="", file=f)
f.close()

l1 = [1, 2, 3, 1, 2]
l2 = ['a', 'b', 'c', 'a']
for i in zip(l1, l2):
    print(i)

l = [1, 2, 3, 4]


def pow2(x):
    return x * x


for i in map(pow2, l):
    print(i)


def comp(x):
    return x


print(sorted([1, 3, 2, 4], key=comp))  # 会生成副本
