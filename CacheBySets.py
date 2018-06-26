from Cache import *
class CacheBySets(Cache):
    def __init__(self, linhas, palavras_linhas, num_conjuntos):
        super().__init__(linhas, palavras_linhas, num_conjuntos)
        #completar

    def insert(self, tag, conj = 0):
        new_conj = self.modulos[conj]
        new_idx = new_conj.idx
        if(new_conj.isFull()):
            if self.alg_substituicao == 0:  # FIFO #Algoritmo de Substituiçao
                '''  
                    if self.fila.full():  # Cache cheia
                        voltando_memoria = self.fila.get_nowait()  # retira o primeiro item adicionado
                        for i in range(self.linhas):
                            if self.linha[i].tag == voltando_memoria:  # encontra o item a ser retirado
                                linha_nova = i
                                break
                        if self.linha[linha_nova].bit:
                            self.Memoria += 1
                    elif self.idx < self.linhas:  # Cache não cheia, índice numa faixa aceitável
                        linha_nova = self.idx
                    self.fila.put_nowait(tag)  # adiciona o novo item na fila
                '''
            else:  # aleatorio
                linha_nova = randint(0, new_conj.num_lines - 1)
                if new_conj.linhas[linha_nova].bit:
                        self.Memoria += 1
                new_conj.linhas[linha_nova] = Linha(tag, new_idx)
                
            
        else:
            new_conj.linhas[new_idx] = Linha(tag, new_idx)
            new_conj.idx += 1
            
        self.modulos[conj] = new_conj

    
    def look(self, tag, conj = 0): #OK
        index = -1
        for i in range(self.modulos[conj].linhas):  # Procuramos o bloco no conjunto
            if i.tag == tag:
                index = i.idx
                break
            elif i.idx == -1:
                break
        if index != -1: # Acerto de cache 
            self.cache_hit += 1
        else:  # Erro de cache
            self.cache_miss += 1
        return index


    def writeback(self, tag, conj = 0): 
        idx = self.look(tag, conj)  
        if idx != -1:
            self.modulos[conj].linhas[idx].bit = True  # Acerto de cache, bit de uso ligado (bloco atualizado)
        else:
            self.insert(tag, conj)  # erro de cache, o bloco é atualizado e transferido para a cache sem bit de uso ligado

    def writethrough(self, tag, conj = 0): 
        idx = self.look(tag, conj)  # Atualizamos a cache e a memoria
        self.Memoria += 1

    def loadInstrucao(self, tag, conj = 0): #OK
        if self.look(tag, conj) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag, conj)  # Falha de cache

    def loadData(self, tag, conj = 0): #OK
        if self.look(tag, conj) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag, conj)  # Falha de cache

    def storeData(self, tag, politics, conj = 0):
        if politics == 1:
            self.writethrough(tag, conj)
        else:
            self.writeback(tag, conj)


    def modifyData(self, tag, politics, conj = 0): #rever método # 1 == write through || 2 == write back
        self.loadData(tag, conj)
        self.storeData(tag, politics, conj)
