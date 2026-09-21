import navios
import tabuleiro
import utils
class Jogador():
    def __init__(self,nome):
        self.nome=nome
        self.tabuleiro=tabuleiro.criando_matriz()
        self.navios=navios.posicionar_todos_navios(self.tabuleiro)
        self.tiros_dados=0
        self.acertos=0
        self.jogadas_feitas=[]

    def fazer_jogada(self,posicao,tabuleiro):
        posicao_valida=utils.validar_posicao(posicao);

        for jogada in self.jogadas_feitas:
            if(posicao_valida==jogada):
                print("Essa Jogada Já foi Realizada")
                break
            else:
                self.tiros_dados+=1
                self.jogadas_feitas.append(posicao);
