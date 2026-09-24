import utils
import random
class Navio():
    def __init__(self,tamanho,posicoes):
        self.tamanho=tamanho
        self.posicoes=posicoes
        self.atingidas=set()
    def registrar_acerto(self,posicao): #registra se foi acerto ou erro a jogada
        self.atingidas.add(posicao)

    def esta_afundado(self):
        if(len(self.atingidas)==self.tamanho):
            return True
        else: #verica se foi acerto ou afunsou o navio por completo
            return False


def calcular_posicoes(linha, coluna, orientacao, tamanho):
    lista=[]
    for i in range(tamanho):                 #calcula as posicoes posiveis
        if(orientacao=="H"):
            lista.append((linha,coluna+i))
        else:
            lista.append((linha+i,coluna))

    return lista
        

def posicao_valida(posicoes, tabuleiro):
    for posicao in posicoes:
        linha,coluna=posicao     #verifica se a posicao que o random marcou esta dentro da matriz e retorna true se sim
        if(linha<0 or linha>9 or coluna<0 or coluna>9):
            return False
        if(tabuleiro[linha][coluna]!="~"):
            return False
    return True



def posicionar_navio(tabuleiro, tamanho):
    while True:
        l=random.randint(0,9)  #linha e coluna sorteada pra ser uma posicao do navio
        c=random.randint(0,9)
        orientacao=random.choice(["H","V"])
        posicoes_possiveis=calcular_posicoes(l,c,orientacao,tamanho)
        if(posicao_valida(posicoes_possiveis,tabuleiro)==True):
            for posicao in posicoes_possiveis:
                linha,coluna=posicao
                tabuleiro[linha][coluna]="N"  #marcando navio no mapa para cada local sorteado possivel 
        
        

            return Navio(tamanho,posicoes_possiveis)

def posicionar_todos_navios(tabuleiro):
    lista_navios=[]
    quantidade_pequenos=4  #4 navios pequenos
    quantidade_grande=3    # navios grandes
    for navio in range(quantidade_pequenos):
        local=posicionar_navio(tabuleiro,2)       #posiciona os navios pequenos de tamanho 2 e pega a posicao deles e coloca na lista final
        lista_navios.append(local)
    for navio_grande in range(quantidade_grande):
            local2=posicionar_navio(tabuleiro,4)      #posiciona os navios grandes de tamanho 4 e pega a posicao deles e coloca na lista final
            lista_navios.append(local2)

    return lista_navios          