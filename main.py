import menu
import utils
import navios
import jogador
import estatisticas
import computador
import tabuleiro

menu_atual=menu.Menu()
menu_atual.exibir_menu()
opcao=(input("Qual Opção Voçe Deseja: "))
opcao_validada=utils.validar_menu(opcao)
opcao=int(opcao)
while opcao_validada==True:
    if(opcao==1):

    elif(opcao==2):
        estatisticas.exibir_estatisticas()

    elif(opcao==3):

    elif(opcao==4):
        print("Lucas")
    elif(opcao==5):
        break

    menu_atual.exibir_menu()
    opcao=(input("Qual Opção Voçe Deseja: "))
    opcao_validada=utils.validar_menu(opcao)
    opcao=int(opcao)



print("Obrigado Por Jogar.")