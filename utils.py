def validar_menu(resposta):
    try:        #tentando colocar a resposta do usuario em numeros interios se der errado e porque nao e numero
        resposta=int(resposta)
        if(resposta<1 or resposta>5):  #digitou numero mas nao entre as opcoes corretas
            print("Opção inválida, valor tem que ser entre 1 e 5")
            return False
        return True
    except ValueError:
        print("Entrada Inválida digite apenas números")
        return False
def validar_menu_partida(resposta):
    try:        #tentando colocar a resposta do usuario em numeros interios se der errado e porque nao e numero
        resposta=int(resposta)
        if(resposta<1 or resposta>3):  #digitou numero mas nao entre as opcoes corretas
            print("Opção inválida, valor tem que ser entre 1 e 3")
            return False
        return True
    except ValueError:
        print("Entrada Inválida digite apenas números")
        return False

def validar_posicao(entrada):
    entrada=entrada.strip().upper()   #colocando em maiusculo e separando os caracteres
    if len(entrada)<2 or len(entrada)>3:  #verifica se a entrada possiu 2 caracteres ou 3 no caso da linha 10
        print("Entrada Precisa ter 2 ou 3 casas apenas")
        return False
    letra=entrada[0]
    numero=entrada[1:]

    if not ('A'<= letra <= 'J'):                   #verificando se o usuario digitou as 10 primeiras letras do alfabeto
        print("A letra precisa ser entre A a J")
        return False

    if not(numero.isdigit()):   #verificando se o final é um numero ou se possui letras
        print("Número precisa estar entre 1 e 10 e conter apenas numeros após a primeira letra")
        return False;

    numero=int(numero);     #verificacao do numero final formado
    if(numero<1 or numero >10):
        print("Número precisa estar entre 1 e 10")
        return False

    else:
        return entrada