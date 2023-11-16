from collections import deque
import time
from memory_profiler import memory_usage

# Define o estado objetivo do quebra-cabeça
objetivo = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define as posições dos movimentos possíveis
movimentos = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def busca_largura(inicio):
    # Inicializa a fila com o estado inicial
    fila = deque([(inicio, [])])
    # Inicializa o conjunto de estados visitados
    visitados = set([inicio])
    # Inicializa as variáveis de tempo e memória
    start_time = time.time()
    mem_usage = memory_usage()[0]
    
    # Enquanto a fila não estiver vazia
    while fila:
        # Remove o primeiro estado da fila
        estado_atual, caminho_atual = fila.popleft()
        
        # Se o estado atual é o objetivo, retorna o caminho até ele
        if estado_atual == objetivo:
            end_time = time.time()
            mem_usage = memory_usage()[0] - mem_usage
            print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
            print(f"Memória usada: {mem_usage:.6f} MB")
            return caminho_atual
        
        # Para cada movimento possível a partir do estado atual
        for movimento in movimentos[estado_atual.index(0)]:
            # Cria uma cópia do estado atual
            novo_estado = list(estado_atual)
            # Realiza o movimento
            novo_estado[movimento], novo_estado[estado_atual.index(0)] = novo_estado[estado_atual.index(0)], novo_estado[movimento]
            novo_estado = tuple(novo_estado)
            
            # Se o novo estado ainda não foi visitado
            if novo_estado not in visitados:
                # Adiciona o novo estado à fila e ao conjunto de visitados
                fila.append((novo_estado, caminho_atual + [novo_estado]))
                visitados.add(novo_estado)
    
    # Se não encontrou o objetivo, retorna None
    return None

# Define o estado inicial do quebra-cabeça
inicio = (7, 2, 4, 5, 0, 6, 8, 3, 1)
print(f"{inicio[0]} {inicio[1]} {inicio[2]}")
print(f"{inicio[3]} {inicio[4]} {inicio[5]}")
print(f"{inicio[6]} {inicio[7]} {inicio[8]}")
print()
# Chama a função de busca em largura
caminho = busca_largura(inicio)

# Imprime o passo a passo da solução
if caminho is None:
    print("Não foi possível encontrar uma solução.")
else:
    print("Solução encontrada:")
    for i, estado in enumerate(caminho):
        print(f"Passo {i}:")
        print(f"{estado[0]} {estado[1]} {estado[2]}")
        print(f"{estado[3]} {estado[4]} {estado[5]}")
        print(f"{estado[6]} {estado[7]} {estado[8]}")
        print()