from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))  # (jug_a, jug_b, path)

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:
            print("Solution found!")
            for step, state in enumerate(path):
                print(f"Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L")
            return

        # All possible operations
        next_states = [
            (capacity_a, b),           # Fill A
            (a, capacity_b),           # Fill B
            (0, b),                    # Empty A
            (a, 0),                    # Empty B
            (max(0, a + b - capacity_b), min(capacity_b, a + b)),  # Pour A -> B
            (min(capacity_a, a + b), max(0, a + b - capacity_a)),  # Pour B -> A
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution found.")


# --- Run ---
capacity_a = 3   # Jug A capacity
capacity_b = 4   # Jug B capacity
target = 2       # Target amount

print(f"Jugs: A={capacity_a}L, B={capacity_b}L | Target: {target}L\n")
water_jug_bfs(capacity_a, capacity_b, target)