# python内置模块

# re
import re

pattern = ""
str_ = ""

result = re.search(pattern, str_)
print(result.group() if result else None)

result = re.match(pattern, str_)  # 必须从头匹配
print(result.group() if result else None)

result = re.findall(pattern, str_)
print(result)

result = re.finditer(pattern, str_)  # 找的内容比较多的时候
for i in result:
    print(i.group() if i else None)

result = re.split(pattern, str_)

result = re.sub(pattern, 'O', str_)
print(result)
obj = re.compile(pattern)
result = obj.search(str_)
print(result)

pattern = "/\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b/g"
str_ = "abcd test1@jld.com 1234 test2@jld.com"
result = re.search(pattern, str_)
print("---",)
print(result.group() if result else None)

# () 表示捕获分组，() 会把每个分组里的匹配的值保存起来，python分组优先加?