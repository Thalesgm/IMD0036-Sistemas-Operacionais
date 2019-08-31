import threading
import time

maxWorkers = 3 #Total Number of Working Threads
workCondition = -1 #Current Working Thread - Starts at -1 so no thread will run instantly
#Work that will be done by each thread
def job(i):
    global workCondition
    while True:
        if workCondition == i:
            print("Thread ", i, " Working")
        else:
            time.sleep(1)

#CPU Scheduler Runs until last process has been executed, then returns to the first one.
def cpu():
    global maxWorkers
    global workCondition
    while True:
        if workCondition < maxWorkers:
            workCondition += 1
            print("Currently Executing thread: ", workCondition)
            time.sleep(1)
        else:
            workCondition = 0
            print("Currently Executing thread: ", workCondition)
            time.sleep(1)

thread0 = threading. Thread(target=job, args= (0,))
thread1 = threading. Thread(target=job, args= (1,))
thread2 = threading. Thread(target=job, args= (2,))
thread3 = threading. Thread(target=job, args= (3,))
threadCPU = threading. Thread(target=cpu)

thread0.start()
thread1.start()
thread2.start()
thread3.start()
threadCPU.start()