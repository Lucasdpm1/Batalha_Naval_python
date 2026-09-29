estatistica_principal={
    "Partidas":0,               #dicionario principal com partidas total de tiros e total de acertos todos começam com 0
    "total_tiros":0,
    "total_acertos":0,
}
def atualizar_dicionario(tiros,partida_fim,acertos):
    if(partida_fim==True):   #pra cada partida atualiza o numero das estatisticas principais     #atualizando o dicionario
        estatistica_principal["total_tiros"]+=tiros#apos o fim da partida chama o atualizar que soma as jogadas na esta estatistica principal
        estatistica_principal["total_acertos"]+=acertos

    else:
        print("Partida em Andamento/Não começou")  #caso a partida ainda esteja em andamento print que ainda esta em andamento mas isso nunca vai ser possivel nas funcionalidades atuais pois nao e possivel sair da partida 
        
def contar_partida():        #soma 1 no total de partidas, chamada uma unica vez por partida
    estatistica_principal["Partidas"]+=1

def aproveitamento(acertos,tiros):
    if(tiros==0):          #taxa de aproveitamento
        print("0 jogadas ainda.") #taxa de acerto acumulado no sistema de partidaas
        return 0
    else:
        taxa=acertos/tiros#divisao pra achar a taxa de acertos 
        return taxa*100

def exibir_estatisticas():
    for chave,valor in estatistica_principal.items():   #exibindo os resultados  de taxas de aproveitamento e taxa de acerto e o total de tiros
        print(f"{chave}:  {valor}")#para cada coisa que existe dentro do dicionario ele vai printar total de partidas , tiros , acertos
    taxa=aproveitamento(estatistica_principal["total_acertos"],estatistica_principal["total_tiros"])#aqui chama o aproveitamento passando as duas chaves do dicionario de tiro e acerto como parametro para a funcao aproveitamento
    print("Taxa de Acertos: ", f"{taxa:.2f}%")#validacao sobre o resultado da taxa 
  