"""Module de busca por A Estrela para o problema dos canibais e missionários"""
from .canibal_missionario_base import BaseMissionarioCanibal
from heapq import heappop, heappush

class BuscaEstrelaCanibalMissionario(BaseMissionarioCanibal):
    """
    Classe de solução do problema dos canibais e missionários, 
    usando busca por A Estrela.
    """
    def __init__(self) -> BaseMissionarioCanibal:
        super().__init__()
        self.estado_objetivo = (0, 0, 0)

    def estado_valido(self, estado: tuple) -> bool:
        """
        Metódo de validar estado
        """
        missionario, canibal, _ = estado
        if missionario < 0 or canibal < 0 or missionario > 3 or canibal > 3:
            return False
        if missionario < canibal and missionario > 0:
            return False
        if (3 - missionario) < (3 - canibal) and (3 - missionario) > 0:
            return False
        return True

    def gerar_sucessores(self, estado: tuple) -> list:
        """
        Metódo de gerar novo estados
        """
        missionario, canibal, barco = estado
        sucessores = []
        for delta_missionario, delta_canibal in [
            (0, 1), (1, 0), (1, 1), (0, 2), (2, 0)]:
            novo_estado = (missionario + delta_missionario * (1 - 2 * barco),
                            canibal + delta_canibal * (1 - 2 * barco), 1 - barco)
            if self.estado_valido(novo_estado):
                sucessores.append(novo_estado)
        return sucessores

    def heuristica(self, estado: tuple):
        """
        Metódo da heuristica da busca por A *
        """
        missionario, canibal, barco = estado
        return missionario + canibal - barco  # Subtrair b para considerar a posição do barco

    def reconstruir_caminho(self, veio_de: tuple, atual: tuple) -> list:
        """
        Metódo de reconstruir caminho da busca por A *
        """
        caminho_total = [atual]
        while atual in veio_de:
            atual = veio_de[atual]
            caminho_total.append(atual)
        return caminho_total[::-1]

    def buscar(self) -> list | None:
        """
        Metódo de buscar por estrela
        """
        fronteira = [(self.heuristica(self.estado_inicial), self.estado_inicial)]
        veio_de = {}
        explorado = set()
        while fronteira:
            _, atual = heappop(fronteira)
            if atual == self.estado_objetivo:
                return self.reconstruir_caminho(veio_de, atual)
            explorado.add(atual)
            for node in self.gerar_sucessores(atual):
                if node not in explorado and node not in veio_de:
                    veio_de[node] = atual
                    heappush(fronteira, (self.heuristica(node), node))
        return None