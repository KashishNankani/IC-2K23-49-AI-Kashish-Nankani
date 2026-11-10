# ── Knowledge Representation in AI ──────────────────────────────────────────
# Two approaches demonstrated:
# 1. Rule-Based System (Production Rules / IF-THEN)
# 2. Semantic Network (using a dictionary graph)

# ════════════════════════════════════════════════════════════════════════════
# PART 1 — Rule-Based System (Medical Diagnosis Expert System)
# ════════════════════════════════════════════════════════════════════════════

class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = [
            {
                'conditions': ['fever', 'cough', 'sore_throat'],
                'conclusion': 'flu',
                'explanation': 'Patient likely has the flu.'
            },
            {
                'conditions': ['fever', 'headache', 'rash'],
                'conclusion': 'measles',
                'explanation': 'Patient may have measles.'
            },
            {
                'conditions': ['cough', 'shortness_of_breath', 'chest_pain'],
                'conclusion': 'pneumonia',
                'explanation': 'Patient may have pneumonia.'
            },
            {
                'conditions': ['fever', 'body_ache', 'fatigue'],
                'conclusion': 'covid',
                'explanation': 'Patient may have COVID-19.'
            },
        ]

    def add_fact(self, fact):
        self.facts.add(fact)

    def diagnose(self):
        print("\n--- Rule-Based Diagnosis System ---")
        print(f"Symptoms entered: {', '.join(self.facts)}\n")
        diagnosed = False
        for rule in self.rules:
            if all(cond in self.facts for cond in rule['conditions']):
                print(f"Rule matched: {rule['conditions']}")
                print(f"Diagnosis: {rule['conclusion'].upper()}")
                print(f"Explanation: {rule['explanation']}\n")
                diagnosed = True
        if not diagnosed:
            print("No diagnosis found. Please consult a doctor.\n")


# Run Rule-Based System
rbs = RuleBasedSystem()
rbs.add_fact('fever')
rbs.add_fact('cough')
rbs.add_fact('sore_throat')
rbs.diagnose()


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — Semantic Network
# ════════════════════════════════════════════════════════════════════════════

class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_node(self, node):
        if node not in self.network:
            self.network[node] = []

    def add_relation(self, subject, relation, obj):
        self.add_node(subject)
        self.add_node(obj)
        self.network[subject].append((relation, obj))

    def query(self, subject):
        print(f"\nRelations for '{subject}':")
        if subject in self.network and self.network[subject]:
            for relation, obj in self.network[subject]:
                print(f"  {subject}  --[{relation}]-->  {obj}")
        else:
            print(f"  No relations found for '{subject}'")

    def display_all(self):
        print("\n--- Full Semantic Network ---")
        for node, relations in self.network.items():
            for relation, obj in relations:
                print(f"  {node}  --[{relation}]-->  {obj}")


# Build a Semantic Network about animals
sn = SemanticNetwork()

sn.add_relation('Dog',    'is-a',       'Animal')
sn.add_relation('Cat',    'is-a',       'Animal')
sn.add_relation('Animal', 'has',        'Life')
sn.add_relation('Dog',    'has',        'Fur')
sn.add_relation('Dog',    'can',        'Bark')
sn.add_relation('Dog',    'eats',       'Meat')
sn.add_relation('Cat',    'can',        'Meow')
sn.add_relation('Cat',    'has',        'Whiskers')
sn.add_relation('Bird',   'is-a',       'Animal')
sn.add_relation('Bird',   'can',        'Fly')
sn.add_relation('Bird',   'has',        'Wings')
sn.add_relation('Parrot', 'is-a',       'Bird')
sn.add_relation('Parrot', 'can',        'Talk')

sn.display_all()
sn.query('Dog')
sn.query('Parrot')