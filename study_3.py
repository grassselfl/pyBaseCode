# %格式化输出，仅有%s、%d
name = input("请输入姓名：")
age = input("请输入年龄：")
process = input("请输入学习进度：")
msg = "我是%s，今年%s岁，学习进度为%s%%" % (name, age, process)  # 前面%为转义标识，即%%输出%
print(msg)
