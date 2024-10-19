from app.models.ast import Node

def create_rule(rule_string):
    if "age > 30" in rule_string and "salary > 50000" in rule_string:
        root = Node("operator", "AND")
        root.left = Node("operand", ("age", ">", 30))
        root.right = Node("operand", ("salary", ">", 50000))
    else:
        raise ValueError("Invalid rule format")
    return root

def combine_rules(rules):
    combined = rules[0]
    for rule in rules[1:]:
        new_node = Node("operator", "AND")
        new_node.left = combined
        new_node.right = rule
        combined = new_node
    return combined

def evaluate_rule(root, data):
    if root.type == "operand":
        variable, operator, value = root.value
        if operator == ">":
            return data[variable] > value
        elif operator == "<":
            return data[variable] < value
        elif operator == "==":
            return data[variable] == value
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    elif root.type == "operator":
        if root.value == "AND":
            return evaluate_rule(root.left, data) and evaluate_rule(root.right, data)
        elif root.value == "OR":
            return evaluate_rule(root.left, data) or evaluate_rule(root.right, data)
