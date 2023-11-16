import heapq

def heuristic(state, goal):
    return sum(abs(b % 3 - g % 3) + abs(b//3 - g//3)
               for b, g in ((state.index(i), goal.index(i)) for i in range(1, 9)))

def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for dx, dy in moves:
        x, y = i % 3 + dx, i // 3 + dy
        if 0 <= x < 3 and 0 <= y < 3:
            copy = list(state)
            copy[i], copy[x + y*3] = copy[x + y*3], copy[i]
            neighbors.append(tuple(copy))
    return neighbors

def a_star(start, goal):
    queue = [(heuristic(start, goal), start)]
    visited = set()
    came_from = {start: None}
    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current
    return None

start_state = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)

path = a_star(start_state, goal_state)
print(f"[{start_state[0]} {start_state[1]} {start_state[2]}]")
print(f"[{start_state[3]} {start_state[4]} {start_state[5]}]")
print(f"[{start_state[6]} {start_state[7]} {start_state[8]}]")
if path:
    print("Solution path:")
    for i, state in enumerate(path):
        print(f"{i+1}.")
        print(f"[{state[0]} {state[1]} {state[2]}]")
        print(f"[{state[3]} {state[4]} {state[5]}]")
        print(f"[{state[6]} {state[7]} {state[8]}]")
else:
    print("No solution.")