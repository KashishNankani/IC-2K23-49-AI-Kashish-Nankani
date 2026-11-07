# Water Jug Problem – Theory Notes

## What is the Water Jug Problem?

The Water Jug Problem is a classic puzzle in Artificial Intelligence used to
demonstrate state space search. We are given two jugs — Jug A and Jug B —
with fixed capacities but no measurement markings. The goal is to measure
exactly a target amount of water using only these two jugs.

For example: Jug A = 3L, Jug B = 4L, Target = 2L.

---

## Why is it an AI Problem?

In AI, problems are solved by searching through possible states until we
reach the goal. The Water Jug Problem is a perfect example of this because:
- There is a clear **initial state** (both jugs empty)
- There are defined **actions** (fill, empty, pour)
- There is a clear **goal state** (one jug contains the target amount)
- We need to find the **sequence of actions** to reach that goal

---

## Key Concepts

### State
A state is a snapshot of the current situation.
Here, a state is represented as a pair: **(amount in Jug A, amount in Jug B)**

- Initial State → (0, 0)
- Goal State → (2, ?) or (?, 2) — any state where target is reached

### Operators (Actions)
These are the moves we can make at any point:

1. Fill Jug A completely
2. Fill Jug B completely
3. Empty Jug A completely
4. Empty Jug B completely
5. Pour water from Jug A into Jug B (until A is empty or B is full)
6. Pour water from Jug B into Jug A (until B is empty or A is full)

### State Space
The state space is the collection of ALL possible states reachable from the
initial state using the above operators. BFS explores this space level by level.

---

## Algorithm Used — BFS (Breadth-First Search)

BFS is used here because it explores all states level by level, meaning it
always finds the solution with the **fewest number of steps** (optimal path).

Steps:
1. Start from (0, 0), add it to a queue
2. For each state, apply all 6 operators to generate next states
3. If a state has already been visited, skip it
4. If the goal is found, stop and print the path
5. If the queue becomes empty, no solution exists

---

## Example Trace

Jug A = 3L | Jug B = 4L | Target = 2L

| Step | Jug A | Jug B | Action      |
|------|-------|-------|-------------|
| 0    | 0     | 0     | Start       |
| 1    | 0     | 4     | Fill B      |
| 2    | 3     | 1     | Pour B → A  |
| 3    | 0     | 1     | Empty A     |
| 4    | 1     | 0     | Pour B → A  |
| 5    | 1     | 4     | Fill B      |
| 6    | 3     | 2     | Pour B → A ✅ |

Goal reached at Step 6 — Jug B contains 2L.

---

## Complexity

| | Value |
|-|-------|
| Time Complexity  | O(A × B) — total number of unique states |
| Space Complexity | O(A × B) — to store visited states |

---

## Real-World Applications

- Liquid measurement in chemistry labs
- Resource allocation problems
- Puzzle solving and planning in AI
- Demonstrates constraint-based problem solving