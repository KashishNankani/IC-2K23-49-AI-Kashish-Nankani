# Knowledge Representation – Theory Notes

## What is Knowledge Representation?

Knowledge Representation (KR) is a field in Artificial Intelligence that
deals with how to formally encode information about the world so that a
computer can reason with it, draw conclusions, and make decisions.

For an AI system to behave intelligently, it needs to know things — facts
about the world, relationships between objects, rules, and logic. KR is
the method of storing this knowledge in a structured and usable way.

---

## Why is Knowledge Representation Important?

Without knowledge, an AI is just a set of blind rules or random guesses.
Knowledge representation allows an AI to:

- Store facts about the world (a dog is an animal)
- Understand relationships (a parrot is a bird, birds can fly)
- Apply rules to draw new conclusions (if a patient has fever and cough → flu)
- Explain decisions (why did it give this diagnosis?)

---

## Types of Knowledge

| Type | Description | Example |
|------|-------------|---------|
| Declarative | Facts about the world | "A dog is an animal" |
| Procedural | How to do something | Steps to solve a problem |
| Heuristic | Rules of thumb from experience | "If fever and cough → possible flu" |
| Meta | Knowledge about knowledge | "I know that dogs are animals" |

---

## Techniques Used in This Lab

### 1. Rule-Based System (Production Rules)

A rule-based system stores knowledge as a set of **IF-THEN rules**:

```
IF <conditions are true> THEN <conclusion>
```

It has three components:
- **Knowledge Base** — a collection of IF-THEN rules
- **Working Memory (Facts)** — the current known facts
- **Inference Engine** — checks which rules match the facts and fires them

#### Example — Medical Diagnosis:
```
IF fever AND cough AND sore_throat THEN diagnosis = flu
IF fever AND headache AND rash     THEN diagnosis = measles
```

The system takes a patient's symptoms as facts, matches them against
rules, and produces a diagnosis. This is how early expert systems like
MYCIN worked.

#### Advantages
- Easy to understand and explain
- Can encode expert knowledge directly
- Transparent — you can see exactly why a decision was made

#### Limitations
- Cannot handle uncertainty well
- Rules must be manually written
- Breaks down with too many rules (rule explosion)

---

### 2. Semantic Network

A semantic network is a **graph-based** knowledge representation where:
- **Nodes** represent objects, concepts, or entities
- **Edges (links)** represent relationships between them

Common relationships used:
- `is-a` → inheritance (Parrot is-a Bird)
- `has` → properties (Dog has Fur)
- `can` → capabilities (Bird can Fly)
- `part-of` → composition (Wheel part-of Car)

#### Example Network:
```
Parrot --[is-a]--> Bird --[is-a]--> Animal
Bird   --[can]---> Fly
Dog    --[has]---> Fur
Dog    --[can]---> Bark
```

#### Property Inheritance
One key benefit is **inheritance** — if Parrot is-a Bird, and Bird can Fly,
then we can infer that Parrot can also Fly without stating it explicitly.

#### Advantages
- Very intuitive and visual
- Supports inheritance and reasoning
- Good for representing hierarchies and relationships

#### Limitations
- Not suited for complex logical reasoning
- No standard for handling exceptions
- Can become very large for real-world knowledge

---

## Comparison

| Feature | Rule-Based System | Semantic Network |
|---------|-------------------|------------------|
| Structure | IF-THEN rules | Graph of nodes and edges |
| Best For | Decision making, diagnosis | Relationships, hierarchies |
| Reasoning | Forward / Backward chaining | Inheritance, traversal |
| Transparency | High | High |
| Complexity | Grows with more rules | Grows with more nodes |

---

## Other KR Techniques (not coded here)

- **Frames** — structured records like objects in OOP
- **Logic (Predicate Calculus)** — formal mathematical reasoning
- **Ontologies** — large-scale formal knowledge bases (used in the web)
- **Bayesian Networks** — probabilistic knowledge representation

---

## Real-World Applications

- **Medical Expert Systems** — MYCIN (antibiotic prescriptions)
- **Search Engines** — Google's Knowledge Graph
- **Natural Language Processing** — understanding word relationships
- **Chatbots** — storing and retrieving facts to answer questions
- **Autonomous Systems** — representing the world for a robot to reason about