import threading
import time

#Time Spent Running each thread
scheduledTime = 2
#Total Number of Working Threads
maxWorkers = 9
#highest level of priority for any thread
maxdefaultPriority = 3 
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

#Work that will be done by each thread
def job(i):
    global workCondition
    while True:
        if workCondition == i:
            print("Thread ", i, " Working")
        else:
            time.sleep(1)

p = Priority(4)
print(p.getPriority())