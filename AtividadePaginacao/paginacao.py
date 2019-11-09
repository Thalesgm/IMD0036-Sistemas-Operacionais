#IMD0036 - SISTEMAS OPERACIONAIS - T02
#Atividade Prática - Gerenciamento de Memória - Paginação
#Eucharlis Vieria Duarte
#Thales Gomes Moreira

import datetime, time
from itertools import cycle
lru = 0 # Variável Global para controle de LRU

#Variavel Para controlar o tempo entre adição de páginas à lista.
#Aumentar o tempo para verificar aplicação da regra dos 10 segundos
sleepTime = 1 


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
    #Atualiza dados da página na posição
    def updatePage(self, pageID):
        self.pageID = pageID
        self.insertTime = time.time()
        self.bitR = 1

#imprime a lista de páginas
def printList(pageList):
    i = 0
    print("Páginas no ciclo")
    while i < len(pageList):
        print("Posição", i, "|" "Página: ", pageList[i].pageID, '|', "bitR: ", pageList[i].bitR)
        i += 1

#Verifica e Atualiza o bitR das páginas pela regra dos 10segundos
def upadtePageList(pageList):
    i = 0 
    currentTime = time.time()
    while i < len(pageList):
        pageList[i].updateR(currentTime)
        i += 1
#Retorna a LRU e aponta para o próximo elemento
#Se LRU = Atual complexidade o(1)
#Se LRU != Atual complexidade o(n)
def getLRU(pageList):
    global lru
    currentLRU = 0
    while True:
        if pageList[lru].bitR == 0:
            currentLRU = lru
            #Verificação para voltar ao começo da lista, caracterizando comportamento de lista circular.
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

#Adicionar uma nova página à lista
def addPage(pageList, pageID):
    #Lista não está cheia
    if len(pageList) < 10:
        p = Page(pageID)
        pageList.append(p)
    #Lista cheia
    else:
        lru = getLRU(pageList)
        pageList[lru].updatePage(pageID)

#lista de Páginas
pageList = []
currentID = 0

while True:
    addPage(pageList, currentID)
    currentID += 1
    printList(pageList)
    upadtePageList(pageList)
    time.sleep(sleepTime)