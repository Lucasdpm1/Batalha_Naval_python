def criando_matriz():
    linhas=10                 #criando matriz 10/10
    colunas=10
    tabuleiro=[["~" for _ in range(colunas)] for _ in range(linhas)] #cria a matriz 10/10 nesse for
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
            print(numero," "," ".join(linha_visivel))
        else:
            print(numero," ".join(linha_visivel))
        numero=numero+1
def exibir_matriz_propria(tabuleiro):
    letras="A B C D E F G H I J"
    print("   "+letras)     #cabecalho com as letras
    numero=1                                      # antes de comecar o jogo mesmo exibe sua propria matriz pra saber onde estao seus proprios barcos
    for linha in tabuleiro:      #mostra a matriz linha por linha
        if(numero<10):
            print (numero," "," ".join(linha))
        else:
            print(numero," ".join(linha))
        numero=numero+1