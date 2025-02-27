import numpy as np
from .satisfacao_restricoes import SatisfacaoRestricoes
from .restricoes import SeOdeiam, SeGostam, AnimalNaJaula, Adjacente

class Zoo:
    def __init__(self):
        self.variaveis = np.array([])
        self.dominios = {}

    def define_variaveis(self):
        self.variaveis = np.array([
            "T", "L", "H", "S", "J", "P", "A"
        ])

        for variavel in self.variaveis:
            self.dominios[variavel] = np.array([1, 2, 3, 4])

    def define_restricoes(self):
        self.problema = SatisfacaoRestricoes(self.variaveis, self.dominios)
        self.problema.adicionar_restricao(SeOdeiam("L", "T"))
        self.problema.adicionar_restricao(SeOdeiam("L", "A"))
        self.problema.adicionar_restricao(SeOdeiam("T", "A"))
        self.problema.adicionar_restricao(SeOdeiam("T", "P"))
        self.problema.adicionar_restricao(SeOdeiam("T", "S"))
        self.problema.adicionar_restricao(SeOdeiam("T", "J"))
        self.problema.adicionar_restricao(SeOdeiam("L", "P"))
        self.problema.adicionar_restricao(SeGostam("J", "S"))
        self.problema.adicionar_restricao(SeGostam("H", "T"))
        self.problema.adicionar_restricao(AnimalNaJaula("L"))
        self.problema.adicionar_restricao(Adjacente("L", "A"))
        self.problema.adicionar_restricao(Adjacente("T", "A"))

    def rodar(self):
        self.define_variaveis()
        self.define_restricoes()
        self.resposta = self.problema.busca_backtracking()

    def imprime_resposta(self):
        if self.resposta is None:
            print("Nenhuma resposta encontrada")
        else:
            for estado, valor in self.resposta.items():
                print(f"{estado}: {valor}")
