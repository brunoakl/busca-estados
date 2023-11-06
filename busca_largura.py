from collections import deque
import time

import psutil

class BuscaEmLargura:
    def __init__(self, problema):
        self.problema = problema

    def buscar(self):
        fila = deque()
        visitados = set()
        inicio = time.time()
        estado_inicial = self.problema.estado_inicial
        estado_inicial.parent = None
        fila.append(estado_inicial)

        while fila:
            estado_atual = fila.popleft()
            visitados.add(estado_atual)

            if self.problema.eh_objetivo(estado_atual):
                print(f"Tempo de Execução: {time.time() - inicio:.6f} segundos")
                print(f"Uso de Memória: {psutil.Process().memory_info().rss / 1024} KB")
                return self.construir_caminho(estado_atual)

            for acao in self.problema.acoes_possiveis(estado_atual):
                novo_estado = self.aplicar_acao(estado_atual, acao) 
                if novo_estado is not None and novo_estado not in visitados and novo_estado not in fila:
                    novo_estado.parent = estado_atual
                    fila.append(novo_estado)
        return None

    def aplicar_acao(self, estado, acao):
        pass

    def construir_caminho(self, estado):
        caminho = []
        while estado:
            caminho.insert(0, estado)
            estado = estado.parent
        return caminho
