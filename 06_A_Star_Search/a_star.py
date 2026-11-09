import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f = g + h, node, g_cost, path)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start, 0, [start]))

    visited = {}  # node: best g_cost seen

    print(f"Start: {start} | Goal: {goal}")
    print("-" * 40)

    while open_list:
        f, node, g, path = heapq.heappop(open_list)

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        h = heuristic[node]
        print(f"Visiting: {node} | g={g} | h={h} | f={f}")

        if node == goal:
            print("-" * 40)
            print(f"Goal reached!")
            print(f"Path: {' -> '.join(path)}")
            print(f"Total cost: {g}")
            return path

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_g = g + weight
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(open_list, (new_f, neighbour, new_g, path + [neighbour]))

    print("Goal not reachable.")
    return None


# --- Weighted graph (adjacency list with costs) ---
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 3)],
    'G': []
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 8,
    'D': 4,
    'E': 2,
    'F': 9,
    'G': 0
}

a_star(graph, heuristic, start='A', goal='G')