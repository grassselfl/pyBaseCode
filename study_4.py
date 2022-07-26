# 运算符

# 算术运算符
# +
# -
# *
# /
# **
# //

# 赋值运算符
# =
# +=
# -=
# /=
# *=
# **=
# //=


# 关系运算符
# >
# =
# <
# >=
# <=
# !=


# 逻辑运算符，返回表达式的值
# and
# or
# not
# ()>not>and>or

print(1 and 2)  # 2
print(0 and 2)  # 0
print(2 and 0)  # 0

print(1 or 2)  # 1
print(0 or 2)  # 2
print(2 or 0)  # 2

print(not 1)  # False
print(not 2)  # False
print(not 0)  # True
print(not '0')
# 根据表达式结果判定，如果为0，返回可以确定整个表达式真假的表达式的值

print("10" and 0)
print(0 or "10")
print(0 or True)

print(1 and 2 > 1)
print(2 > 1 and 1)
print(2 > 1 or 1)

print("" and 1)  # 特别注意
# 根据逻辑运算符返回表达式的值，如果使用关系运算符，则正好返回bool


# 成员操作符
# in
