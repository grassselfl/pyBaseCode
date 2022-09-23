print(bool("123") ^ bool(""))
print(not [])
# python判空一个not即可

def h(i : int):
    return i


print(h(2.0))

import math

def circumference(radius: float) -> float:
    return 2 * math.pi * radius
print(circumference.__annotations__)

_i = 1
__i = 2

def _get():
    print("_get")

def __get():
    print("_get")