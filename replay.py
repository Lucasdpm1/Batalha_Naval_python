def exibir_historico(historico):         #funcao pra exibir o replay da partida e o que estiver dentro da lista de historico
    total=len(historico)                    #que mostra tudo que esta la dentro e se nao tiver nada mostra nada
    numero=1                                
    for jogada in historico:
        nome,cordenada,resultado=jogada         #printa as jogadas de cada jogador salvas se nao tiver nada no historico nao retorna nada , pois nao tem nenhuma partida salva em historico no main
        print(f"Jogada{numero}/{total}  - {nome}  - {cordenada} - {resultado}")#print das jogas com o numero 1/ total de jogadas que foram realizadas entre os 2 jogadores no total
        numero=numero+1;#pra cada execucao do loop aumenta o valor do numero para padronizar a saida