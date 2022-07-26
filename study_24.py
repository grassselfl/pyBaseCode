import time

# 时间戳
print(time.time())
print(time.time_ns())  # 纳秒

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%H:%S"))

# 结构化时间
print(time.struct_time.tm_min)


print(time.localtime())
print(time.gmtime())
time.sleep(1)


print(time.strptime('2000-12.31','%Y-%m.%d'))

print(time.asctime())
print(time.ctime())