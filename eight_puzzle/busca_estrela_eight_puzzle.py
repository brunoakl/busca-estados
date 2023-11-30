"""Module de busca por a estrela para o problema do 8 puzzle"""
from .eight_puzzle_base import EightPuzzle
from heapq import heappop, heappush

class BuscaAEstrelaEightPuzzle(EightPuzzle):
    """
    Classe de solução do 8 puzzle, usando Busca por A *
    """
    def heuristica(self, estado: tuple) -> int:
        """
        Metódo da heuristica para a busca por A *
        """
        return sum(abs(atual % 3 - objetivo % 3) + abs(atual//3 - objetivo//3)
                for atual, objetivo in ((estado.index(index), self.objetivo.index(index)) 
                             for index in range(1, 9)))

    def pegar_vizinhos(self, estado: tuple) -> list:
        """
        Metódo de pegar vizinhos para ver possíveis movimentos
        """
        vizinhos = []
        index = estado.index(0)
        movimentos = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for delta_x, delta_y in movimentos:
            eixo_x, eixo_y = index % 3 + delta_x, index // 3 + delta_y
            if 0 <= eixo_x < 3 and 0 <= eixo_y < 3:
                copia = list(estado)
                copia[index], copia[
                    eixo_x + eixo_y*3] = copia[eixo_x + eixo_y*3], copia[index]
                vizinhos.append(tuple(copia))
        return vizinhos

    def buscar(self) -> list | None:
        """
        Metódo de busca por A *
        """
        fila = [(self.heuristica(self.estado_inicial), 
                 self.estado_inicial)]
        visitado = set()
        veio_de = {self.estado_inicial: None}
        while fila:
            _, atual = heappop(fila)
            if atual == self.objetivo:
                caminho = []
                while atual is not None:
                    caminho.append(atual)
                    atual = veio_de[atual]
                caminho.reverse()
                return caminho
            visitado.add(atual)
            for vizinho in self.pegar_vizinhos(atual):
                if vizinho not in visitado:
                    heappush(fila, (self.heuristica(vizinho), vizinho))
                    veio_de[vizinho] = atual
        return None