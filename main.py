import numpy as np
from queue import PriorityQueue

class No:
    def __init__(self, estado, no_pai=None, aresta=None, custo=0.0, heuristica=0.0):
        self.estado = estado
        self.no_pai = no_pai
        self.aresta = aresta
        self.custo = custo
        self.heuristica = heuristica

    def __repr__(self):
        return str(self.estado)

    def __lt__(self, outro):
        return (self.custo + self.heuristica) < (outro.custo + outro.heuristica)


class FilaPrioridade:
    def __init__(self):
        self.fila = PriorityQueue()

    def push(self, valor, item):
        self.fila.put((valor, item))

    def pop(self):
        if (self.esta_vazio()):
            return None
        else:
            (_, no) = self.fila.get()
            return no

    def esta_vazio(self):
        return self.fila.empty()


class Visitados:
    def __init__(self):
        # Conjuntos (Sets) em python e {1, 2, 3}
        # necessita ser uma tupla ou string por ser comparável com ==
        self.visitados = set({})

    def adicionar(self, no):
        self.visitados.add(tuple(no.estado))

    def foi_visitado(self, no):
        return tuple(no.estado) in self.visitados

    def tamanho(self):
        return len(self.visitados)


def dijkstra(problema):
    no = problema.iniciar()
    fila = FilaPrioridade()
    fila.push(0, no)
    visitados = Visitados()
    visitados.adicionar(no)

    while not fila.esta_vazio():
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        resultado = problema.testar_objetivo(no)
        if (resultado):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)

        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor):
                fila.push(no_sucessor.custo, no_sucessor)

    return (visitados.tamanho(), None)


def a_estrela(problema):
    no = problema.iniciar()

    fila = FilaPrioridade()
    fila.push(0, no)

    visitados = Visitados()
    visitados.adicionar(no)

    while not fila.esta_vazio():
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        resultado = problema.testar_objetivo(no)
        if (resultado):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)

        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor):
                no_sucessor.custo = no.custo + problema.custo(no, no_sucessor)
                no_sucessor.heuristica = problema.heuristica(no_sucessor)
                a_estrela_n = (no_sucessor.custo + no_sucessor.heuristica)

                fila.push(a_estrela_n, no_sucessor)

    return (visitados.tamanho(), None)


class Tabuleiro:
    def __init__(self):
        self.tabuleiro = np.array([["_", "1", "1", "1", "-1", "1", "3", "1"],  # _: Pos atual
                                   ["1", "6", "1", "1", "1", "3", "-1", "1"],  # 1: terra(custo 1)
                                   ["1", "6", "-1", "1", "3", "-1", "1", "1"],  # -1: bloqueio(impossível de atravessar)
                                   ["1", "1", "1", "1", "3", "1", "1", "1"],  # 3: água(custo 3)
                                   ["1", "-1", "1", "3", "3", "3", "3", "3"],  # 6: areia movediça(custo 6)
                                   ["-1", "1", "3", "-1", "1", "6", "-1", "-1"],  # 8: objetivo
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

def no_caminho(no):
  caminho = []
  while no.no_pai is not None:
    caminho.append(no.estado)
    no = no.no_pai
  caminho.reverse()  # Inverte a ordem para que ela retorne uma lista do primeiro nó do Array até o ultimo
  return caminho

problema= Tabuleiro()
print("Solução com Dijkstra:")
total, sol = dijkstra(problema)
if sol:
  print(no_caminho(sol))
print("Quantidade de estados visitados: ", total)

print("\n")
total, sol = a_estrela(problema)
if sol:
  print("Solução com A estrela: ", no_caminho(sol))
print("Quantidade de estados visitados: ", total)





