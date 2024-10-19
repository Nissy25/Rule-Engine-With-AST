class Node:
    def __init__(self, node_type, value=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (conditions)
        self.left = None       # Left child node
        self.right = None      # Right child node
        self.value = value     # Operand value (e.g., age > 30)

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
