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

