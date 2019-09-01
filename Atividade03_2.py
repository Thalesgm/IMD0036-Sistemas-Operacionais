import threading
import time

#List to store each priority representation as objects of the Priority Class decribed bellw
priorityList = []
#Time Spent Running each thread
scheduledTime = 1
#Total Number of Working Threads
maxWorkers = 3
#highest level of priority for any thread
maxdefaultPriority = 8
#Current Working Thread - Starts at -1 so no thread will run instantly
workCondition = -1 

"""Class to define priority objects, each object will have a default priority and 
an overtime priority which will be updated during execution"""
class Priority:
    defaultPriority = 0
    overtimePriority = 0
    
    def __init__(self, defaultPriority):
        self.defaultPriority = defaultPriority
    
    def getPriority(self):
        realPriority = self.defaultPriority + self.overtimePriority
        return realPriority

#This function fills the priority list using the global variables.
def createPriority(priorityList):
    global maxdefaultPriority
    global maxWorkers
    countPriority = maxdefaultPriority 
    while countPriority > 0:
        countWorkers = maxWorkers
        while countWorkers > 0:
            p = Priority(countPriority)
            priorityList.append(p)
            countWorkers -= 1
        countPriority -= 3

#This function returns the next thread to be run, also updates the overtime priority list to avoid starvation.
def getNextPriority(priorityList):
    highestPriority = priorityList[0].getPriority()
    highestPriorityPos = 0
    i = 1
    while i < len(priorityList):
        if highestPriority < priorityList[i].getPriority():
            highestPriority = priorityList[i].getPriority()
            highestPriorityPos = i
        i += 1
    countUpdate = 0
    while countUpdate < len(priorityList):
        if countUpdate != highestPriorityPos:
            priorityList[countUpdate].overtimePriority += 1
        countUpdate += 1
    return highestPriorityPos

#Work that will be done by each thread
def job(i):
    global workCondition
    while True:
        if workCondition == i:
            print("Thread ", i, " Working")
        else:
            time.sleep(1)
#CPU scheduler, runs the control functions and also alters the variable that alows threads to do their work. 
def cpu(priorityList):
    global workCondition
    global scheduledTime
    while True:
        workCondition = getNextPriority(priorityList)
        print("Currently Executing thread:", workCondition)
        time.sleep(scheduledTime)

createPriority(priorityList)
thread0 = threading.Thread(target=job, args= (0,))
thread1 = threading.Thread(target=job, args= (1,))
thread2 = threading.Thread(target=job, args= (2,))
thread3 = threading.Thread(target=job, args= (3,))
thread4 = threading.Thread(target=job, args= (4,))
thread5 = threading.Thread(target=job, args= (5,))
thread6 = threading.Thread(target=job, args= (6,))
thread7 = threading.Thread(target=job, args= (7,))
thread8 = threading.Thread(target=job, args= (8,))

cpuThread = threading.Thread(target=cpu, args=(priorityList,))
thread0.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()

cpuThread.start()