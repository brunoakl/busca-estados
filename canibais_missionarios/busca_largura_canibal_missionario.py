"""Module de busca por largura para o problema dos canibais e missionários"""
from .canibal_missionario_base import BaseMissionarioCanibal 
from collections import deque

class BuscaLarguraCanibalMissionario(BaseMissionarioCanibal):
    """
    Classe de solução do problema dos canibais e missionários, 
    usando busca por largura.
    """
    def __init__(self):
        super().__init__()
        self.estado_objetivo = (0, 0, -1)

    def buscar(self) -> list|None:
        """
        Implementa o algoritmo de busca em largura.
        """
        fila = deque([self.estado_inicial])
        visitados = set([self.estado_inicial])
        passos = [self.estado_inicial]
        
        while fila:
            estado_atual = fila.popleft()
            if estado_atual == self.estado_objetivo:
                return passos
            for proximo_estado in self.gerar_estados_sucessores(estado_atual):
                if proximo_estado not in visitados and self.validar_estado(proximo_estado):
                    visitados.add(proximo_estado)
                    fila.append(proximo_estado)
                    passos.append(proximo_estado)
        return None
    
    def gerar_estados_sucessores(self, estado_atual: tuple):
        """
        Metódo de gerar estado sucessores de acordo com o uso de busca por largura
        """
        barco = estado_atual[2]
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    novo_estado = (estado_atual[0] - m * estado_atual[2], estado_atual[1] - c * estado_atual[2], -barco)
                    if 0 <= novo_estado[0] <= 3 and 0 <= novo_estado[1] <= 3:
                        yield novo_estado

    def validar_estado(self, estado: tuple) -> bool:
        """
        Metódo de validar estado
        """
        if estado[0] > 0 and estado[0] < estado[1]:
            return False
        if estado[0] < 3 and estado[0] > estado[1]:
            return False
        return True