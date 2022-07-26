# ASCII 英文一个字节
# UTF-8 英文一个字节，中文三个字节
# Unicode 中英文四个字节
# GBK2312 英文一个字节 中文两个字节

# python3 字符串在内存中使用unicode编码
# 表示（存储、传输）

s = 'davis'
s1 = b"davis"
print(s, type(s))
print(s1, type(s1))

s = '欢喜'
# s1 = b"欢喜"#SyntaxError: bytes can only contain ASCII literal characters.
print(s, type(s))
print(s1, type(s1))
