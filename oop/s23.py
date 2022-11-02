"""
__eq__
__hash__
"""

class A(object):
    def __init__(self, a):
        self.a = a


o1 = A(1)
o2 = A(1)

print(o1 == o2)

print(o1 is o2)

print(o1.__eq__(o2))


class B:
    def __init__(self, b):
        self.b = b

    def __eq__(self, other):
        return self.b == other.b


b1 = B(1)
b2 = B(1)

print(b1 == b2)

print(b1 is b2)

print(b1.__eq__(b2)) ## ==与__eq__是一致的


# hash() __hash__

class C:
    def __init__(self, c):
        self.c = c

    def __eq__(self, other):
        return self.c == other.c

    def __hash__(self):
        return self.c.__hash__()

c1 = C(1)
c2 = C(1)

print(c1 == c2)

print(c1 is c2)

print(c1.__eq__(c2))