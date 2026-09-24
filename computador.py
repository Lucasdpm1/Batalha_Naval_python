import random
import utils
import navios
import jogador
def escolher_jogada(computador):
    while True:                                                             #sorteria a posicao do computador
        linha=random.randint(0,9)  #linha e coluna sorteada pra ser uma posicao do navio
        coluna=random.randint(0,9)
        letra=chr(coluna + ord("A"))
        numero=linha+1;
        posicao=letra+str(numero)
        if posicao in computador.jogadas_feitas:
            pass
        else:
            return posicao

def jogar_turno(computador, adversario):
    cordenada=escolher_jogada(computador)          #marcando a jogada do computador usando a funcao de escolher a jogada que faz o sorteio das casas que o o bot vai jogar
    print(f"Computador Jogou em :{cordenada} ")   #print pro main
    resultado=computador.fazer_jogada(cordenada,adversario)
    return cordenada,resultado
    