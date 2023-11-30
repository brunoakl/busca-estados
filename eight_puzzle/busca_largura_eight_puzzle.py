"""Module de busca por largura para o problema do 8 puzzle"""
from .eight_puzzle_base import EightPuzzle
from collections import deque

class BuscaLarguraEightPuzzle(EightPuzzle):
    """
    Classe de solução do 8 puzzle, usando Busca por Largura
    """

    def __init__(self, inicio: list) -> None:
        super().__init__(inicio)
    
    def pegar_vizinhos(self, estado: list) -> dict:
        """
        Metódo de pegar vizinho, retornando movimentos possiveis
        """
        return {0: [1, 3],
                1: [0, 2, 4],
                2: [1, 5],
                3: [0, 4, 6],
                4: [1, 3, 5, 7],
                5: [2, 4, 8],
                6: [3, 7],
                7: [4, 6, 8],
                8: [5, 7]}[estado.index(0)]

    def buscar(self) -> list | None:
        """
        Metódo de busca por largura para solucionar o 8 puzzle
        """
        fila = deque([(self.estado_inicial, [])])
        visitados = set([self.estado_inicial])

        while fila:
            estado_atual, caminho_atual = fila.popleft()
            if estado_atual == self.objetivo:
                return caminho_atual
            for vizinho in self.pegar_vizinhos(estado_atual):
                novo_estado = list(estado_atual)
                novo_estado[
                    vizinho], novo_estado[
                        estado_atual.index(0)] = novo_estado[
                            estado_atual.index(0)], novo_estado[vizinho]
                novo_estado = tuple(novo_estado)               
                if novo_estado not in visitados:
                    fila.append((novo_estado, caminho_atual + [novo_estado]))
                    visitados.add(novo_estado)
        return None