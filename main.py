from classes import Fila, Visitados, Pilha, Labirinto

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

        if problema.testar_objetivo(no):
            return visitados.tamanho(), no

        nos_sucessores = problema.gerar_sucessores(no)
        for no_sucessor in nos_sucessores:
            if not visitados.foi_visitado(no_sucessor):
                fila.push(no_sucessor)

    return visitados.tamanho(), None

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

if __name__ == "__main__":
    problema = Labirinto()
    resultado = bfs(problema)

    if resultado[1] is not None:
        caminho = no_caminho(resultado[1])
        print("Caminho percorrido até o estado final:")
        for estado in caminho:
            for linha in estado:
                print(" ".join(linha))
            print()

