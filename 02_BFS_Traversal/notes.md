# BFS Graph Traversal – Theory Notes

## What is BFS?

Breadth-First Search (BFS) is a graph traversal algorithm that starts at a
given source node and explores all its neighbours first before moving on to
nodes at the next level. It visits nodes layer by layer, which is why it is
also called Level-Order Traversal.

BFS is one of the most fundamental algorithms in Artificial Intelligence and
is used as the base for many advanced search techniques.

---

## Why is BFS Important in AI?

In AI, search algorithms are used to explore a problem space to find a
solution. BFS is an **uninformed (blind) search** strategy, meaning it has
no knowledge about how close it is to the goal — it simply explores
everything level by level.

It guarantees finding the **shortest path** in an unweighted graph, which
makes it very useful when the cost of each step is equal.

---

## Key Concepts

### Graph
A graph is a collection of nodes (also called vertices) connected by edges.
It can be directed, undirected, weighted, or unweighted.
BFS works on all of these.

### Adjacency List
We represent the graph using an adjacency list — a dictionary where each
node maps to a list of its neighbours:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
```

### Visited Set
To avoid visiting the same node twice and getting stuck in cycles, we
maintain a visited set. Once a node is added to the queue, it is marked
visited immediately.

---

## Algorithm Steps

1. Start at the source node, mark it as visited
2. Add it to a queue (FIFO — First In First Out)
3. While the queue is not empty:
   - Remove the front node from the queue
   - Add it to the traversal result
   - For each unvisited neighbour — mark visited and enqueue it
4. Repeat until queue is empty

---

## Data Structure Used

BFS uses a **Queue (FIFO)** — nodes enter from the back and leave from the front.
In Python we use `collections.deque` for efficient queue operations.

---

## Example Trace

```
Graph:
    A
   / \
  B   C
 / \   \
D   E - F
```

BFS from A:

| Step | Queue      | Action                        |
|------|------------|-------------------------------|
| 1    | [A]        | Start, enqueue A              |
| 2    | [B, C]     | Visit A, enqueue B and C      |
| 3    | [C, D, E]  | Visit B, enqueue D and E      |
| 4    | [D, E, F]  | Visit C, enqueue F            |
| 5    | [E, F]     | Visit D (no new neighbours)   |
| 6    | [F]        | Visit E (F already queued)    |
| 7    | []         | Visit F, queue empty — done   |

Final Order: **A → B → C → D → E → F**

---

## Properties of BFS

| Property         | BFS                                        |
|------------------|--------------------------------------------|
| Complete         | Yes — always finds solution if one exists  |
| Optimal          | Yes — shortest path in unweighted graphs   |
| Time Complexity  | O(V + E) — V = vertices, E = edges        |
| Space Complexity | O(V) — stores all nodes in queue           |

---

## BFS vs DFS

|                | BFS                        | DFS                    |
|----------------|----------------------------|------------------------|
| Order          | Level by level             | Branch by branch       |
| Data Structure | Queue                      | Stack                  |
| Shortest Path  | Yes                        | Not guaranteed         |
| Memory Usage   | More (stores whole level)  | Less                   |
| Best For       | Shortest path problems     | Exploring all paths    |

---

## Real-World Applications

- **Google Maps / GPS** — finding shortest route between two locations
- **Social Networks** — friend suggestions within N connections
- **Web Crawlers** — exploring web pages level by level
- **Puzzle Solving** — solving mazes, sliding puzzles, Water Jug Problem