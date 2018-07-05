from CacheDrct import *
from CacheBySets import *

while True:
    try:
        mapeamento = int(input('TIPO DE MAPEAMENTO\n1-Mapeamento Direto\n2-Mapeamento Associativo\n3-Mapeamento Associativo em Conjunto\n'))
        if mapeamento < 1 or mapeamento > 3:
            print('Digite apenas 1, 2 ou 3\n')
        else:
            break
    except ValueError:
        print('Valor inválido!\n')

while True:
    try:
        linhas_cache = int(input('NÚMERO DE LINHAS NA CACHE\n'))
        if linhas_cache < 1:
            print('O número de linhas na cache não pode ser menor que 1\n')
        else:
            break
    except ValueError:
        print('Valor inválido!\n')

while True:
    try:
        palavras_linha = int(input('NÚMERO DE PALAVRAS POR LINHA\n'))
        if palavras_linha < 1:
            print('O número de palavras por linhas não pode ser menor que 1\n')
        else:
            break
    except ValueError:
        print('Valor inválido!\n')

if mapeamento == 3:
    while True:
        try:
            linhas_conjunto = int(input('NÚMERO DE LINHAS POR CONJUNTO\n'))
            if linhas_conjunto < 1:
                print('O número de linhas por conjunto não pode ser menor que 1\n')
            else:
                if linhas_cache % linhas_conjunto != 0:
                    print('O número de linhas na cache deve ser divisível pelo número de linhas por conjunto\n')
                else:
                    break
        except ValueError:
            print('Valor inválido!\n')

while True:
    try:
        politica = int(input('POLÍTICA DE ESCRITA\n1-Write through\n2-Write back\n'))
        if politica!=1 and politica!=2:
            print('Escolha 1 ou 2\n')
        else:
            break
    except ValueError:
        print('Valor inválido\n')

if mapeamento == 2 or mapeamento == 3:
    while True:
        try:
            alg_subs = int(input('ALGORÍTIMO DE SUBSTITUIÇÃO\n0-FIFO\n1-Aleatório\n'))
            if alg_subs != 0 and alg_subs != 1:
                print('Escolha 0 ou 1\n')
            else:
                break
        except ValueError:
            print('Valor inválido!\n')

if mapeamento == 1:
    Direto = CacheDrct(linhas_cache, palavras_linha, politica)
