import random #biblioteca pra sortear
import utils
import navios
import jogador
def escolher_jogada(computador):
    while True:                                                             #sorteria a posicao do computador
        linha=random.randint(0,9)  #linha e coluna sorteada pra ser uma posicao do navio
        coluna=random.randint(0,9)
        letra=chr(coluna + ord("A"))#tabela ascci pra descobrir a letra que foi sorteada pro bot jogar
        numero=linha+1;#+1 pra o numero ser entre 1 a 10
        posicao=letra+str(numero)#cocatenando letra+o numero sorteado pelo random
        if posicao in computador.jogadas_feitas:
            pass
        else:
            return posicao#se nao tiver ja feito essa jogada retorna a posicao que foi sorteada para a funcao de baixo

def jogar_turno(computador, adversario):
    cordenada=escolher_jogada(computador)          #marcando a jogada do computador usando a funcao de escolher a jogada que faz o sorteio das casas que o o bot vai jogar
    print(f"Computador Jogou em :{cordenada} ")   #print pro main
    resultado=computador.fazer_jogada(cordenada,adversario)#passa a cordenada pra funcao de fazer jogada da classe jogador que pega a posicao e marca no mapa do adversario
    return cordenada,resultado #retorna a cordenada que foi jogada e o resultado daquela jogada pra fazer o replay depois
    