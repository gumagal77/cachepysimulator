from asyncio import Queue
from random import randint
from Cache import *

#entrada:
# arquivo, tipo de cache (direta, associativa, associativa cj),
# numero linhas total cache, número de palavras por linhas, (ass cj) numero de linhas por conjunto

'''
class Linha:
    def __init__(self, info = None, set = False):
        self.bit = set
        if info is None:
            self.tag = 0
        else:
            self.tag = info

class Cache:
    def __init__(self, linhas, palavras_linhas, nro_linhas_conjunto = None):
        self.cache_hit = 0 #Acerto de cache
        self.cache_miss = 0 #Erro de cache
        self.Memoria = 0 #Acesso a memoria
        self.linhas = linhas
        self.tam_block = palavras_linhas
        if nro_linhas_conjunto is not None:
            self.conjuntos = linhas / nro_linhas_conjunto
            self.linhas_conjunto = nro_linhas_conjunto
            self.sets = [[Linha() for i in range(nro_linhas_conjunto)] for i in range(self.conjuntos)]
            self.associativo_conjunto = True
        else:
            self.associativo_conjunto = False
            self.linha = [Linha() for i in range(linhas)]
'''

class CacheAsct(Cache):
    
    def __init__(self, linhas, palavras_linhas, alg_substituicao=1):
        super().__init__(linhas, palavras_linhas)
        self.idx = 0
        self.alg_substituicao = alg_substituicao  # 0 para FIFO, 1 para aleatório
        if alg_substituicao == 0:  # FIFO
            self.fila = Queue(linhas)

        return s[0]
            

    def insert(self, tag):
        linha_nova = self.idx
        if self.alg_substituicao == 0:  # FIFO #Algoritmo de Substituiçao
            
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

        elif self.idx >= self.linhas:  # aleatorio
            linha_nova = randint(0, self.linhas - 1)
            if self.linha[linha_nova].bit:
                    self.Memoria += 1
        
        self.linha[linha_nova] = Linha(tag)
        self.idx += 1
        self.Memoria += 1  # tranferencia do bloco para a cache

    def look(self, tag):
        check = -1
        for i in range(min(self.idx - 1, self.linhas)):  # Procuramos o bloco na cache
            if self.linha[i].tag == tag:
                check = i
        if check == -1:  # Erro de cache
            self.cache_miss += 1
        else:  # Acerto de cache
            self.cache_hit += 1
        return check

    def writeback(self, tag):
        idx = self.look(tag)  # Verificamos se o bloco esta na cache
        if idx != -1:
            self.linha[idx].bit = True  # Acerto de cache, bit de uso ligado
        else:
            self.insert(tag)  # erro de cache, o bloco é atualizado e transferido para a cache sem bit de uso ligado

    def writethrough(self, tag):
        self.look(tag)  # Atualizamos a cache e a memoria
        self.Memoria += 1

    def loadinstrucao(self, tag):
        if self.look(tag) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag)  # Falha de cache

    def loaddata(self, tag):
        if self.look(tag) == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert(tag)  # Falha de cache

    def storedata(self, tag, politics):
        if politics == 1:
            self.writethrough(tag)
        else:
            self.writeback(tag)


    def modifydata(self, tag, politics):  # 1 == write through || 2 == write back
        self.loaddata(tag)
        self.storedata(tag, politics)
