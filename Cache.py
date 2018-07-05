from asyncio import Queue
class Linha:
    def __init__(self, info = -1):
        self.bit_uso = False
        self.tag = info

class Conjunto:
    def __init__(self, nro_linhas_conjunto = 1):
        self.conj = [Linha() for i in range(nro_linhas_conjunto)]
        self.index = 0
        self.tot_lin = nro_linhas_conjunto
        self.fila = Queue()

    def isFull(self):
        return self.tot_lin == self.index


class Cache:
    def __init__(self, linhas, palavras_linhas, nro_linhas_conjunto):
        self.cache_hit = 0  # Acerto de cache
        self.cache_miss = 0  # Erro de cache
        self.Memoria = 0  # Acesso a memoria
        self.tam_qtag = 0 # Total de bits destinados a tag
        self.tam_qconj = 99999999 # Total de bits destinados ao "conjunto"

        self.qtd_linhas = linhas
        self.tam_block = palavras_linhas

        if (nro_linhas_conjunto == -1):
            nro_linhas_conjunto = linhas

        self.num_conjuntos = int(linhas / nro_linhas_conjunto)
        self.cache = [Conjunto(nro_linhas_conjunto) for i in range(self.num_conjuntos)]

    def __str__(self):
        hm = self.cache_hit + self.cache_miss
        s = 'Bits destinados a tag: ' + str(self.tam_qtag) + '\n'
        if not hm:
            hm = 1
        if self.tam_qconj != 99999999:
            s += 'Bits destinados a identificação da linha: ' + str(self.tam_qconj) + '\n'

        return 'Cache Hit: %d (%.2f%%)\nCache Miss: %d (%.2f%%)\nQuantidade de acesso ao barramento: %d\n' % (
        self.cache_hit, (self.cache_hit / hm) * 100, self.cache_miss, (self.cache_miss / hm) * 100, self.Memoria) + s
