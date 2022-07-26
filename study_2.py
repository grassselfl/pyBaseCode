# 用户交互
id = input('请输入ID：')
print(id, type(id))

# 流程控制

# 条件判断允许值判断,非零真，零为假
count = 10
while count:
    count -= 1
    print(count)
    # break
    # continue
else:
    print("循环正常执行完毕，没有被break打断")


for i in range(10):
    print(i)



# 条件语句
flag = 1
if flag == 1:
    print("我是一")
elif flag == 2:
    print("我是二")
else:
    print("我是三")
