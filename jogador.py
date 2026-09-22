import navios
import tabuleiro
import utils
class Jogador():
    def __init__(self,nome):
        self.nome=nome
        self.tabuleiro=tabuleiro.criando_matriz()
        self.navios=navios.posicionar_todos_navios(self.tabuleiro)
        self.tiros_dados=0                                          #criando os atributos da classe
        self.acertos=0
        self.jogadas_feitas=[]

    def fazer_jogada(self,posicao,adversario):
        posicao_valida=utils.validar_posicao(posicao);

        if posicao_valida in self.jogadas_feitas:           #verifica se a jogada tentada pelo usuario ja foi usada
            print("Essa Jogada Já foi Realizada")
            return
            
        else:
            self.tiros_dados+=1
            self.jogadas_feitas.append(posicao_valida);
            linha=int(posicao_valida[1:])
            coluna=posicao_valida[0]                     #anota no tabuleiro do adversario
            linha=linha-1
            coluna=ord(coluna)-ord("A")
            if adversario.tabuleiro[linha][coluna]=="N":
                self.acertos+=1;
                adversario.tabuleiro[linha][coluna]="X" 
                for navio in adversario.navios:                            #confere cada navio no tabuleiro
                    if (linha,coluna) in navio.posicoes:         
                        navio.registrar_acerto((linha,coluna))
                        afundou=navio.esta_afundado()
                        if(afundou==True):
                            print("Navio Afundado")
                        else:
                            print("Apenas Acerto")

            else:
                adversario.tabuleiro[linha][coluna]="O"
                print("Tiro na água")


    def todos_afundados(self):
        for navio in self.navios:
            if navio.esta_afundado()==False:    #CONFERE SE AINDA RESTAM NAVIOS VIVOS
               # print("Ainda Restam Navios")
                return False
        return True
        