estatistica_principal={
    "Partidas":0,               #dicionario principal
    "total_tiros":0,
    "total_acertos":0,
}
def atualizar_dicionario(tiros,partida_fim,acertos):
    if(partida_fim==True):
        estatistica_principal["Partidas"]+=1      #atualizando o dicionario
        estatistica_principal["total_tiros"]+=tiros
        estatistica_principal["total_acertos"]+=acertos

    else:
        print("Partida em Andamento/Não começou")
        


def aproveitamento(acertos,tiros):
    if(tiros==0):          #taxa de aproveitamento
        print("0 jogadas ainda.")
        return 0
    else:
        taxa=acertos/tiros
        return taxa*100

def exibir_estatisticas():
    for chave,valor in estatistica_principal.items():   #exibindo os resultados
        print(f"{chave}:  {valor}")
    taxa=aproveitamento(estatistica_principal["total_acertos"],estatistica_principal["total_tiros"])
    print("Taxa de Acertos: ", f"{taxa:.2f}%")