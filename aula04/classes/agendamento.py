from .satisfacao_restricoes import SatisfacaoRestricoes
from .restricoes import MaxAulasProf, EqAulasMateria

class Agendamento:
    """
    # Modelagem

    Aula: tupla({ matéria, professor })
    Horário: tupla({ dia_semana (seg-sex), hora (8-12) })

    # Restrições

    - [ ] Cada disciplina deve ter exatamente o n° de aulas exigidas
    - [ ] Cada prof. pode lecionar no máximo 4 aulas por semana
    - [x] Cada horário pode ter apenas uma aula
    - [x] Um professor só pode dar aulas das disciplinas que domina
    - [x] Um professor não pode dar mais de uma aula ao mesmo tempo

    > As restrições marcadas já são resolvidas por estar sendo usado tuplas na modelagem
    """

    def __init__(self):
        self.variaveis = []
        self.dominios = {}

    def define_variaveis(self):
        self.variaveis = [
            *[("seg", hora) for hora in range(8, 13)],
            *[("ter", hora) for hora in range(8, 13)],
            *[("qua", hora) for hora in range(8, 13)],
            *[("qui", hora) for hora in range(8, 13)],
            *[("sex", hora) for hora in range(8, 13)]
        ]
        for variavel in self.variaveis:
            self.dominios[tuple(variavel)] = [
                ("mat", "a"), 
                ("fis", "a"),
                ("com", "b"), 
                ("mat", "b"),
                ("fis", "c"), 
                ("com", "c"),
                None # Pode ter aulas livres, no caso é "None"
            ]

    def define_restricoes(self):
        self.problema = SatisfacaoRestricoes(self.variaveis, self.dominios)
        self.problema.adicionar_restricao(MaxAulasProf(self.variaveis, "a", 4))
        self.problema.adicionar_restricao(MaxAulasProf(self.variaveis, "b", 4))
        self.problema.adicionar_restricao(MaxAulasProf(self.variaveis, "c", 4))
        self.problema.adicionar_restricao(EqAulasMateria(self.variaveis, "mat", 3))
        self.problema.adicionar_restricao(EqAulasMateria(self.variaveis, "fis", 2))
        self.problema.adicionar_restricao(EqAulasMateria(self.variaveis, "com", 3))


    def rodar(self):
        self.define_variaveis()
        self.define_restricoes()
        self.resposta = self.problema.busca_backtracking(qtd_atribuicoes=8)

    def imprime_resposta(self):
        if self.resposta is None:
            print("Nenhuma resposta encontrada")
        else:
            for estado, valor in self.resposta.items():
                print(f"{estado}: {valor}")


    def aulas_materia(variaveis, materia = ""):
        aulas_materia = []
        for variavel in variaveis:
            if variavel is None:
                continue
            if variaveis[variavel][1] == materia:
                aulas_materia.append(variavel)
        return aulas_materia
