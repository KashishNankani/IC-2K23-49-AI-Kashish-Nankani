import heapq

def best_first_search(graph, heuristic, start, goal):
    # Priority queue: (heuristic_value, node)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    path = []

    print(f"Start: {start} | Goal: {goal}")
    print("-" * 40)

    while open_list:
        cost, node = heapq.heappop(open_list)

        if node in visited:
            continue

        visited.add(node)
        path.append(node)
        print(f"Visiting: {node} | Heuristic: {cost}")

        if node == goal:
            print("-" * 40)
            print(f"Goal reached!")
            print(f"Path: {' -> '.join(path)}")
            return path

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(open_list, (heuristic[neighbour], neighbour))

    print("Goal not reachable.")
    return None


# --- Graph (adjacency list) ---
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': []
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 6,
    'G': 0
}

best_first_search(graph, heuristic, start='A', goal='G')