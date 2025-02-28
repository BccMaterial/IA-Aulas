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
    def __init__(self, variaveis, professor, max_aulas):
        super().__init__(variaveis)
        self.professor = professor
        self.max_aulas = max_aulas
    
    def aulas_professor(self, atribuicao):
        qtd_aulas_professor = 0
        for variavel in self.variaveis:
            if atribuicao.get(variavel, None) is None:
                continue
            if (atribuicao[variavel])[1] == self.professor:
                qtd_aulas_professor += 1
        return qtd_aulas_professor

    def esta_satisfeita(self, atribuicao):
        # if self.professor not in atribuicao:
        #     return True
        return self.aulas_professor(atribuicao) <= self.max_aulas


class EqAulasMateria(Restricao):
    def __init__(self, variaveis, materia, qtd_aulas):
        super().__init__(variaveis)
        self.materia = materia
        self.qtd_aulas = qtd_aulas

    def aulas_materia(self, atribuicao):
        qtd_aulas_materia = 0
        for variavel in self.variaveis:
            if atribuicao.get(variavel, None) is None:
                continue
            # print(f"{variavel} => {atribuicao[variavel]")
            if (atribuicao[variavel])[0] == self.materia:
                qtd_aulas_materia += 1
        return qtd_aulas_materia

    def esta_satisfeita(self, atribuicao):
        # if self.materia not in atribuicao:
        #     return True
        return self.aulas_materia(atribuicao) <= self.qtd_aulas



