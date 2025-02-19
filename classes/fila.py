class Fila:  # Utilizado em BFS
    def __init__(self):
        self.fila = []

    def push(self, item):
        self.fila.append(item)

    def pop(self):
        return self.fila.pop(0)

    def esta_vazio(self):
        return len(self.fila) == 0

