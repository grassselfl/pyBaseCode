"""
多进程
Manager
"""

from multiprocessing import Manager, Process

# Manager中一些数据类型是进程不安全的
def main(dic):
    dic['count'] -=1
    print(dic)

if __name__ == "__main__":
    m = Manager()
    dic = m.dict({'count':100})
    p = Process(target=main,args=(dic,))
    p.start()
    p.join()
    print("主进程",dic)




# 进程通信，IPC