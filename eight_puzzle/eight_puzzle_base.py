"""Module base do problema do Eight Puzzle"""
from time import time
from memory_profiler import memory_usage

class IEightPuzzle:
    """
    Classe abstrata do problema do 8 puzzle
    """

    def iniciar(self) -> None: ...
    """
    Metódo de iniciar a solução do problema do 8 puzzle
    """

class EightPuzzle(IEightPuzzle):
    """
    Classe base do problema do 8 puzzle, uma grade de 3x3, onde cada quadrado é
    número exceto por um que é faltando, com ele você consegue mover os outros
    quadrados e ordenadar ou desordenar, o objetivo dele é no final esteja ordenado:
    1 2 3
    4 5 6
    7 8 0
    """
    def __init__(self, inicio: list) -> None:
        self.estado_inicial = inicio
        self.objetivo = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    @classmethod
    def new(cls: "EightPuzzle", inicio: list) -> IEightPuzzle:
        return cls(inicio)

    def pegar_vizinhos(self, estado) -> list|dict: ...
    """
    Metódo abstrato de pegar vizinhos pela busca
    """

    def buscar(self) -> list|None: ...
    """
    Metódo abstrato de busca para o problema
    """

    def mostrar_estado(self, estado: tuple) -> None:
        """
        Metódo de mostrar estado do 8-puzzle
        """
        print(f"{estado[0]} {estado[1]} {estado[2]}")
        print(f"{estado[3]} {estado[4]} {estado[5]}")
        print(f"{estado[6]} {estado[7]} {estado[8]}")
        print()

    def iniciar(self) -> None:
        """
        Metódo de iniciar solução do 8 puzzle
        """
        tempo_inicial = time()
        memoria_inicial = memory_usage()[0]
        solucao = self.buscar()
        tempo_execucao = time() - tempo_inicial
        memoria_usada = memory_usage()[0] - memoria_inicial
        if solucao is None:
            print("Sem solução encontrada.")
        else:
            self.mostrar_estado(self.estado_inicial)
            print("Solução:")
            for index, estado in enumerate(solucao):
                print(f"{index + 1}")
                self.mostrar_estado(estado)
            
            print(f"Tempo de execução: {tempo_execucao}")
            print(f"Uso de memória: {memoria_usada:.6f} MB")