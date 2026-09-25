# Batalha Naval - GPTech Games

Trabalho 1 de Programação em Python, CEFET-MG Divinópolis (Prof. Guido Pantuza).
Jogo de Batalha Naval em modo texto, feito individualmente.

## Como rodar

Precisa de Python 3.10 ou mais novo. Não usei nenhuma biblioteca de fora, só
`random`, `time` e `datetime` (que já vêm com o Python).

```
python3 main.py
```

Só seguir o menu e digitar o número da opção.

## Arquivos do projeto

- `main.py` - onde tudo se junta: os menus e o loop da partida
- `menu.py` - classe Menu, só mostra as telas de menu
- `utils.py` - validação de entrada (opção do menu e coordenada da jogada)
- `tabuleiro.py` - cria e mostra a matriz 10x10
- `navios.py` - classe Navio e o posicionamento automático dos navios
- `jogador.py` - classe Jogador (tabuleiro, navios, jogadas, acertos)
- `computador.py` - jogada do computador (aleatória)
- `estatisticas.py` - dicionário com partidas/tiros/acertos acumulados
- `replay.py` - mostra o histórico de jogadas da última partida

## O que já funciona

- Menu principal (Nova Partida, Ver Estatísticas, Replay, Créditos, Sair)
- Tabuleiro 10x10 pros dois jogadores
- Navios pequenos (2 casas) e grandes (4 casas), posicionados sozinhos sem
  se sobrepor
- Validação das entradas do jogador (menu e coordenada tipo C5)
- Mensagens de água, acerto e navio afundado
- Tela de fim de jogo com vencedor, total de jogadas e tempo de partida
- Modo Jogador x Computador e modo Dois Jogadores
- Antes da partida começar, cada jogador vê o próprio tabuleiro com os
  navios pra confirmar
- Replay da última partida jogada
- Estatísticas que vão acumulando entre as partidas (enquanto o programa
  está aberto)

## Algumas decisões que tomei

- O enunciado não diz quantos navios cada jogador tem, então defini 6 no
  total: 4 pequenos e 2 grandes.
- O tabuleiro do adversário nunca mostra onde estão os navios escondidos -
  por dentro a matriz sabe onde é `"N"`, mas a função que mostra na tela
  esconde isso até ser atingido. Já a tela de conferência dos próprios
  navios (antes da partida) usa outra função, que mostra tudo.
- A jogada do computador é totalmente aleatória, só evitando repetir uma
  coordenada que ele já tentou. Não tem lógica de perseguir um navio depois
  de acertar (dava pra melhorar isso depois).
- As estatísticas são atualizadas dos dois jogadores no fim de cada
  partida, não só do vencedor. E só existem enquanto o programa está
  rodando, não salvo em arquivo.
- Coordenada segue o formato do enunciado: letra (A-J) + número (1-10),
  sem espaço ou separador, tipo `C5`.


## Autor

Lucas - Engenharia de Computação, CEFET-MG Divinópolis