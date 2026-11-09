# A* Search – Theory Notes

## What is A* Search?

A* (pronounced "A-star") is one of the most widely used and powerful
search algorithms in Artificial Intelligence. It finds the **shortest
path** from a start node to a goal node in a weighted graph by combining
two things:

- **g(n)** — the actual cost to reach the current node from the start
- **h(n)** — a heuristic estimate of the cost from the current node to the goal

The total score for each node is:

```
f(n) = g(n) + h(n)
```

A* always expands the node with the lowest f value, making it both
**optimal** and **efficient**.

---

## Why is A* Better than Best First Search?

Best First Search only uses h(n) — the heuristic. It is greedy and
can take a path that looks close to the goal but has a very high
actual cost.

A* uses f(n) = g(n) + h(n), so it balances both the cost already
paid and the estimated remaining cost. This guarantees the optimal
(shortest / cheapest) path as long as the heuristic is **admissible**.

---

## Key Concepts

### g(n) — Actual Cost
The total cost of the path from the start node to the current node.
This is calculated as we travel through the graph.

### h(n) — Heuristic
An estimate of how far the current node is from the goal.
Must be **admissible** — meaning it never overestimates the true cost.

### f(n) — Total Score
f(n) = g(n) + h(n)
This is the value used to prioritise which node to explore next.

### Admissible Heuristic
A heuristic is admissible if it never overestimates the actual cost
to reach the goal. For example, straight-line distance is admissible
because the actual road distance is always equal to or more than it.

### Open List
A priority queue of nodes to be explored, ordered by f(n).

### Visited / Closed Set
Nodes already explored with their best known g cost, so we don't
reprocess them unnecessarily.

---

## Algorithm Steps

1. Add start node to open list with f = h(start), g = 0
2. While open list is not empty:
   - Pop the node with the lowest f value
   - If it is the goal → return the path and cost
   - Mark it visited with its g cost
   - For each neighbour:
     - Calculate new_g = current g + edge weight
     - Calculate new_f = new_g + h(neighbour)
     - Add to open list if not yet visited
3. If open list is empty → no path exists

---

## Example Trace

Weighted graph with heuristic values to goal G:

| Node | h(n) |
|------|------|
| A    | 7    |
| B    | 6    |
| C    | 8    |
| D    | 4    |
| E    | 2    |
| F    | 9    |
| G    | 0    |

Edge weights: A→B=1, A→C=4, B→D=2, B→E=5, C→F=3, E→G=2

| Step | Node | g | h | f  | Action                    |
|------|------|---|---|----|---------------------------|
| 1    | A    | 0 | 7 | 7  | Start                     |
| 2    | B    | 1 | 6 | 7  | A→B cost 1                |
| 3    | E    | 6 | 2 | 8  | B→E cost 5, total g=6     |
| 4    | G    | 8 | 0 | 8  | E→G cost 2, total g=8 ✅  |

Path: **A → B → E → G** | Total cost: **8**

---

## Properties

| Property         | A* Search                                      |
|------------------|------------------------------------------------|
| Complete         | Yes — always finds a solution if one exists    |
| Optimal          | Yes — with an admissible heuristic             |
| Time Complexity  | O(b^d) — b = branching factor, d = depth      |
| Space Complexity | O(b^d) — stores all nodes in open list        |

---

## Comparison with Other Algorithms

|                  | BFS        | Best First Search | A* Search          |
|------------------|------------|-------------------|--------------------|
| Uses cost g(n)   | No         | No                | Yes                |
| Uses heuristic   | No         | Yes               | Yes                |
| Optimal          | Yes (unweighted) | No          | Yes                |
| Speed            | Slow       | Fast              | Fast + Optimal     |

---

## Real-World Applications

- **Google Maps / GPS** — finding the shortest driving route
- **Game AI** — pathfinding for characters in games (Pac-Man, RPGs)
- **Robotics** — robot navigation and motion planning
- **Network routing** — finding the least-cost path in a network
- **Puzzle solving** — 8-puzzle, 15-puzzle with Manhattan distance heuristic