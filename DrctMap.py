from Cache import *
class mapeamentoDireto(Cache):
    def __init__(self, linhas, palavras_linhas, poli):
        super().__init__(self, linhas, palavras_linhas)
        self.q_tag = 0
        self.idx = 0
        self.politica = poli

    def calcula(self, adress):
        tipo, endereco = adress.split() #separamos a entrada no tipo de instruçao e o endereco
        endereco = endereco[:-2] #Removemos o q tem dps da virgula e a propria
        endereco = str(bin(int(endereco, 16))) #representaçao em binario do endereço no formato string
        endereco = endereco[2: ] #removemos o 0b
        
        return tipo

    def insert(self):
        if self.linha[self.idx].bit and self.politica == 2:
            self.Memoria += 1
        self.linha[self.idx].tag = self.q_tag
        self.Memoria += 1

    def writeback(self, adress):
        if self.look(adress):
            self.linha[self.idx].bit = True

    def writethrough(self, adress):
        if self.look(adress):
            self.Memoria += 1

    def look(self, adress):
        self.calcula(adress)
        if self.linha[self.idx].tag == self.q_tag:
            self.cache_hit += 1
            return True
        else:
            self.cache_miss += 1
            self.insert()
            return False

    def loadInstrucao(self, adress):
        self.look(adress)

    def loadData(self, adress):
        self.look(adress)

    def storeData(self, adress):
        if self.politica == 1:  # 1 to writethrough n 2 to writeback
            self.writethrough(adress)
        else:
            self.writeback(adress)

    def modifyData(self, adress):
        self.look(adress)
        if self.politica == 1:  # 1 - writethrough e 2 - writeback
            self.writethrough(adress)
        else:
            self.writeback(adress)
