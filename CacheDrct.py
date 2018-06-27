from CacheBySets import *
class CacheDrct(CacheBySets):
    def __init__(self, linhas, palavras_linha, poli):
        super().__init__(linhas, palavras_linha, 1, poli, 1)

    def look(self):
        if self.cache[self.qconj].conj[0].tag == self.qtag:
            self.cache_hit += 1
            return 1
        else:
            self.cache_miss += 1
            return -1

    def insert(self):
        if self.cache[self.qconj].conj[0].bit_uso:
            self.Memoria += 1
        self.cache[self.qconj].conj[0] = Linha(self.qtag)
        self.Memoria += 1

    def writeThrough(self):
        self.look()
        self.insert()

    def writeBack(self):
        if self.look() != -1:
            self.cache[self.qconj].conj[0].bit_uso = True
        else:
            self.insert()
    '''
    def loadInstrucao(self):
        if self.d_look() == False:
            self.d_insert()

    def loadData(self):
        self.d_loadinstrucao()
    
    def storeData(self):
        if self.politics == 1:
            self.d_writethrough()
        else:
            self.d_writeback()

    def d_modifyData(self):  # rever método # 1 == write through || 2 == write back
        self.d_storeData()
    '''
