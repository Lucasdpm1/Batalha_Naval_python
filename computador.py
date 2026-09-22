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
    cordenada=escolher_jogada(computador);
    print(f"Computador Jogou em :{cordenada} ")
    computador.fazer_jogada(cordenada,adversario)
    