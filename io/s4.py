"""
文件操作
"""

f = open('../file.txt', mode='r', encoding='utf-8')  # 以什么方式编码，就以什么方式打开
data = f.read()
print(data)
f.close()

# r，只读
# rb，二进制只读
# w，无该文件会新建,有该文件
# wb
# a 追加写入
# ab
f = open('../file.txt', mode='r', encoding='utf-8')
data = f.write("不念过往,不畏将来")
print(data)
f.close()

# f.seek(0)

# 读模式
# r
# 打开不存在的文件会报错、不能写；如不指定模式则默认是r
# 写模式
# w
# 打开不存在的文件会, 会新建一个文件；打开存在的文件会先清空后覆盖原有文件；不能读
# 追加模式
# a
# 打开不存在的文件会, 会新建一个文件；不能读
#
# 读写模式
# r + 能写，打开不存在的文件会报错,r+b
# 写读模式
# w + 能读，但是读不到内容，因为w先把文件内容清空了,w+b
# 追加读模式
# a + 能读，但读不到内容，因为文件指针默认在最后一行，可用seek移动文件指针位置,a+b


# f.read(3)  # 按照字符
# f.seek(3)  # 按照字节,具体看编码方式
# f.readline()
# f.readlines() # list
f.readable()
f.tell()  # 光标位置
# f.truncate(3)  # 注意

with open('../file.txt', mode='r', encoding='utf-8') as obj:
    print(obj.read())
# r+ w+区别