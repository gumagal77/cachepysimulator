from Menu import *
from CacheDrct import *
from CacheBySets import *
from datetime import datetime

def start_simulation():
    while True:
        try:
            patht = str(input('Nome de arquivo com os traços: '))
            arqtracos = open(patht, 'r')
            tracos = arqtracos.readlines()
            break
        except FileNotFoundError:
            print('Arquivo não encontrado!\n')

    for i in tracos:
        typ = mapt.calcula(i)
        if typ == 'I':
            mapt.loadInstrucao()
        elif typ == 'L':
            mapt.loadData()
        elif typ == 'S':
            mapt.storeData()
        elif typ == 'M':
            mapt.modifyData()
        else:
            print('Instrução inválida')


    arqname = str(tmap + str(datetime.now()).replace(':', '-') + '.txt')
    arqgerado = open(arqname, 'a')
    arqgerado.write('Arquivo lido: '+patht+'\n'+info + mapt.__str__()+'\n')
    arqgerado.close()
    print(mapt.__str__())


while True:
    try:
        m = int(input("MODO DE EXECUÇÃO\n1.Escolher parâmetros\n2.Carregar parâmetros\n"))
        if m != 1 and m != 2:
            print('Escolha corretamente o modo de execução')
            continue
        if m == 1:
            menu = Menu()
            menu.le_mapeamento()
            menu.le_linhas_cache()
            menu.le_palavras_linha()
            menu.le_linhas_conjunto()
            menu.le_politica()
            menu.le_alg_sub()

            if menu.politica == 1:
                tpol = '-Write through'
            else:
                tpol = '-Write back'
            if menu.alg_subs == 0:
                talg_subs = '-FIFO'
            else:
                talg_subs = '-Aleatorio'

            if menu.mapeamento == 1:
                tmap = 'DrctMap_'
                info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(menu.linhas_cache)+'\nPalavras_linha: '+str(menu.palavras_linha)+'\nPolitica_escrita: '+str(menu.politica)+tpol+'\n\n'
                mapt = CacheDrct(menu.linhas_cache, menu.palavras_linha, menu.politica)
            elif menu.mapeamento == 2:
                tmap = 'AssMap_'
                info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(menu.linhas_cache)+'\nPalavras_linha: '+str(menu.palavras_linha)+'\nPolitica_escrita: '+str(menu.politica)+tpol+'\n'
                info = info + 'Alg_substituicao: '+str(menu.alg_subs)+talg_subs+'\nLinhas_conjunto: '+str(menu.linhas_cache)+'\n\n'
                mapt = CacheBySets(menu.linhas_cache, menu.palavras_linha, menu.alg_subs, menu.politica, menu.linhas_cache)
            else:
                tmap = 'SetAssMap_'
                info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(menu.linhas_cache)+'\nPalavras_linha: '+str(menu.palavras_linha)+'\nPolitica_escrita: '+str(menu.politica)+tpol+'\n'
                info = info + 'Alg_substituicao: '+str(menu.alg_subs)+talg_subs+'\nLinhas_conjunto: '+str(menu.linhas_conjunto)+'\n\n'
                mapt = CacheBySets(menu.linhas_cache, menu.palavras_linha, menu.alg_subs, menu.politica, menu.linhas_conjunto)
            start_simulation()
        else:
            try:
                path = input("Digite o nome do arquivo (deve estar na mesma pasta)\n")
                arqconfig = open(path, 'r')
                config = arqconfig.read().split()
                arqconfig.close()

                if int(config[0]) == 1:
                    tmap = 'DrctMap_'

                    if config[3] == 1:
                        tpol = '1-Write through'
                    else:
                        tpol = '2-Write back'

                    info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(config[1])+'\nPalavras_linha: '+str(config[2])+'\nPolitica_escrita: '+tpol+'\n\n'
                    mapt = CacheDrct(int(config[1]), int(config[2]), int(config[3]))
                elif int(config[0]) == 2:
                    tmap = 'AssMap_'

                    if int(config[3]) == 1:
                        tpol = '1-Write through'
                    else:
                        tpol = '2-Write back'
                    if int(config[4]) == 0:
                        talg_subs = '0-FIFO'
                    else:
                        talg_subs = '1-Aleatorio'

                    info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(config[1])+'\nPalavras_linha: '+str(config[2])+'\nPolitica_escrita: '+tpol+'\n'
                    info = info + 'Alg_substituicao: '+talg_subs+'\nLinhas_conjunto: '+str(config[1])+'\n\n'
                    mapt = CacheBySets(int(config[1]), int(config[2]), int(config[3]), int(config[4]), int(config[1]))
                else:
                    tmap = 'SetAssMap_'

                    if int(config[4]) == 1:
                        tpol = '1-Write through'
                    else:
                        tpol = '2-Write back'
                    if int(config[3]) == 0:
                        talg_subs = '0-FIFO'
                    else:
                        talg_subs = '1-Aleatorio'

                    info = 'Mapeamento: '+tmap+'\nLinhas_cache: '+str(config[1])+'\nPalavras_linha: '+str(config[2])+'\nPolitica_escrita: '+tpol+'\n'
                    info = info + 'Alg_substituicao: '+talg_subs+'\nLinhas_conjunto: '+str(config[5])+'\n\n'
                    mapt = CacheBySets(int(config[1]), int(config[2]), int(config[3]), int(config[4]), int(config[5]))
                start_simulation()
            except IOError:
                print('Arquivo não encontrado. Tente novamente')
                continue
        break

    except ValueError:
        print('Entrada Inválida! Tente novamente.')
