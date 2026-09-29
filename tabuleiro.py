def criando_matriz():
    linhas=10                 #criando matriz 10/10
    colunas=10                                                            #com o tamanho de linhas e colunas que esta colocado aqui
    tabuleiro=[["~" for i in range(colunas)] for i in range(linhas)] #cria a matriz 10/10 nesse for colocando o ~ pra representar cada casa da matriz
    return tabuleiro

def exibir_matriz(tabuleiro):
    letras="A B C D E F G H I J"
    print("   "+letras)     #cabecalho com as letras
    numero=1
    for linha in tabuleiro:      #mostra a matriz linha por linha com as letras e numeros no formato tradicional
        linha_visivel=[]
        for casa in linha:
            if casa=="N":
                linha_visivel.append("~")   #esconde navio ainda nao atingido pra nao atrapalhar o jogo
            else:
                linha_visivel.append(casa)

        if numero<10:
            print(f" {numero} " + " ".join(linha_visivel))#juntado pra fazer a lateral da matriz
        else:
            print(f"{numero} " + " ".join(linha_visivel))
        numero=numero+1

def exibir_matriz_propria(tabuleiro):
    letras="A B C D E F G H I J"
    print("   "+letras)     #cabecalho com as letras
    numero=1                                      # antes de comecar o jogo mesmo exibe sua propria matriz pra saber onde estao seus proprios barcos
    for linha in tabuleiro:      #mostra a matriz linha por linha
        if(numero<10):
            print(f" {numero} " + " ".join(linha))# mostra a matriz sem esconder os navios do adversario
        else:
            print(f"{numero} " + " ".join(linha))
        numero=numero+1