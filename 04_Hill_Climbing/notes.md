# Hill Climbing – Theory Notes

## What is Hill Climbing?

Hill Climbing is a **heuristic search algorithm** used in Artificial
Intelligence to find a good solution to an optimisation problem. It starts
from an initial state and repeatedly moves to the neighbouring state that
improves the current solution, just like climbing a hill by always stepping
upward.

The algorithm keeps moving in the direction of increasing value (or
decreasing cost) until it reaches a point where no neighbour is better
than the current state — this is called a **local maximum**.

---

## Why is it Called Hill Climbing?

Imagine you are standing on a hilly landscape and you want to reach the
highest peak. You cannot see the whole landscape — you can only see what
is immediately around you. So your strategy is simple: always take a step
in the direction that goes uphill. You stop when every direction around
you is downhill.

This is exactly what the algorithm does in a solution space.

---

## Key Concepts

### State
The current solution or position in the search space.

### Heuristic / Evaluation Function
A function that scores how good a state is. The algorithm always tries
to maximise this score (or minimise cost, depending on the problem).

### Neighbour
A state that is one small change away from the current state.
For example, if the current state is 10, neighbours could be 9 and 11.

### Local Maximum
A state that is better than all its neighbours but may not be the
globally best solution. Hill Climbing often gets stuck here.

### Global Maximum
The actual best solution in the entire search space. Hill Climbing
does not always find this.

---

## Algorithm Steps

1. Start with an initial state (can be random)
2. Evaluate the current state using the heuristic function
3. Generate all neighbouring states
4. Find the best neighbour
5. If the best neighbour is better than current → move to it
6. If no neighbour is better → stop (local maximum reached)
7. Return the current state as the solution

---

## Example Trace

Problem: Find the number closest to target = 25, starting from 18

| Iteration | Current | Score (−|x−25|) | Best Neighbour | Neighbour Score |
|-----------|---------|-----------------|----------------|-----------------|
| Start     | 18      | −7              | 19             | −6              |
| 1         | 19      | −6              | 20             | −5              |
| 2         | 20      | −5              | 21             | −4              |
| ...       | ...     | ...             | ...            | ...             |
| 7         | 25      | 0               | 24 or 26       | −1              |

Stops at 25 — no neighbour has a better (higher) score. ✅

---

## Problems with Hill Climbing

### 1. Local Maximum
Gets stuck at a point that is better than its neighbours but not the
best overall solution.

### 2. Plateau
A flat region where all neighbours have the same score. The algorithm
doesn't know which direction to move.

### 3. Ridge
A narrow peak where neighbours on either side are worse, but the actual
path to the global maximum goes diagonally — hard for simple hill climbing.

---

## Variants of Hill Climbing

| Variant | Description |
|---------|-------------|
| Simple Hill Climbing | Move to the first neighbour that is better |
| Steepest Ascent | Evaluate all neighbours, move to the best one |
| Random Restart | Restart from a new random state if stuck |
| Stochastic | Pick a random uphill neighbour instead of the best |

Our implementation uses **Steepest Ascent** — we evaluate all neighbours
and always pick the best one.

---

## Properties

| Property         | Hill Climbing                               |
|------------------|---------------------------------------------|
| Complete         | No — can get stuck at local maxima          |
| Optimal          | No — not guaranteed to find best solution   |
| Time Complexity  | Depends on the problem and landscape        |
| Space Complexity | O(1) — only stores current state            |

---

## Real-World Applications

- **N-Queens Problem** — placing N queens on a board with no conflicts
- **Travelling Salesman Problem** — finding a short route between cities
- **Neural Network Training** — gradient descent is a form of hill climbing
- **Game Playing** — finding the best move in a given board state
- **Scheduling** — optimising task assignment and timetables