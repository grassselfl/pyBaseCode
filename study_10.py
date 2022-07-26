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
d.get(1,'NULL')
k, v = d.items()
d.setdefault(1, 12)  # 有键值对不更改，无则使用值更改
d.pop(100, '123')
d.popitem()  # 随机删除
d2 = {1: 2, 4: 4}

d.update(d2)  # 字典更新

a, b = 1, 2
b, a = a, b

# builtins
