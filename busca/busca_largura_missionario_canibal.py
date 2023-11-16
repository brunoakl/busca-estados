from collections import deque
import faulthandler
import time
from memory_profiler import memory_usage

def busca_largura(inicio, objetivo, validar_estado, verbose=False):
    fila = deque([inicio])
    visitados = set([inicio])
    passos = [inicio]
    # Inicializa as variáveis de tempo e memória
    start_time = time.time()
    mem_usage = memory_usage()[0]
    
    while fila:
        estado_atual = fila.popleft()
        if estado_atual == objetivo:
            end_time = time.time()
            mem_usage = memory_usage()[0] - mem_usage
            print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
            print(f"Memória usada: {mem_usage:.6f} MB")
            return passos
        for proximo_estado in gerar_estados_sucessores(estado_atual):
            if proximo_estado not in visitados and validar_estado(proximo_estado):
                visitados.add(proximo_estado)
                fila.append(proximo_estado)
                passos.append(proximo_estado)
                if verbose:
                    print(proximo_estado)
    return None

def gerar_estados_sucessores(estado_atual):
    barco = estado_atual[2]
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                novo_estado = (estado_atual[0] - m * estado_atual[2], estado_atual[1] - c * estado_atual[2], -barco)
                if 0 <= novo_estado[0] <= 3 and 0 <= novo_estado[1] <= 3:
                    yield novo_estado

def validar_estado(estado):
    if estado[0] > 0 and estado[0] < estado[1]:
        return False
    if estado[0] < 3 and estado[0] > estado[1]:
        return False
    return True

def print_estado(estado):
    margem_esquerda = f" margem esquerda: {str(estado[0]) + ' Missionário e '}{str(estado[1]) + ' Canibal'}"
    margem_direita = f" margem direita: {str((3 - estado[0])) + ' Missionário e '}{str((3 - estado[1])) + ' Canibal'}"
    barco = "Barco" if estado[2] == 1 else "      "
    print(f"{margem_esquerda}|{margem_direita}")

inicio = (3, 3, 1)
objetivo = (0, 0, -1)
passos = busca_largura(inicio, objetivo, validar_estado, verbose=False)
if passos is None:
    print("Não foi possível encontrar uma solução.")
else:
    print("Solução encontrada:")
    for i, estado in enumerate(passos):
        print(f"{i+1}.")
        print_estado(estado)
