class CacheBySets(Cache):
    def __init__(self, linhas, palavras_linhas, alg_substituicao = 1, politica = 1, num_conjuntos = None):
        super().__init__(linhas, palavras_linhas, num_conjuntos)
        self.politics = politica
        self.algo = alg_substituicao #FIFO = 0 & Aleatorio = 1

    def insert(self, tag, conj=0):
        current = self.cache[conj]

        if current.isFull():
            if self.algo == 0:  # FIFO #Algoritmo de Substituiçao
                linha_nova = current.fila.get_nowait()  # retira o primeiro item adicionado
            else:  # aleatorio
                linha_nova = randint(0, current.tot_lin - 1)
            if current.set[linha_nova].bit_uso:
                self.Memoria += 1
        else:
            linha_nova = current.index

        current.fila.put_nowait(linha_nova) #Inserimos na fila o novo elemento
        current.set[linha_nova].tag = tag

        self.cache[conj] = current
        self.Memoria += 1

    def look(self, tag, conj=0):  # OK
        index = -1
        for i in range(self.cache[conj].tot_lin):  # Procuramos o bloco no conjunto
            if self.cache[conj].set[i].tag == tag:
                index = i
                break
        if index != -1:  # Acerto de cache
            self.cache_hit += 1
        else:  # Erro de cache
            self.cache_miss += 1
        return index

    def writeback(self, tag, conj=0):
        index = self.look(tag, conj)
        if index != -1:
            self.cache[conj].set[index].bit_uso = True  # Acerto de cache, bit de uso ligado (bloco atualizado)
        else:
            self.insert(tag, conj)  # erro de cache, o bloco é atualizado e transferido para a cache sem bit de uso ligado

    def writethrough(self, tag, conj=0):
        index = self.look(tag, conj)  # Atualizamos a cache e a memoria
        if index == -1:
            self.insert(tag, conj)
        else:
            self.Memoria += 1

    def loadInstrucao(self, tag, conj=0):  # OK
        if self.look(tag, conj) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag, conj)  # Falha de cache

    def loadData(self, tag, conj=0):  # OK
        if self.look(tag, conj) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag, conj)  # Falha de cache

    def storeData(self, tag, conj=0):
        if self.politics == 1:
            self.writethrough(tag, conj)
        else:
            self.writeback(tag, conj)

    def modifyData(self, tag, conj=0):  # rever método # 1 == write through || 2 == write back
        self.storeData(tag, conj)

