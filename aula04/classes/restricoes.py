###################
### CLASSE BASE ###
###################

class Restricao():
    def __init__(self, variaveis):
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
        """
        # Definição
        Verifica se a restrição implementada está satisfeita
        
        # Parâmetros
        A atribuição é um dicionário, onde:
        - A chave é a variável
        - O valor é o "valor de domínio" atribuído
        """
        return True

########################
### RESTRIÇÕES - ZOO ###
########################

class SeGostam(Restricao):
    def __init__(self, animal1, animal2):
        super().__init__([animal1, animal2])
        self.animal1 = animal1
        self.animal2 = animal2

    def esta_satisfeita(self, atribuicao):
        if self.animal1 not in atribuicao or self.animal2 not in atribuicao:
            return True
        return atribuicao[self.animal1] == atribuicao[self.animal2]

class SeOdeiam(Restricao):
    def __init__(self, animal1, animal2):
        super().__init__([animal1, animal2])
        self.animal1 = animal1
        self.animal2 = animal2

    def esta_satisfeita(self, atribuicao):
        if self.animal1 not in atribuicao or self.animal2 not in atribuicao:
            return True
        return atribuicao[self.animal1] != atribuicao[self.animal2]

class AnimalNaJaula(Restricao):
    def __init__(self, animal):
        super().__init__([animal])
        self.animal = animal

    def esta_satisfeita(self, atribuicao):
        if self.animal not in atribuicao:
            return True
        return atribuicao[self.animal] == 1

class Adjacente(Restricao):
    def __init__(self, animal1, animal2):
        super().__init__([animal1, animal2])
        self.animal1 = animal1
        self.animal2 = animal2

    def esta_satisfeita(self, atribuicao):
        if self.animal1 not in atribuicao or self.animal2 not in atribuicao:
            return True
        return abs(atribuicao[self.animal1] - atribuicao[self.animal2]) > 1

################################
### RESTRIÇÕES - AGENDAMENTO ###
################################

class MaxAulasProf(Restricao):
    def __init__(self, professor, max_aulas):
        super().__init__([professor, max_aulas])
        self.professor = professor
        self.max_aulas = max_aulas

    def esta_satisfeita(self, atribuicao):
        if self.professor not in atribuicao:
            return True
        return atribuicao[self.professor] <= self.max_aulas


class EqAulasMateria(Restricao):
    def __init__(self, materia, qtd_aulas):
        super().__init__([materia, qtd_aulas])
        self.materia = materia
        self.qtd_aulas = qtd_aulas

    def esta_satisfeita(self, atribuicao):
        if self.materia not in atribuicao:
            return True
        return atribuicao[self.materia] == self.qtd_aulas
