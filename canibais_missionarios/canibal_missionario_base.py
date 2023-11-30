"""Module base do problema dos Canibais e Missionários"""
from time import time
from memory_profiler import memory_usage

class IMissionarioCanibal:
    """
    Classe abstrada do problema de missionário e canibal
    """

    def iniciar(self) -> None: ...
    """
    Metódo de iniciar solução do problema
    """

class BaseMissionarioCanibal(IMissionarioCanibal):
    """
    Classe Base do Problema Missionário e Canibais.
    Na margem de um rio tem 3 canibais e 3 missionários, 
    eles desejam chegar do outro lado do rio, no entanto tem um barco
    que consegue apenas carregar duas pessoas por vez e não pode em nenhuma
    das margens ficar mais canibais que missionários
    """
    def __init__(self) -> "BaseMissionarioCanibal":
        self.estado_inicial = (3, 3, 1)

    @classmethod
    def new(cls: "BaseMissionarioCanibal") -> IMissionarioCanibal:
        return cls()

    def estado_valido(self, estado: tuple) -> bool: ...
    """
    Metódo abstrato de Verificar se o estado dado é válido.
    """

    def buscar(self) -> list|None: ...
    """
    Metódo abstrato de busca que será implementado pela busca especifica
    """

    def gerar_sucessores(self, estado: tuple) -> list: ...
    """
    Metódo abstrato de gerar estados sucessores para o estado dado.
    """

    def mostrar_estado(self, estado: tuple) -> None:
        """
        Mostra estado de maneira mais fácil de usuário entender
        """
        margem_esquerda = f" margem esquerda: {str(estado[0]) + ' Missionário e '}{str(estado[1]) + ' Canibal'}"
        margem_direita = f" margem direita: {str((3 - estado[0])) + ' Missionário e '}{str((3 - estado[1])) + ' Canibal'}"
        print(f"{margem_esquerda}|{margem_direita}")

    def iniciar(self) -> None:
        """
        Iniciador da busca com tudo que deve ser usado embutido
        """
        tempo_inicial = time()
        memoria_inicial = memory_usage()[0]
        solucao = self.buscar()
        tempo_execucao = time() - tempo_inicial
        memoria_usada = memory_usage()[0] - memoria_inicial
        if solucao is None:
            print("Não foi possível encontrar solução.")
        else:
            print("Solução encontrada: \n")
            for index, estado in enumerate(solucao):
                print(f"{index + 1}:")
                self.mostrar_estado(estado)
            print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
            print(f"Memória usada: {memoria_usada:.6f} MB")
