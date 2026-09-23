import menu
import utils
import navios
import jogador
import estatisticas
import computador
import tabuleiro
import time
import datetime
import replay
historico=[]
menu_atual=menu.Menu()
menu_atual.exibir_menu()
menu_partida=menu.Menu()

while True:
    opcao=input("Qual Opção Voçe Deseja: ")
    opcao_validada=utils.validar_menu(opcao)
    if(opcao_validada==True):
        opcao=int(opcao)
        break

while opcao_validada==True:
    if(opcao==1):
        menu_partida.menu_partida()
        while True:
            opcao_partida=input("Qual Opção Voçe Deseja: ")
            opcao_partida_validada=utils.validar_menu_partida(opcao_partida)
            if(opcao_partida_validada==True):
                opcao_partida=int(opcao_partida)
                break

        while opcao_partida_validada==True:
            if(opcao_partida==1):
                player1=input("Digite o Nome do Jogador 1: ")
                player2=input("Digite o Nome do Jogador 2: ")
                jogador1=jogador.Jogador(player1)
                jogador2=jogador.Jogador(player2)
                inicio=time.time()
                atacante=jogador1
                defensor=jogador2
                while True:
                    tabuleiro.exibir_matriz(defensor.tabuleiro)
                    coordenada=input(f"{atacante.nome}, digite sua jogada (ex: C5): ")
                    coordenada_validada=utils.validar_posicao(coordenada)
                    if(coordenada_validada==False):
                        continue
                    resultado=atacante.fazer_jogada(coordenada_validada,defensor)
                    if(resultado==None):          #jogada repetida, nao consome a rodada
                        continue
                    historico.append((atacante.nome,coordenada_validada,resultado))
                    if(defensor.todos_afundados()==True):
                        print(f"{atacante.nome} venceu a partida")
                        break

                    atacante,defensor=defensor,atacante
                fim=time.time()
                duracao=fim-inicio
                duracao=datetime.timedelta(seconds=duracao)
                estatisticas.atualizar_dicionario(atacante.tiros_dados,True,atacante.acertos)
                estatisticas.atualizar_dicionario(defensor.tiros_dados,True,defensor.acertos)
                total_jogadas=atacante.tiros_dados+defensor.tiros_dados
                print("Fim de Jogo")
                print(f"Vencedor :{atacante.nome}")
                print(f"Total Jogadas:{total_jogadas}")
                print(f"Duração Partida: {duracao}")
            elif(opcao_partida==2):
                player1=input("Digite o Nome do Jogador 1: ")
                jogador1=jogador.Jogador(player1)
                jogador2=jogador.Jogador("Computador")
                atacante=jogador1
                defensor=jogador2
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
                        print(f"{atacante.nome} venceu a partida!")
                        break

                    atacante,defensor=defensor,atacante
                        #troca quem ataca e quem defende
                fim=time.time()
                duracao=fim-inicio
                duracao=datetime.timedelta(seconds=duracao)
                estatisticas.atualizar_dicionario(atacante.tiros_dados,True,atacante.acertos)
                estatisticas.atualizar_dicionario(defensor.tiros_dados,True,defensor.acertos)
                total_jogadas=atacante.tiros_dados+defensor.tiros_dados
                print("Fim de Jogo")
                print(f"Vencedor :{atacante.nome}")
                print(f"Total Jogadas:{total_jogadas}")
                print(f"Duração Partida: {duracao}")

            elif(opcao_partida==3):
                break

            menu_partida.menu_partida()
            while True:
                opcao_partida=input("Qual Opção Voçe Deseja: ")
                opcao_partida_validada=utils.validar_menu_partida(opcao_partida)
                if(opcao_partida_validada==True):
                    opcao_partida=int(opcao_partida)
                    break

    elif(opcao==2):
        estatisticas.exibir_estatisticas()

    elif(opcao==3):
        replay.exibir_historico(historico)
    elif(opcao==4):
        print("Lucas")
    elif(opcao==5):
        break

    menu_atual.exibir_menu()
    while True:
        opcao=input("Qual Opção Voçe Deseja: ")
        opcao_validada=utils.validar_menu(opcao)
        if(opcao_validada==True):
            opcao=int(opcao)
            break

print("Obrigado Por Jogar.")