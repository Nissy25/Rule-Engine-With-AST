from typing import List

class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (conditions)
        self.left = None       # Left child node
        self.right = None      # Right child node
        self.value = value     # Operand value (e.g., age > 30)

def combine_rules(rules: List[str]) -> Node:
    if not rules:
        raise ValueError("No rules to combine")

    # Create a new root node for the combined rule
    combined = Node("operator", "AND")

    # Parse each rule and add it as a child to the combined node
    for rule in rules:
        # Here you might need to implement your logic to parse each rule into a Node
        # For simplicity, we'll create a Node with the rule as a string
        rule_node = Node("operand", rule)  # You might want to replace this with actual parsing logic
        if not combined.left:
            combined.left = rule_node
        else:
            # If left already exists, attach it to the right as an AND operation
            combined.right = rule_node
            # Create a new AND node to chain further
            combined = Node("operator", "AND")
            combined.left = combined  # Previous combined node
            combined.right = rule_node  # Current rule

    return combined

