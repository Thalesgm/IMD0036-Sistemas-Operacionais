#Memory Manager Project
#IMD0036 - Sistemas Operacionais
#Eucharlis Vieira Duarte
#Thales Gomes Moreira
import datetime, time

#Class to represent positions on the Bit Map
class MapPosition:
    bitR = 0 #Bit to indicate position is taken
    processID = 0 #Process id to indicate which process is using the position; assumes -1 if empty
    def __init__(self, processID):
        self.bitR = 0
        self.processID = processID
    
    def updatePosition(self, processID):
        self.bitR = 1
        self.processID = processID

#Process as represented on Disc and Memory
class Process:
    processID = 0 #Process reference id
    processSize = 0 #Process total position count on memory capacity
    runTime = 0 #Time used to run the process
    waitTime = 0 #Time process waits on disc
    startingWaitTime = 0 #Reference time value for the last time process was put on disc
    startingRunTime = 0 #Reference time value for the last time process was loaded into memory
    def __init__(self, processID, processSize, runTime, waitTime):
        self.processID = processID
        self.processSize = processSize
        self.runTime = runTime
        self.waitTime = waitTime
        self.startingRunTime = 0
        self.startingWaitTime = time.time()

#Memory Manager Class
#Contains the methods to control the memory usage and display it's current status
class MemManager:
    discSize = 20 #Disc Capacity
    currentMemSize = 0 #Curremt Memory Used
    maxMemSize = 50 #Memory size
    bitMap = [] #BitMap representation
    disc = [] #Disc representation
    memory = [] #Memory representation 

    def __init__(self):
        i = 0
        while i < self.maxMemSize:
            m = MapPosition(0)
            self.bitMap.append(m)
            i += 1

    #Method to print the current Bit Map
    def printBitMap(self):
        i = 0
        print("Current Bit Map Status:")
        while i < len(self.bitMap):
            print("Position: ", i, " Status: ", self.bitMap[i].bitR, " ProcessID: ", self.bitMap[i].processID)
            i += 1
    
    #Method to Print the current disc status
    def printDisc(self):
        i = 0
        print("Current Disc Status:")
        while i < len(self.disc):
            print("Position: ", i, " ProcessID: ", self.disc[i].processID)
            i += 1
    
    #Method to Print the current status of the memory
    def printMem(self):
        i = 0
        print("Current Memory Status")
        while i < len(self.memory):
            print("Position: ", i, " ProcessID: ", self.memory[i].processID)
            i += 1
    
    #Method to add a process to the Bit Map
    def bitMapAdd(self, processID, processSize, fittingPosition):
        i = fittingPosition
        while i < (processSize+fittingPosition):
            self.bitMap[i].bitR = 1
            self.bitMap[i].processID = processID
            i += 1
    
    #Method to remove a process from the Vit Map
    def bitMapRemove(self, processID):
        i = 0
        while i < self.maxMemSize:
            if self.bitMap[i].processID == processID:
                self.bitMap[i].bitR = 0
                self.bitMap[i].processID = -1
            i += 1

    #Finds the first possible fit to the process
    def findBitMapFit(self, processSize):
        i = 0
        fitStart = -1
        fitlegth = 0
        while i < len(self.bitMap):
            if self.bitMap[i].bitR == 0:
                fitStart = i
                fitlegth += 1
                i += 1
                while i < len(self.bitMap) and self.bitMap[i].bitR < 1:
                    fitlegth += 1
                    i += 1
                    if fitlegth == processSize:
                        return fitStart
            fitStart = -1
            fitlegth = 0
            i += 1
        return fitlegth

    #Method to represent the swapping process
    #Also Uses the Bit Map methods
    def swapping(self):
        #Checking for processes past their run time
        if self.currentMemSize > 0:
            i = 0
            currentTime = time.time()
            while i < len(self.memory):
                if (currentTime - self.memory[i].startingRunTime) > self.memory[i].runTime:
                    p = self.memory.pop(i)
                    p.startingWaitTime = time.time()
                    self.bitMapRemove(p.processID)
                    self.disc.append(p)
                    self.currentMemSize -= p.processSize
                i+=1
        #checking for processes past their wait time on disc
        if self.maxMemSize > self.currentMemSize:
            countDisc = 0
            while countDisc < len(self.disc):
                currentTime = time.time()
                if (currentTime - self.disc[countDisc].startingWaitTime) > self.disc[countDisc].waitTime:
                    fit = self.findBitMapFit(self.disc[countDisc].processSize)
                    if fit > -1:
                        p = self.disc.pop(countDisc)
                        p.startingRunTime = time.time()
                        self.bitMapAdd(p.processID, p.processSize, fit)
                        self.currentMemSize += p.processSize
                        self.memory.append(p)
                        countDisc -= 1
                countDisc += 1

m = MemManager()
c = 0
#Inserting the processes on the disc
while c < m.discSize:
    if c < 10:
        p = Process(c, 5, 2, 2)
        m.disc.append(p)
    else:
        p = Process(c, 10, 5, 3)
        m.disc.append(p)
    c +=1

m.printDisc()
m.printBitMap()
m.printMem()
while True:
    time.sleep(1)
    print("Running Swapping")
    m.swapping()
    m.printBitMap()
