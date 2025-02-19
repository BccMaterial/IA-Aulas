import numpy as np
from .no import No

class Tabuleiro:
    def __init__(self):
        # _   = Posição atual
        # 1   = Terra (Custo 1)
        # -1  = Barreira (Não pode passar)
        # 3   = Água (Custo 3)
        # 6   = Areia Movediça (Custo 6)
        # 8   = Objetivo
        self.tabuleiro = np.array([["_", "1", "1", "1", "-1", "1", "3", "1"],
                                   ["1", "6", "1", "1", "1", "3", "-1", "1"],
                                   ["1", "6", "-1", "1", "3", "-1", "1", "1"],
                                   ["1", "1", "1", "1", "3", "1", "1", "1"],
                                   ["1", "-1", "1", "3", "3", "3", "3", "3"],
                                   ["-1", "1", "3", "-1", "1", "6", "-1", "-1"],
                                   ["1", "3", "3", "1", "1", "6", "-1", "1"],
                                   ["3", "3", "1", "-1", "1", "1", "1", "8"]])

        self.posInicial = (0, 0)  # Primeira posição do primeiro Array dentro da Matriz 2d
        self.posObjetivo = (7, 7)  # Ultima posição do ultimo array(Os arrays começam na pos 0, então 7 será o ultimo membro do array)

    def iniciar(self):
        return No(self.posInicial)

    # Função booleana que verifica se o estado atual
    # é o estado objetivo do problema
    def testar_objetivo(self, no):
        return no.estado == self.posObjetivo  # VERIFICAR SE ESTÁ FUNCIONANDO

    def gerar_sucessores(self, no):
        posX, posY = no.estado
        movimentosPossiveis = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Lista de tuplas que permite se mover para cima, baixo, direita e esquerda
        sucessores = []

        for i, j in movimentosPossiveis:
            novaPosX, novaPosY = i + posX, j + posY  # Gera um novo x e y a partir dos possíveis movimentos dentro de movimentosPossiveis
            if 0 <= novaPosX < 8 and 0 <= novaPosY < 8 and self.tabuleiro[novaPosX, novaPosY] != "-1":  # Garante o que o novo x esteja entre 0 <= novoX <= 8 e 0 <= novoY <= 8 e que a nova posição não seja sobre um bloqueio
                if self.tabuleiro[novaPosX, novaPosY]:
                  custo=0
                else:
                  custo = int(self.tabuleiro[novaPosX, novaPosY])  # Transforma a posição do tabuleiro que é uma string em um inteiro que representa o custo de movimentação daquela célula
                sucessores.append(No((novaPosX, novaPosY), no, (i, j), custo=no.custo + custo))  # Adiciona um novo estado sucessor a partir das novas posições de x e y, passa o nó atual como nó pai e também passa o custo do caminho percorrido até o novo nó
        return sucessores

    def custo(self, no, no_destino):
        return int(
            self.tabuleiro[no_destino.estado])  # Transforma a string em inteiro, e este valor é igual ao preço do nó

    # Heurística 2: Distância para o resultado espero
    # Heurística adminissível, pois, sempre o resultado chega mais perto
    # Transformei o array em matriz para fazer cálculo de distância
    def heuristica(self, no):  # A Distância de Manhattan é utilizada para calcular a heurística
        posX, posY = no.estado
        posXdestino, posYdestino = self.posObjetivo
        return abs(posX - posXdestino) + abs(posY - posYdestino)  # Distância de Manhattan: d = |xi-xj| + |yi-yj|

