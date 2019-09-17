import datetime, time
from itertools import cycle
global lru

class Page:
    pageID = 0 # Identificador para a página
    bitR = 0 #bit de representação de uso 0 ou 1
    insertTime = 0 #Tempo de inserção
    #Inicia a classe com os dados.
    def __init__(self, pageID):
        self.bitR = 1
        self.pageID = pageID
        self.insertTime = time.time()
    #Atualiza o bitR
    def updateR(self, currentTime):
        if (currentTime - self.insertTime) > 10:
            self.bitR = 0
    def updatePage(self, currentTime, pageID):
        self.pageID = pageID
        self.insertTime = currentTime
        self.bitR = 1


def printList(pageList):
    i = 0
    while i < len(pageList):
        print("Página: ", pageList[i].pageID, ' ', "bitR: ", pageList[i].bitR)
        i += 1

pageList = []
#p = Page(1)
a = 0
while a < 10:
    p = Page(a)
    pageList.append(p)
    a += 1

printList(pageList)

#pageList.append(p)
#print(p.pageID, ' ', p.bitR, ' ', p.insertTime)
#time.sleep(12)
#currentTime = time.time()
#print(currentTime)
#p.updateR(currentTime)
#print(p.pageID, ' ', p.bitR)
#now = time.time()
#p.updatePage(now, 50)
#print(p.pageID, ' ', p.bitR)