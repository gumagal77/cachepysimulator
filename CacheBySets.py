from Cache import *
from random import randint
class CacheBySets(Cache):
    def __init__(self, linhas, palavras_linhas, alg_substituicao = 1, politica = 1, nro_linhas_conjuntos = -1):
        super().__init__(linhas, palavras_linhas, nro_linhas_conjuntos)
        self.politics = politica
        self.algo = alg_substituicao #FIFO = 0 & Aleatorio = 1
        self.qconj = 0 #qual conjunto o bloco atual pertence
        self.qtag = 0 # qual a tag do bloco atual

   
    #SEMPRE UTILIZAR PARA ATUALIZAR QUAL É O CONJUNTO E TAG ATUAL
    def calcula(self, adress):
        # calculo da tag e conj
        tipo, endereco = adress.split()
        endereco = int(endereco[:-2], 16)
        endereco = int(endereco/self.tam_block)
        whichset = endereco%self.num_conjuntos
        tag = int(endereco/self.num_conjuntos)
        
        self.qconj = whichset
        self.qtag = tag
        return tipo

    def insert(self):
        current = self.cache[self.qconj]

        if current.isFull():
            if self.algo == 0:  # FIFO #Algoritmo de Substituiçao
                linha_nova = current.fila.get_nowait()  # retira o primeiro item adicionado
            else:  # aleatorio
                linha_nova = randint(0, current.tot_lin - 1)
            if current.conj[linha_nova].bit_uso:
                self.Memoria += 1
        else:
            linha_nova = current.index

        current.fila.put_nowait(linha_nova) #Inserimos na fila o novo elemento
        current.conj[linha_nova].tag = self.qtag

        self.cache[self.qconj] = current
        self.Memoria += 1

    def look(self):  # OK
        index = -1
        for i in range(self.cache[self.qconj].tot_lin):  # Procuramos o bloco no conjunto
            if self.cache[self.qconj].conj[i].tag == self.qtag:
                index = i
                break
        if index != -1:  # Acerto de cache
            self.cache_hit += 1
        else:  # Erro de cache
            self.cache_miss += 1
        return index

    def writeBack(self):
        index = self.look()
        if index != -1:
            self.cache[self.qconj].conj[index].bit_uso = True  # Acerto de cache, bit de uso ligado (bloco atualizado)
        else:
            self.insert()  # erro de cache, o bloco é atualizado e transferido para a cache sem bit de uso ligado

    def writeThrough(self):
        index = self.look()  # Atualizamos a cache e a memoria
        if index == -1:
            self.insert()
        else:
            self.Memoria += 1
            
    def load(self):
        if self.look() == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert()  # Falha de cache
    
    def loadInstrucao(self):  # OK
        self.load()

    def loadData(self):  # OK
        self.load() 

    def storeData(self):
        if self.politics == 1:
            self.writeThrough()
        else:
            self.writeBack()

    def modifyData(self):  # rever método # 1 == write through || 2 == write back
        self.storeData()
