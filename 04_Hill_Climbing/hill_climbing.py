import random

def hill_climbing(problem, max_iterations=1000):
    # Start with a random solution
    current = problem['initial_state']
    current_score = problem['evaluate'](current)

    print(f"Starting state: {current} | Score: {current_score}")
    print("-" * 40)

    for i in range(max_iterations):
        neighbours = problem['get_neighbours'](current)

        if not neighbours:
            print("No neighbours found. Stopping.")
            break

        # Find the best neighbour
        best_neighbour = max(neighbours, key=problem['evaluate'])
        best_score = problem['evaluate'](best_neighbour)

        # If no neighbour is better, we are at a peak — stop
        if best_score <= current_score:
            print(f"Local maximum reached at iteration {i + 1}")
            break

        # Move to the better neighbour
        current = best_neighbour
        current_score = best_score
        print(f"Iteration {i + 1}: Moved to {current} | Score: {current_score}")

    print("-" * 40)
    print(f"Final state: {current} | Final Score: {current_score}")
    return current


# --- Problem: Find the number closest to a target in a range ---
TARGET = 25

def evaluate(state):
    # Higher score = closer to target (we want to maximise this)
    return -abs(state - TARGET)

def get_neighbours(state):
    # Neighbours are the numbers just above and below current state
    return [state - 1, state + 1]

problem = {
    'initial_state': random.randint(0, 50),
    'evaluate': evaluate,
    'get_neighbours': get_neighbours
}

hill_climbing(problem)