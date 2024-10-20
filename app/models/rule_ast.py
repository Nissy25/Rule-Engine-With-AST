from typing import List

class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (conditions)
        self.left = None       # Left child node
        self.right = None      # Right child node
        self.value = value     # Operand value (e.g., age > 30)

def combine_rules(rules: List[Node]) -> Node:
    if not rules:
        raise ValueError("No rules to combine")

    # Initialize the combined node as the first rule
    combined = rules[0]
    
    # Combine all rules using the AND operator
    for rule in rules[1:]:
        new_combined = Node("operator", "AND")  # Create a new AND node
        new_combined.left = combined             # Previous combined rule
        new_combined.right = rule                 # Current rule
        combined = new_combined                   # Update combined rule
    
    return combined
