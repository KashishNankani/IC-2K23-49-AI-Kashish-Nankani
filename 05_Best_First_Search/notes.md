# Best First Search – Theory Notes

## What is Best First Search?

Best First Search is an **informed search algorithm** that uses a heuristic
function to decide which node to explore next. Unlike BFS and DFS which
explore nodes based on order of discovery, Best First Search always picks
the node that appears to be closest to the goal according to the heuristic.

It is called "best first" because at every step it selects the most
promising node — the one with the best heuristic value — from all the
nodes it knows about so far.

---

## What is a Heuristic?

A heuristic is an estimated value that tells us how close a given state is
to the goal. It is not always exact — it is a guess based on some
knowledge about the problem.

For example, in a map problem, the straight-line distance to the
destination is a heuristic. The actual road distance may be longer, but
it gives us a useful estimate to guide the search.

A good heuristic makes the search much faster by avoiding unnecessary paths.

---

## Key Concepts

### Open List
A priority queue that stores nodes yet to be explored, ordered by their
heuristic value. The node with the lowest heuristic (closest to goal)
is always explored first.

### Visited Set
Keeps track of nodes already explored so we don't revisit them.

### Priority Queue
We use a min-heap (via Python's `heapq`) so that the node with the
smallest heuristic value is always at the front.

---

## Algorithm Steps

1. Add the start node to the open list with its heuristic value
2. While the open list is not empty:
   - Pop the node with the lowest heuristic value
   - If it is the goal → return the path
   - Mark it as visited
   - For each unvisited neighbour → add to open list with its heuristic
3. If open list becomes empty → goal not reachable

---

## Example Trace

```
Graph:
A - B - D
|   |
C   E - G (Goal)
|
F
```

Heuristic values (estimated distance to G):

| Node | Heuristic |
|------|-----------|
| A    | 6         |
| B    | 4         |
| C    | 5         |
| D    | 3         |
| E    | 2         |
| F    | 6         |
| G    | 0         |

| Step | Visited | Open List (node, h)              |
|------|---------|----------------------------------|
| 1    | A       | (B,4), (C,5)                     |
| 2    | B       | (E,2), (D,3), (C,5)              |
| 3    | E       | (G,0), (D,3), (C,5)              |
| 4    | G ✅    | Goal reached!                    |

Path: **A → B → E → G**

---

## Properties

| Property         | Best First Search                              |
|------------------|------------------------------------------------|
| Complete         | Yes (if graph is finite)                       |
| Optimal          | No — does not guarantee shortest path          |
| Time Complexity  | O(b^m) — b = branching factor, m = max depth  |
| Space Complexity | O(b^m) — stores all nodes in open list        |

---

## Best First Search vs BFS

|                  | BFS                        | Best First Search           |
|------------------|----------------------------|-----------------------------|
| Strategy         | Uninformed                 | Informed (uses heuristic)   |
| Node Selection   | FIFO order                 | Best heuristic value        |
| Shortest Path    | Yes (unweighted)           | Not guaranteed              |
| Speed            | Slower                     | Faster with good heuristic  |

---

## Limitation

Best First Search is **greedy** — it only looks at the heuristic and
ignores the actual cost to reach a node. This can lead to suboptimal
paths. A* Search fixes this by considering both the actual cost and
the heuristic together.

---

## Real-World Applications

- **GPS Navigation** — finding a route guided by estimated distance
- **Game AI** — choosing the best move towards a goal state
- **Robot path planning** — navigating towards a target efficiently
- **Puzzle solving** — 8-puzzle, 15-puzzle problems