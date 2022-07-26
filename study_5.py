# 字符串操作
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
