import menu
import utils
import navios
import jogador
import estatisticas
import computador              #import dos arquivos principais
import tabuleiro
import time
import datetime
import replay
historico=[]
menu_atual=menu.Menu()
menu_atual.exibir_menu()  #chamada do menu
menu_partida=menu.Menu()
print("\n")
while True:
    opcao=input("Qual Opção Voçe Deseja: ")
    print("\n")
    opcao_validada=utils.validar_menu(opcao)  #valida a opcao do menu
    if(opcao_validada==True):
        opcao=int(opcao)
        break

while opcao_validada==True:
    if(opcao==1):  #opcao de jogar chama o sub menu com as opcoes de partida
        menu_partida.menu_partida()
        while True:
            opcao_partida=input("Qual Opção Voçe Deseja: ")
            print("\n")
            opcao_partida_validada=utils.validar_menu_partida(opcao_partida)
            if(opcao_partida_validada==True):
                opcao_partida=int(opcao_partida)
                break

        while opcao_partida_validada==True:
            if(opcao_partida==1):  #opcao de jogar 1 contra 1 pede os nome e comeca a pedir as jogadas ate sair o vencedor
                player1=input("Digite o Nome do Jogador 1: ")
                print("\n")
                player2=input("Digite o Nome do Jogador 2: ")
                print("\n")
                jogador1=jogador.Jogador(player1)
                jogador2=jogador.Jogador(player2)
        
                atacante=jogador1
                defensor=jogador2
                print(f"Navios: {jogador1.nome}")
                print("\n")
                tabuleiro.exibir_matriz_propria(jogador1.tabuleiro);  #exibi onde estao seus proprios navios antes de comecar o jogo de verdade 
                pergunta=input("Aperte Qualquer Coisa Pra Continuar.")
                print("\n")


                print(f"Navios: {jogador2.nome}")
                tabuleiro.exibir_matriz_propria(jogador2.tabuleiro);#mostra a matriz propria do jogador 2
                pergunta2=input("Aperte Qualquer Coisa Pra Continuar.")
                print("\n")


                inicio=time.time()
                while True:
                    tabuleiro.exibir_matriz(defensor.tabuleiro)  #exibi a matriz atual do adversario rodada por rodada
                    coordenada=input(f"{atacante.nome}, digite sua jogada (ex: C5): ")
                    print("\n")#valida a posicao digitada com a funcao de validacao pra cada jogada digitada em um loop
                    coordenada_validada=utils.validar_posicao(coordenada)#valida a cordenada digitada pelo usuario a cada interacao dentro do loop
                    if(coordenada_validada==False):
                        continue
                    resultado=atacante.fazer_jogada(coordenada_validada,defensor)#faz a jogada no mapa do outro jogador
                    if(resultado==None):          #jogada repetida, nao consome a rodada
                        continue
                    historico.append((atacante.nome,coordenada_validada,resultado))#salva no historico cada jogada que deu certo
                    if(defensor.todos_afundados()==True):#verifica se todos os navios do oponente afundaram
                        print(f"{atacante.nome} venceu a partida")
                        print("\n")
                        break

                    atacante,defensor=defensor,atacante
                fim=time.time()#funcao pra calcular o tempo da partida total
                duracao=fim-inicio
                duracao=datetime.timedelta(seconds=duracao)
                estatisticas.atualizar_dicionario(atacante.tiros_dados,True,atacante.acertos)#atualiza o dicionario das estatisticas com os dados da partida
                estatisticas.atualizar_dicionario(defensor.tiros_dados,True,defensor.acertos)
                total_jogadas=atacante.tiros_dados+defensor.tiros_dados#jogadas do jogador 1 + jogador 2
                print("\n")
                print("Fim de Jogo")
                print(f"Vencedor :{atacante.nome}")
                print(f"Total Jogadas:{total_jogadas}")#exibindo vencedor e os status basico
                print(f"Duração Partida: {duracao}")
                print("\n")
            elif(opcao_partida==2):
                player1=input("Digite o Nome do Jogador 1: ")
                print("\n")
                jogador1=jogador.Jogador(player1)
                jogador2=jogador.Jogador("Computador")
                atacante=jogador1
                defensor=jogador2#player 2 sendo o computador e usando as funcoes de sortear as posicoes do arquivo computador
                print(f"Navios: {jogador1.nome}")
                tabuleiro.exibir_matriz_propria(jogador1.tabuleiro);
                pergunta=input("Aperte Qualquer Coisa Pra Continuar.")
                print("\n")
                inicio=time.time()
                while True:
                    tabuleiro.exibir_matriz(defensor.tabuleiro)     #mostra o tabuleiro de quem vai ser atacado

                    if(atacante.nome=="Computador"):
                        cordenada_jogada,resultado=computador.jogar_turno(atacante,defensor)
                        historico.append((atacante.nome,cordenada_jogada,resultado))
                    else:
                        coordenada=input(f"{atacante.nome}, digite sua jogada (ex: C5): ")
                        coordenada_validada=utils.validar_posicao(coordenada)
                        if(coordenada_validada==False):
                            continue          #se a coordenada nao for valida, pede de novo sem trocar a vez
                        resultado=atacante.fazer_jogada(coordenada_validada,defensor)
                        if(resultado==None):          #jogada repetida, nao consome a rodada
                            continue
                        historico.append((atacante.nome,coordenada_validada,resultado))

                    if(defensor.todos_afundados()==True):
                        print(f"{atacante.nome} venceu a partida!")#mesma logica da opcao 1 , so que agora sem o jogador 2 , que é a propria maquina
                        break   #quebra o loop quando alguem perde

                    atacante,defensor=defensor,atacante
                        #troca quem ataca e quem defende
                fim=time.time()
                duracao=fim-inicio
                duracao=datetime.timedelta(seconds=duracao)#atualiza o dicionario e mostra os status basicos apos o fim da partida
                estatisticas.atualizar_dicionario(atacante.tiros_dados,True,atacante.acertos)
                estatisticas.atualizar_dicionario(defensor.tiros_dados,True,defensor.acertos)
                total_jogadas=atacante.tiros_dados+defensor.tiros_dados
                print("Fim de Jogo")
                print(f"Vencedor :{atacante.nome}")
                print(f"Total Jogadas:{total_jogadas}")
                print(f"Duração Partida: {duracao}")
                print("\n")


            elif(opcao_partida==3):
                break

            menu_partida.menu_partida()
            while True:
                opcao_partida=input("Qual Opção Voçe Deseja: ")
                print("\n")
                opcao_partida_validada=utils.validar_menu_partida(opcao_partida)
                if(opcao_partida_validada==True):
                    opcao_partida=int(opcao_partida)
                    break

    elif(opcao==2):
        estatisticas.exibir_estatisticas() #usa a funcao pra exibir as estatisticas dps de uma partida

    elif(opcao==3):
        replay.exibir_historico(historico) #exibe o historico como replay
    elif(opcao==4):
        print("Lucas")  #eu
        print("\n")

    elif(opcao==5):#encerra o programa 
        break

    menu_atual.exibir_menu()
    while True:
        opcao=input("Qual Opção Voçe Deseja: ")
        print("\n")
        opcao_validada=utils.validar_menu(opcao)
        if(opcao_validada==True):
            opcao=int(opcao)
            break

print("Obrigado Por Jogar.")