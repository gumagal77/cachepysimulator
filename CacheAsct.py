class Associativo(CacheBySets):
    def __init__(self, linhas, palavras_linhas, alg_substituicao = 1, politica = 1):
        super().__init__(linhas, palavras_linhas, alg_substituicao, politica)
        self.tag = 0 #qual a tag atual

    def calcula(self, adress):
        ###########
        self.tag = ####
