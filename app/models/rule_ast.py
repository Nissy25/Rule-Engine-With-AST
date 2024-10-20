from typing import List

class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type
        self.left = None
        self.right = None
        self.value = value

def combine_rules(rules: List[str]) -> Node:
    if not rules:
        raise ValueError("No rules to combine")

    combined = Node("operator", "AND")

    # Combine the rules into the AST
    for rule in rules:
        rule_node = Node("operand", rule)
        if not combined.left:
            combined.left = rule_node
        else:
            combined.right = rule_node
            # Create a new AND node to chain further if needed
            combined = Node("operator", "AND")
            combined.left = combined  # Previous combined node
            combined.right = rule_node  # Current rule

    return combined
