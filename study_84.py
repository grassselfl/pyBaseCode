# 定时器

import time
from threading import Timer


def func():
    print("时间同步")


while True:
    t = Timer(1, func)
    t.start()
    time.sleep(1)

