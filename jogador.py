import navios
import tabuleiro
import utils
class Jogador():#classe jogador pois precisa ficar repetindo 
    def __init__(self,nome):
        self.nome=nome#atributo nome
        self.tabuleiro=tabuleiro.criando_matriz()#tabuleiro pega matriz usando o arquivo tabuleiro
        self.navios=navios.posicionar_todos_navios(self.tabuleiro)#navios do jogador com o arquivo navio
        self.tiros_dados=0                                          #criando os atributos da classe
        self.acertos=0
        self.jogadas_feitas=[]

    def fazer_jogada(self,posicao,adversario):
        posicao_valida=utils.validar_posicao(posicao);#valida posicao tentada pelo usuario

        if posicao_valida in self.jogadas_feitas:           
            print("Essa Jogada Já foi Realizada")#verifica se a jogada tentada pelo usuario ja foi usada
            return
            
        else:
            self.tiros_dados+=1#se passar tudo anota +1 tiro
            self.jogadas_feitas.append(posicao_valida);#salva a posicao jogada na lista de jogadas ja feitas
            linha=int(posicao_valida[1:])#pega o numero que o usuario digitou
            coluna=posicao_valida[0]                     #anota no tabuleiro do adversario
            linha=linha-1# linha e coluna# indice 0 a 9 
            coluna=ord(coluna)-ord("A")# faz o teste de qual letra ele digitou com tabela asCCi
            if adversario.tabuleiro[linha][coluna]=="N":# se no tabuleiro do adversario for navio joga dnv e anota acerto e faz a verificacao se afundou  ou nao
                self.acertos+=1;
                adversario.tabuleiro[linha][coluna]="X" #marca como x pra ficar como acerto
                for navio in adversario.navios:                            #confere cada navio no tabuleiro pra ver se ja foi afundado ou nao
                    if (linha,coluna) in navio.posicoes:         
                        navio.registrar_acerto((linha,coluna))
                        afundou=navio.esta_afundado()#testa se o navio esta afundado ou nao
                        if(afundou==True):
                            print("Navio Afundado")#prints e returns do resultado
                            return "Afundado"
                        else:
                            print("Apenas Acerto")
                            return "Acerto"

            else:
                adversario.tabuleiro[linha][coluna]="O" #marca apenas o tiro na agua ja que na posicao no campo do adversario  nao era navio e passa a vez 
                print("Tiro na água")
                return "Água"


    def todos_afundados(self):
        for navio in self.navios:               
            if navio.esta_afundado()==False:    #CONFERE SE AINDA RESTAM NAVIOS VIVOS
                print("Ainda Restam Navios")
                return False
        return True
        