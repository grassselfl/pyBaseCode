from multiprocessing import Process


class ProcessDemo(Process):
    def run(self) -> None:
        print(12345)


if __name__ == "__main__":  # 为什么python创建进程需要使用主函数，否则就报错
    p = ProcessDemo()
    p.start()
