# 元组
t = (1, 2, 3, 'tuple', [1, 'tuple'])
t[4][0]=2
print(t)


# 元组不可修改，仅限于元组内的值不允许修改，元组内的列表通常可以更改


# 列表
l = [1, 2, 3]
# 索引切片同字符串，增删改查
l.append('4')
l.pop(-1)
l.extend((1, 2, 3))
l.remove('1')
l.clear()

l[0:1] = '123457890'  # 根据切片修改，有多少改多少
print(len(l))
l.sort(reverse=True)
l.reverse()
# 字典
d = {'1': 1, '2': 2, '3': 3}

# 集合
s = {1, 2, 3}
# frozenset
