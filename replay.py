def exibir_historico(historico):         #funcao pra exibir o replay da partida e o que estiver dentro da lista de historico
    total=len(historico)
    numero=1                                
    for jogada in historico:
        nome,cordenada,resultado=jogada         #printa as jogadas de cada jogador salvas
        print(f"Jogada{numero}/{total}  - {nome}  - {cordenada} - {resultado}")
        numero=numero+1;