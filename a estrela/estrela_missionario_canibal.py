import heapq
import time
from memory_profiler import memory_usage

def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m < c and m > 0:  # Mais canibais que missionários
        return False
    if (3 - m) < (3 - c) and (3 - m) > 0:
        return False
    return True

def successors(state):
    m, c, b = state
    s = []
    for dm, dc in [(0, 1), (1, 0), (1, 1), (0, 2), (2, 0)]:
        new_state = (m + dm * (1 - 2 * b), c + dc * (1 - 2 * b), 1 - b)
        if is_valid(new_state):
            s.append(new_state)
    return s

def heuristic(state):
    m, c, b = state
    return m + c - b  # Subtrair b para considerar a posição do barco

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def a_star(start, goal):
    frontier = [(heuristic(start), start)]
    came_from = {}
    explored = set()
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            return reconstruct_path(came_from, current)
        explored.add(current)
        for node in successors(current):
            if node not in explored and node not in came_from:
                came_from[node] = current
                heapq.heappush(frontier, (heuristic(node), node))
    return None

def print_estado(estado):
    margem_esquerda = f" margem esquerda: {str(estado[0]) + ' Missionário e '}{str(estado[1]) + ' Canibal'}"
    margem_direita = f" margem direita: {str((3 - estado[0])) + ' Missionário e '}{str((3 - estado[1])) + ' Canibal'}"
    barco = "Barco" if estado[2] == 1 else "      "
    print(f"{margem_esquerda}|{margem_direita}")

start_state = (3, 3, 1)
goal_state = (0, 0, 0)

start_time = time.time()
mem_usage = memory_usage()[0]
path = a_star(start_state, goal_state)
print(f"Tempo de execução: {time.time() - start_time:.6f} segundos")
print(f"Memória usada: {memory_usage()[0] - mem_usage:.6f} MB")

if path:
    print("Solution path:")
    for i, state in enumerate(path):
        print(f"{i+1}.")
        print_estado(state)
else:
    print("No solution.")
