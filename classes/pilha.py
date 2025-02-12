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

