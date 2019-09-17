import datetime, time
from itertools import cycle
global lru

#Classe que pode criar e remover referencias à páginas
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

#imprime a lista de páginas
def printList(pageList):
    i = 0
    print("Páginas no momento na lista")
    while i < len(pageList):
        print("Posição", i, "Página: ", pageList[i].pageID, ' ', "bitR: ", pageList[i].bitR)
        i += 1

#Verifica e Atualiza o bitR das páginas pela regra dos 10segundos
def upadtePageList(pageList):
    i = 0 
    currentTime = time.time()
    while i < len(pageList):
        pageList[i].updateR(currentTime)
        i += 1

def getLRU(pageList):
    global lru
    currentLRU
    while True:
        if pageList[lru].bitR == 0:
            currentLRU = lru
            if lru == 9:
                lru = 0
            else:
                lru += 1
            return currentLRU
        else:
            pageList[lru].bitR = 0
            if lru == 9:
                lru = 0
            else:
                lru += 1
pageList = []
#p = Page(1)
a = 0
while a < 10:
    p = Page(a)
    pageList.append(p)
    a += 1

printList(pageList)
time.sleep(2)
upadtePageList(pageList)
print("Atualizando paginas")
printList(pageList)
time.sleep(9)
upadtePageList(pageList)
print("atualizando novamente")
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