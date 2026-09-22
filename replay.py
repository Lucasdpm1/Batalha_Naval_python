def exibir_historico(historico):
    total=len(historico)
    numero=1
    for jogada in historico:
        nome,cordenada,resultado=jogada
        print(f"Jogada{numero}/{total}  - {nome}  - {cordenada} - {resultado}")
        numero=numero+1;