"""
greenlet
"""
from greenlet import greenlet


def eat():
    while True:
        print("eat")
        gl2.switch()


def drink():
    while True:
        print("drink")
        gl1.switch()


if __name__ == "__main__":
    gl1 = greenlet(run=eat)
    gl2 = greenlet(run=drink)
    gl1.switch()  # 没有运行会先运行run
