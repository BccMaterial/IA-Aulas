import numpy as np

class No:
    def __init__(self, estado, no_pai=None, aresta=None):
        self.estado = estado
        self.no_pai = no_pai
        self.aresta = aresta

    def __repr__(self):
        return str(self.estado)

    # def __lt__(self, outro):
    #   return (self.custo + self.heuristica) < (outro.custo + outro.heuristica)


class Visitados:
    def __init__(self):
        # Conjuntos (Sets) em python e {1, 2, 3}
        # necessita ser uma tupla ou string por ser comparável com ==
        self.visitados = set({})

    def adicionar(self, no):
        self.visitados.add(tuple(no.estado.flatten()))

    def foi_visitado(self, no):
        return tuple(no.estado.flatten()) in self.visitados

    def tamanho(self):
        return len(self.visitados)


def no_caminho(no):
    caminho = [no.estado]
    while no.no_pai is not None:
        no = no.no_pai
        caminho.append(no.estado)
    caminho.reverse()
    return caminho


def vertice_caminho(no):
    caminho = []
    while no.no_pai is not None:
        if no.aresta is not None: caminho.append(no.aresta)
        no = no.no_pai
    caminho.reverse()
    return caminho


# Breadth-First Search - Busca em Largura
def bfs(problema):
    no = problema.iniciar()
    fila = Fila()
    fila.push(no)

    visitados = Visitados()

    while not fila.esta_vazio():
        no = fila.pop()
        visitados.adicionar(no)

        # faz o teste objetivo. Se chegou no resultado final
        # retorna o No correspondente
        if (problema.testar_objetivo(no)):
            return (visitados.tamanho(), no)

        # função sucessores define os Nós sucessores
        nos_sucessores = problema.gerar_sucessores(no)

        # para cada sucessor, se armazena se ainda não visitado
        for no_sucessor in nos_sucessores:
            # pula estado_filho se já foi expandido
            if not visitados.foi_visitado(no_sucessor): fila.push(no_sucessor)

    return (visitados.tamanho(), None)


class Fila:  #Utilizado em BFS
    def __init__(self):
        self.fila = []

    def push(self, item):
        self.fila.append(item)

    def pop(self):
        if (self.esta_vazio()):
            return None
        else:
            return self.fila.pop(0)

    def esta_vazio(self):
        return len(self.fila) == 0


#Depth-First Search - Busca em Profundidade
def dfs(problema):
    no = problema.iniciar()
    pilha = Pilha()
    pilha.push(no)
    visitados = Visitados()

    while not pilha.esta_vazio():
        no = pilha.pop()
        visitados.adicionar(no)

        if problema.testar_objetivo(no):
            return visitados.tamanho(), no

        nosSucessores = problema.gerar_sucessores(no)
        for noSucessor in nosSucessores:
            if not visitados.foi_visitado(noSucessor):
                pilha.push(noSucessor)

    return (visitados.tamanho(), None)
class Pilha: #Utilizado em DFS
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if (self.esta_vazio()):
            return None
        else:
            return self.pilha.pop()

    def esta_vazio(self):
        return len(self.pilha) == 0

    def tamanho(self):
        return len(self.pilha)


class Labirinto:
    def __init__(self):
        self.estado_inicial = np.array([
            "I", "#", ".", ".", ".",
            ".", ".", "#", ".", ".",
            ".", "#", ".", "#" ".",
            ".", ".", ".", ".", "#",
            "#", "#", "#", "R", ".",
        ])
        self.estado_objetivo = np.array([
            ".", "#", ".", ".", ".",
            ".", ".", "#", ".", ".",
            ".", "#", ".", "#" ".",
            ".", ".", ".", ".", "#",
            "#", "#", "#", "I", ".",
        ])

    def iniciar(self):
        return No(self.estado_inicial)

    # Função auxiliar para imprimir
    # deve retornar o nó raiz
    # def retornarEstadoInicial(self):
    # return self.estado_inicial

    def imprimir(self, no):
        estado = no.estado
        return estado

    def testar_objetivo(self, no): #Função booleana que verifica se o estado atual é o estado objetivo do problema
        return np.array_equal(no.estado, self.estado_objetivo)

    def gerar_sucessores(self, no): #Gera sucessores válidos a partir de um estado válido e retorna uma lista de nó sucessores
        estado = no.estado  #Estado atual do Nó(estado atual do array)
        nosSucessores = []
        posicao = np.argwhere(estado == "I")[0]  #Localização da pessoa no labirinto
        linha, coluna = posicao  # ??????????

        #Dicionrio utilizado para guardar os possíveis movimentos
        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1)
        }

        for acao, (dLinha, dColuna) in movimentos.items():
            novaLinha = linha + dLinha
            novaColuna = coluna + dColuna

            if 0 <= novaLinha < estado.shape[0] and 0 <= novaColuna < estado.shape[1]:
                if estado[novaLinha, novaColuna] != "#":
                    novo_estado = np.copy(estado)
                    novo_estado[linha, coluna] = "."
                    novo_estado[novaLinha, novaColuna] = "I"
                    nosSucessores.append(No(novo_estado, no, acao))

        return nosSucessores


if __name__ == "__main__":

    #Código com BFS
    problema = Labirinto()
    resultado = bfs(problema)

    if resultado[1] is not None:  #Imprime o estado objetivo utilizando BFS
        caminho = no_caminho(resultado[1])
        print("Caminho percorrido até o estado final:")
        for estado in caminho:
            for linha in estado:
                print(" ".join(linha))
                print()
    else:
        print("Não existe uma solução que leve até o estado final")

    #Código com DFS
    #problema = Labirinto()
    #resultado = bfs(problema)

    #if resultado[1] is not None:  # Imprime o estado objetivo utilizando BFS
        #caminho = no_caminho(resultado[1])
        #print("Caminho percorrido até o estado final:")
        #for estado in caminho:
            #for linha in estado:
                #print(" ".join(linha))
                #print()
    #else:
        #print("Não existe uma solução que leve até o estado final")




# Por algum motivo o código não está funcionando no collab, mas consegui compilar com sucesso no pyCharm e chegar no estado objetivo

