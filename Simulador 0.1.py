from random import randint
import asyncio

class Linha:
    def __init__(self, info=-1):
        self.bit_uso = False
        self.tag = info


class Conjunto:
    def __init__(self, nro_linhas_conjunto=1):
        self.set = [Linha() for i in range(nro_linhas_conjunto)]
        self.index = 0
        self.tot_lin = nro_linhas_conjunto
        self.fila = asyncio.Queue()

    def isFull(self):
        return self.tot_lin == self.index


class Cache:
    def __init__(self, linhas, palavras_linhas, nro_linhas_conjunto):
        self.cache_hit = 0  # Acerto de cache
        self.cache_miss = 0  # Erro de cache
        self.Memoria = 0  # Acesso a memoria

        self.qtd_linhas = linhas
        self.tam_block = palavras_linhas

        if nro_linhas_conjunto == -1:
            nro_linhas_conjunto = linhas

        self.num_conjuntos = int(linhas / nro_linhas_conjunto)
        self.cache = [Conjunto(nro_linhas_conjunto) for i in range(self.num_conjuntos)]


class CacheBySets(Cache):
    def __init__(self, linhas, palavras_linhas, alg_substituicao = 1, politica = 1, nro_linhas_conjuntos = -1):
        super().__init__(linhas, palavras_linhas, nro_linhas_conjuntos)
        self.politics = politica
        self.algo = alg_substituicao  # FIFO = 0 & Aleatorio = 1
        self.qconj = 0  # qual conjunto o bloco atual pertence
        self.qtag = 0 # qual a tag do bloco atual

    # SEMPRE UTILIZAR PARA ATUALIZAR QUAL É O CONJUNTO E TAG ATUAL
    def calcula(self, adress):
        # calculo da tag e set
        tipo, endereco = adress.split()
        endereco = int(endereco[:-2], 16)
        endereco = int(endereco /self.tam_block)
        whichset = endereco %self.num_conjuntos
        tag = int(endereco /self.num_conjuntos)

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
            if current.set[linha_nova].bit_uso:
                self.Memoria += 1
        else:
            linha_nova = current.index

        current.fila.put_nowait(linha_nova)  # Inserimos na fila o novo elemento
        current.set[linha_nova].tag = Linha(self.qtag)

        self.cache[self.qconj] = current
        self.Memoria += 1

    def look(self):  # OK
        index = -1
        for i in range(self.cache[self.qconj].tot_lin):  # Procuramos o bloco no conjunto
            if self.cache[self.qconj].set[i].tag == self.qtag:
                index = i
                break
        if index != -1:  # Acerto de cache
            self.cache_hit += 1
        else:  # Erro de cache
            self.cache_miss += 1
        return index

    def writeback(self):
        index = self.look()
        if index != -1:
            self.cache[self.qconj].set[index].bit_uso = True  # Acerto de cache, bit de uso ligado (bloco atualizado)
        else:
            self.insert()  # erro de cache, o bloco é atualizado e transferido para a cache sem bit de uso ligado

    def writethrough(self):
        index = self.look()  # Atualizamos a cache e a memoria
        if index == -1:
            self.insert()
        else:
            self.Memoria += 1

    def loadInstrucao(self):  # OK
        if self.look() == -1: # Verificamos se o bloco se encontra na caixa
            self.insert()  # Falha de cache

    def loadData(self):  # OK
        if self.look() == -1:  # Verificamos se o bloco se encontra na caixa
            self.insert()  # Falha de cache

    def storeData(self):
        if self.politics == 1:
            self.writethrough()
        else:
            self.writeback()

    def modifyData(self):  # rever método # 1 == write through || 2 == write back
        self.storeData()


class Direto(CacheBySets):
    def __init__(self, linhas, palavras_linha, poli):
        super().__init__(linhas, palavras_linha, 1, poli, 1)

    def d_look(self):
        if self.cache[self.qconj].set[0].tag == self.qtag:
            self.cache_hit += 1
            return True
        else:
            self.cache_miss += 1
            return False

    def d_insert(self):
        if self.cache[self.qconj].set[0].bit_uso:
            self.Memoria += 1
        self.cache[self.qconj].set[0] = Linha(self.qtag)
        self.Memoria += 1

    def d_writethrough(self):
        self.d_look()
        self.d_insert()

    def d_writeback(self):
        if self.d_look():
            self.cache[self.qconj].set[0].bit_uso = True
        else:
            self.d_insert()

    def d_loadinstrucao(self):
        if not self.d_look():
            self.d_insert()

    def d_loaddata(self):
        self.d_loadinstrucao()

    def d_storeData(self):
        if self.politics == 1:
            self.d_writethrough()
        else:
            self.d_writeback()

    def d_modifyData(self):  # rever método # 1 == write through || 2 == write back
        self.d_storeData()
        

