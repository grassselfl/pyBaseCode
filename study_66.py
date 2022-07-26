from multiprocessing import Process


def func(i):
    print(i * '*')


if __name__ == "__main__":
    p_list = []
    for i in range(1, 11):
        p = Process(target=func, args=(i,))  # daemon守护进程，python中主进程需要等待子进程结束后再结束
        p_list.append(p)
        p.start()
        # p.terminate() #结束子进程
    [p.join() for p in p_list]
    print("over")
