def criando_matriz():
    linhas=10                 #criando matriz 10/10
    colunas=10
    tabuleiro=[["~" for _ in range(colunas)] for _ in range(linhas)]
    return tabuleiro

def exibir_matriz(tabuleiro):
    letras="A B C D E F G H I J"
    print("   "+letras)     #cabecalho com as letras
    numero=1
    for linha in tabuleiro:      #mostra a matriz linha por linha
        if numero<10:
            print(numero," "," ".join(linha))
        else:
            print(numero," ".join(linha))
        numero=numero+1


