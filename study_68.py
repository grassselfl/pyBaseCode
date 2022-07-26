from multiprocessing import Semaphore

sem = Semaphore(4)
sem.acquire()
sem.acquire()
sem.acquire()
sem.acquire()
sem.acquire()