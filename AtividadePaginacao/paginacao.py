import datetime, time

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

p = Page(1)
print(p.pageID, ' ', p.bitR, ' ', p.insertTime)
time.sleep(12)
currentTime = time.time()
print(currentTime)
p.updateR(currentTime)
print(p.pageID, ' ', p.bitR)