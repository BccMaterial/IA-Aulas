from .no import No
import numpy as np

class Labirinto:
    def __init__(self):
        self.estado_inicial = np.array([
            ["I", "#", ".", ".", "."],
            [".", ".", "#", ".", "."],
            [".", "#", ".", "#", "."],
            [".", ".", ".", ".", "#"],
            ["#", "#", "#", "R", "."]
        ])
        self.estado_objetivo = np.array([
            [".", "#", ".", ".", "."],
            [".", ".", "#", ".", "."],
            [".", "#", ".", "#", "."],
            [".", ".", ".", ".", "#"],
            ["#", "#", "#", "I", "."]
        ])

    def iniciar(self):
        return No(self.estado_inicial)

    def testar_objetivo(self, no):
        return np.array_equal(no.estado, self.estado_objetivo)

    def gerar_sucessores(self, no):
        estado = no.estado
        nos_sucessores = []
        posicao = np.argwhere(estado == "I")[0]
        linha, coluna = posicao

        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1)
        }

        for acao, (delta_linha, delta_coluna) in movimentos.items():
            nova_linha = linha + delta_linha
            nova_coluna = coluna + delta_coluna

            if 0 <= nova_linha < estado.shape[0] and 0 <= nova_coluna < estado.shape[1]:
                if estado[nova_linha, nova_coluna] != "#":
                    novo_estado = np.copy(estado)
                    novo_estado[linha, coluna] = "."
                    novo_estado[nova_linha, nova_coluna] = "I"
                    nos_sucessores.append(No(novo_estado, no, acao))

        return nos_sucessores

