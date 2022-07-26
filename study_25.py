# random
import random

print(random.Random())
print(random.uniform(1, 10))
random.randint(1, 10)  # [1,10]
random.randrange(1, 10, 2)  # [1,10)

l = [1, '2', [3]]
print(random.choice(l))
print(random.sample(l, 2))
random.shuffle(l)
print(l)

# 应用，生成随机验证码
