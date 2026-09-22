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
        linha_visivel=[]
        for casa in linha:
            if casa=="N":
                linha_visivel.append("~")   #esconde navio ainda nao atingido
            else:
                linha_visivel.append(casa)

        if numero<10:
            print(numero," "," ".join(linha_visivel))
        else:
            print(numero," ".join(linha_visivel))
        numero=numero+1