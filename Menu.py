class Menu:
    def __init__(self):
        self.mapeamento = -1
        self.linhas_cache = -1
        self.palavras_linha = -1
        self.linhas_conjunto = -1
        self.politica = -1
        self.alg_subs = -1

    def le_mapeamento(self):
        while True:
            try:
                self.mapeamento = int(input('TIPO DE MAPEAMENTO\n1-Mapeamento Direto\n2-Mapeamento Associativo\n3-Mapeamento Associativo em Conjunto\n'))
                if self.mapeamento < 1 or self.mapeamento > 3:
                    print('Digite apenas 1, 2 ou 3\n')
                else:
                    break
            except ValueError:
                print('Valor inválido!\n')

    def le_linhas_cache(self):
        while True:
            try:
                self.linhas_cache = int(input('NÚMERO DE LINHAS NA CACHE\n'))
                if self.linhas_cache < 1:
                    print('O número de linhas na cache não pode ser menor que 1\n')
                else:
                    break
            except ValueError:
                print('Valor inválido!\n')

    def le_palavras_linha(self):
        while True:
            try:
                self.palavras_linha = int(input('NÚMERO DE PALAVRAS POR LINHA\n'))
                if self.palavras_linha < 1:
                    print('O número de palavras por linhas não pode ser menor que 1\n')
                else:
                    break
            except ValueError:
                print('Valor inválido!\n')

    def le_linhas_conjunto(self):
        if self.mapeamento == 3:
            while True:
                try:
                    self.linhas_conjunto = int(input('NÚMERO DE LINHAS POR CONJUNTO\n'))
                    if self.linhas_conjunto < 1:
                        print('O número de linhas por conjunto não pode ser menor que 1\n')
                    else:
                        if self.linhas_cache % self.linhas_conjunto != 0:
                            print('O número de linhas na cache deve ser divisível pelo número de linhas por conjunto\n')
                        else:
                            break
                except ValueError:
                    print('Valor inválido!\n')

    def le_politica(self):
        while True:
            try:
                self.politica = int(input('POLÍTICA DE ESCRITA\n1-Write through\n2-Write back\n'))
                if self.politica != 1 and self.politica != 2:
                    print('Escolha 1 ou 2\n')
                else:
                    break
            except ValueError:
                print('Valor inválido\n')

    def le_alg_sub(self):
        if self.mapeamento == 2 or self.mapeamento == 3:
            while True:
                try:
                    self.alg_subs = int(input('ALGORÍTIMO DE SUBSTITUIÇÃO\n0-FIFO\n1-Aleatório\n'))
                    if self.alg_subs != 0 and self.alg_subs != 1:
                        print('Escolha 0 ou 1\n')
                    else:
                        break
                except ValueError:
                    print('Valor inválido!\n')
