"""
数据类型
数字类型：bool、int、flout（无double）、complex 不可变
组合类型：
序列：
     字符串   有序   不可变     可重复
     元组     有序  不可变     可重复
     列表     有序  可变       可重复
集合          无序  可变       不可重复
字典          无序  可变       不可重复（指key）

三个可变，三个不可变
"""

"""
字符串
"""
s = "  davis JoNes_aBc  "
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.startswith("Da"))
print(s.endswith("Bc"))
print(s.count("a"))
print(s.find("a"))  # 找不到返回-1
print(s.find("aB"))
print(s.replace('davis', 'DAVIS'))
print(s.index("JoNes"))  # 找不到抛出异常
print(s.join("      "))
print(s.strip())
print(s.strip(" "))
print(s.rstrip(" "))
print(s.lstrip(" "))
print(s.split())
print(s.split(" "))
print(s.split("a"))

s = '我是{}，今年{}岁，学习进度为{}%'.format("davis", 18, 3)
print(s)

s = '我是{}，今年{}岁，学习进度为{}%'.format("davis", 18, 3)
print(s)

s = '我是{2}，今年{1}岁，学习进度为{1}%'.format("davis", 18, 3)
print(s)

s = '我是{name}，今年{age}岁，学习进度为{process}%'.format(name="davis", age=18, process=3)
print(s)

print(s[3])
print(s[2:6])
print(s[::])
print(s[::-1])
# 字符串索引切片

# 字符串与列表相互转换，join、split
print(' '.join(['1', '2', '3', '4', '5']))

# 字符串%格式化输出，仅有%s、%d
name = input("请输入姓名：")
age = input("请输入年龄：")
process = input("请输入学习进度：")
msg = "我是%s，今年%s岁，学习进度为%s%%" % (name, age, process)  # 前面%为转义标识，即%%输出%
print(msg)

"""
元组
"""
t = (1, 2, 3, 'tuple', [1, 'tuple'])
t[4][0] = 2
print(t)

"""
列表
"""
l = [1, 2, 3]
# 索引切片同字符串，增删改查
l.append('4')
l.pop(-1)
l.extend((1, 2, 3))
l.remove(1)
l.clear()

l[0:1] = '123457890'  # 根据切片修改，有多少改多少
print(len(l))
l.sort(reverse=True)
l.reverse()

"""
集合
"""
s = {1, 2, 3}
# frozenset

"""
字典
"""
d = {'1': 1, '2': 2, '3': 3}
a = [1]
d = {a: 12}
a = 2
print(d)

# 字典的key需要是基本数据类型？
# 增
d[2] = 2
# 删
d.keys()
d.values()
d.copy()
d.clear()
d.get(1, 'NULL')
k, v = d.items()
d.setdefault(1, 12)  # 有键值对不更改，无则使用值更改
d.pop(100, '123')
d.popitem()  # 随机删除
d2 = {1: 2, 4: 4}

d.update(d2)  # 字典更新

a, b = 1, 2
b, a = a, b

# builtins


# 正则表达式
# python内置模块

# re
import re

pattern = ""
str_ = ""

result = re.search(pattern, str_)
print(result.group() if result else None)

result = re.match(pattern, str_)  # 必须从头匹配
print(result.group() if result else None)

result = re.findall(pattern, str_)
print(result)

result = re.finditer(pattern, str_)  # 找的内容比较多的时候
for i in result:
    print(i.group() if i else None)

result = re.split(pattern, str_)

result = re.sub(pattern, 'O', str_)
print(result)
obj = re.compile(pattern)
result = obj.search(str_)
print(result)

pattern = "/\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b/g"
str_ = "abcd test1@jld.com 1234 test2@jld.com"
result = re.search(pattern, str_)
print("---", )
print(result.group() if result else None)

# () 表示捕获分组，() 会把每个分组里的匹配的值保存起来，python分组优先加?
