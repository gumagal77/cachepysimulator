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
        if self.d_look() == False:
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
