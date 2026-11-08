# DFS Graph Traversal – Theory Notes

## What is DFS?

Depth-First Search (DFS) is a graph traversal algorithm that starts at a
source node and explores as far as possible along each branch before
backtracking. Unlike BFS which goes level by level, DFS goes deep into
one path first, then comes back and tries another path.

It is one of the most important algorithms in Artificial Intelligence and
computer science, used in everything from maze solving to topological sorting.

---

## Why is DFS Important in AI?

DFS is an **uninformed (blind) search** strategy just like BFS, but with a
different exploration style. It is preferred when:
- The solution is known to be deep in the search tree
- Memory is limited (DFS uses less memory than BFS)
- We want to explore all possible paths (like in puzzles or games)

---

## Key Concepts

### Recursion
DFS is naturally implemented using **recursion**. Each function call goes
deeper into the graph, and when it hits a dead end, it backtracks
automatically as the call stack unwinds.

### Visited Set
Just like BFS, we maintain a visited set to avoid revisiting nodes and
getting stuck in infinite loops (cycles).

### Call Stack
DFS uses the **call stack** (via recursion) instead of an explicit queue.
This is what makes it explore depth first — the most recently discovered
node is explored next.

---

## Algorithm Steps

1. Start at the source node, mark it as visited
2. Print / process the node
3. For each unvisited neighbour of the current node:
   - Recursively call DFS on that neighbour
4. When no unvisited neighbours remain, backtrack
5. Repeat until all reachable nodes are visited

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

DFS from A:

| Step | Current Node | Action                          |
|------|--------------|---------------------------------|
| 1    | A            | Visit A, go to neighbour B      |
| 2    | B            | Visit B, go to neighbour D      |
| 3    | D            | Visit D, no unvisited neighbours — backtrack |
| 4    | B            | Go to next neighbour E          |
| 5    | E            | Visit E, go to neighbour F      |
| 6    | F            | Visit F, go to neighbour C      |
| 7    | C            | Visit C, no unvisited neighbours — backtrack |
| 8    | —            | All nodes visited, done         |

Final Order: **A → B → D → E → F → C**

---

## Properties of DFS

| Property         | DFS                                            |
|------------------|------------------------------------------------|
| Complete         | Yes (for finite graphs)                        |
| Optimal          | No — does not guarantee shortest path          |
| Time Complexity  | O(V + E) — V = vertices, E = edges            |
| Space Complexity | O(V) — for the recursion call stack            |

---

## BFS vs DFS — When to Use Which?

|                | BFS                        | DFS                         |
|----------------|----------------------------|-----------------------------|
| Order          | Level by level             | Branch by branch (deep)     |
| Data Structure | Queue                      | Stack / Recursion           |
| Shortest Path  | Yes                        | Not guaranteed              |
| Memory Usage   | More                       | Less                        |
| Best For       | Shortest path, level order | Full path exploration, mazes|

---

## Real-World Applications

- **Maze solving** — explores one path fully before trying another
- **Topological sorting** — ordering tasks by dependencies
- **Cycle detection** — detecting loops in a graph
- **Web crawlers** — following one link chain deeply
- **Game trees** — exploring all possible moves in chess or tic-tac-toe