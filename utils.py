def validar_menu(resposta):#validacao das primeiras 5 opcoes do menu
    try:        #tentando colocar a resposta do usuario em numeros interios se der errado e porque nao e numero
        resposta=int(resposta)#bloco try pra facilitar a correcao de erros
        if(resposta<1 or resposta>5):  #digitou numero mas nao entre as opcoes corretas
            print("Opção inválida, valor tem que ser entre 1 e 5")#saida visual pro usuario
            return False#retorna false e precisa rodar novamente no main
        return True#deu certo
    except ValueError:
        print("Entrada Inválida digite apenas números")#pegou entrada invalida
        return False
def validar_menu_partida(resposta):
    try:        #tentando colocar a resposta do usuario em numeros interios se der errado e porque nao e numero
        resposta=int(resposta)#mesma coisa da funcao acima so que pra validar o menu da partida com as 3 opções
        if(resposta<1 or resposta>3):  #digitou numero mas nao entre as opcoes corretas
            print("Opção inválida, valor tem que ser entre 1 e 3")
            return False
        return True#retornos pra sair do while no main
    except ValueError:#valor incorreto
        print("Entrada Inválida digite apenas números")
        return False

def validar_posicao(entrada):#validar a posicao digitada pelo usuario
    entrada=entrada.strip().upper()   #colocando em maiusculo e separando os caracteres
    if len(entrada)<2 or len(entrada)>3:  #verifica se a entrada possiu 2 caracteres ou 3 no caso da linha 10 # quantidade de caracteres validacao
        print("Entrada Precisa ter 2 ou 3 casas apenas")
        return False#return de false pra perguntar dnv na main
    letra=entrada[0]# letra e o primeiro caracter da entrada apos fazer o strip que separa os caracteres como um vetor na posicao 0 pega a primeira casa
    numero=entrada[1:]# o numero e o segundo ou o terceiro caracter na casa do 10 por exemplo

    if not ('A'<= letra <= 'J'):                   #verificando se o usuario digitou algo entre as 10 primeiras letras do alfabeto
        print("A letra precisa ser entre A a J")#se nao tiver digitado printa e return falso
        return False

    if not(numero.isdigit()):   #verificando se o final é um numero ou se possui letras 
        print("Número precisa estar entre 1 e 10 e conter apenas numeros após a primeira letra")#verificando se o resto dos 2 caracteres ou 1 caracter possui apenas numeros ou letras no meio pra causar erro
        return False;

    numero=int(numero);     #verificacao do numero final formado
    if(numero<1 or numero >10):
        print("Número precisa estar entre 1 e 10")
        return False

    else:                  #retorno da posicao correta do tabuleiro apos as verificacoes
        return entrada   #retornando ja validado