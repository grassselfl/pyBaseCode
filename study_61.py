# hashlib

# MD5 Message Digest 5 信息摘要
# SHA Security Hash Algorithm 安全散列算法


import hashlib

md5 = hashlib.md5()
md5.update(b"Hello World!")
print(md5.digest())
print(md5.hexdigest())

# 静态盐
md5 = hashlib.md5(bytes('盐值加密', encoding='utf8'))
md5.update(b"Hello World!")
print(md5.hexdigest())

# 动态盐
# 比如用户名密码，使用用户名一部分加某些字符作为盐，可以基本做到每个用户的盐不一样

md5 = hashlib.md5(bytes('盐值加密', encoding='utf8'))
md5.update(b"Hello ")  # 可以分次加密
md5.update(b"World!")
print(md5.hexdigest())
