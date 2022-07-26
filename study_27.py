# 序列化
# json
import json

#


d = {1: "a", 2: "b"}
print(d, type(d))
d_dump = json.dumps(d)
print(d_dump, type(d_dump))
d_rd = json.loads(d_dump)
print(d_rd, type(d_rd))

d = {1: "细节", 2: "b"}
f = open("dump.txt", "w", encoding="utf-8")
json.dump(d, f, ensure_ascii=False)
f.close()

f = open("dump.txt", encoding="utf-8")
d = json.load(f)
f.close()
print(d, type(d))

# 小例子
l = [{'a': 1}, {'b': 2}, {'c': 3}]
f = open("file", "w")
for d in l:
    print(d, type(d))
    str_dict = json.dumps(d)
    f.write(str_dict + "\n")
f.close()

f = open("file")
l = []
for line in f:
    d = json.loads(line.strip())
    l.append(d)
f.close()
print(l)




# 二进制存储，不支持分词load
import pickle

d = {1: "a", 2: "b"}
print(d, type(d))
d_dump = pickle.dumps(d)
print(d_dump, type(d_dump))
d_rd = pickle.loads(d_dump)
print(d_rd, type(d_rd))

d = {1: "细节", 2: "b"}
f = open("dump.txt", "wb")
pickle.dump(d, f)
f.close()

f = open("dump.txt", "rb")
d = pickle.load(f)
f.close()
print(d, type(d))


import shelve
f = shelve.open('open_file')
f['key'] = {'int':11,'float':1.2,'string':'ssd'}
f.close()

f = shelve.open('open_file',flag='r')
e = f['key']
f.close()
print(e) 