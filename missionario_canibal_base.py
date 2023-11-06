class Estado:
    def __init__(self, missionarios, canibais, barco):
        self.missionarios = missionarios  # Número de missionários no lado atual
        self.canibais = canibais          # Número de canibais no lado atual
        self.barco = barco                # True se o barco está no lado inicial, False caso contrário

    def __eq__(self, other):
        return (self.missionarios == other.missionarios and
                self.canibais == other.canibais and
                self.barco == other.barco)

    def __hash__(self):
        return hash((self.missionarios, self.canibais, self.barco))

class ProblemaMissionariosCanibais:
    def __init__(self, estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def acoes_possiveis(self, estado: Estado):
        acoes = []
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    if estado.barco:
                        novo_estado = Estado(estado.missionarios - m, estado.canibais - c, False)
                    else:
                        novo_estado = Estado(estado.missionarios + m, estado.canibais + c, True)

                    if self.eh_estado_valido(novo_estado):
                        acoes.append((m, c))
        return acoes

    def eh_estado_valido(self, estado: Estado):
        if estado.missionarios < 0 or estado.canibais < 0:
            return False
        if 3 - estado.missionarios < 0 or 3 - estado.canibais < 0:
            return False
        if (estado.missionarios > 0 and estado.missionarios < estado.canibais) or \
           (3 - estado.missionarios > 0 and 3 - estado.missionarios < 3 - estado.canibais):
            return False
        return True

    def eh_objetivo(self, estado):
        return estado == self.estado_final

    def resolver(self):
        # Implemente aqui a lógica de busca, como busca em largura (BFS) ou busca em profundidade (DFS).
        # Você também pode usar bibliotecas de busca como networkx para simplificar o processo.
        pass
