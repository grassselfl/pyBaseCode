import time
from threading import Thread


class ThreadDemo(Thread):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def run(self) -> None:
        time.sleep(1)
        print(self.args)


t = ThreadDemo((1,2))
t.start()
