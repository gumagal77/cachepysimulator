class Linha:
    def __init__(self, info = None, idx = -1):
        self.bit = False
        self.idx = idx
        if info is None:
            self.tag = 0
        else:
            self.tag = info

class Conjunto:
    def __init__(self, nro_linhas_conjunto = 1):
        self.num_lines = nro_linhas_conjunto
        self.linhas = [Linha() for i in range(num_lines)]
        self.idx = 0

    def isFull(self):
        return idx == num_lines

class Cache:
    def __init__(self, linhas, palavras_linhas, nro_linhas_conjunto = None):
        self.cache_hit = 0 #Acerto de cache
        self.cache_miss = 0 #Erro de cache
        self.Memoria = 0 #Acesso a memoria
        self.linhas = linhas
        self.tam_block = palavras_linhas
        if nro_linhas_conjunto is not None:
            self.num_conjuntos = linhas / nro_linhas_conjunto
            self.modulos = [Conjunto(nro_linhas_conjunto) for i in range(num_conjuntos)]
            self.associativo_conjunto = True
        else:
            self.associativo_conjunto = False
            self.linha = [Linha() for i in range(linhas)]

