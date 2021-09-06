from typing import Optional


class Node:
    def __init__(self, value : int) -> None:
        self.value : int = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None

    def __repr__(self) -> str:
        left_val = str(self.left.value) if self.left != None else "None"
        right_val = str(self.right.value) if self.right != None else "None"

        return f"Node({self.value}, {left_val}, {right_val})"
    
    def visualize(self):
        display(self)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def visualize(self):
        if self.root != None:
            self.root.visualize()
        else:
            print("Empty tree")

    def insert(self, value : int) -> None:
        if self.root == None:
            self.root = Node(value)
            return

        self.insert_recursive(value, self.root)


    def insert_recursive(self, value : int, current : Node) -> None:
        # Left
        if value < current.value:
            if current.left == None:
                current.left = Node(value)
            else:
                self.insert_recursive(value, current.left)

        # Right
        elif value >= current.value:
            if current.right == None:
                current.right = Node(value)
            else:
                self.insert_recursive(value, current.right)

    def search(self, value : int) -> Optional[Node]:
        if self.root == None:
            return None

        return self.search_recursive(value, self.root)

    def search_recursive(self, value : int, current : Optional[Node]) -> Optional[Node]:
        if current == None:
            return None

        if current.value == value:
            return current

        elif current.value > value:
            return self.search_recursive(value, current.left)

        elif current.value < value:
            return self.search_recursive(value, current.right)

    def find_parent(self, value : int) -> Optional[Node]:
        if self.root == None:
            return None
        return self.find_parent_recursive(value, self.root)

    def find_parent_recursive(self, value : int, node : Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        if node.left != None and node.left.value == value:
            return node

        if node.right != None and node.right.value == value:
            return node

        if node.value > value:
            return self.find_parent_recursive(value, node.left)

        if node.value < value:
            return self.find_parent_recursive(value, node.right)


    def delete(self, value : int) -> None:
        if self.root == None:
            return
        self.root = self.delete_node(self.root)

    def delete_node(self, node : Node) -> None:
        if node.left != None and node.right != None:
            self.delete_node_two_children(node)
        elif node.left != None:
            pass

    
    def delete_node_two_children(self, node : Node) -> None:
        pass

    def replace_node_with_one_child(self, node : Node) -> Optional[Node]:
        return node.left if node.left != None else node.right



def display(node):
    lines, *_ = _display_aux(node)
    for line in lines:
        print(line)

def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right is None and node.left is None:
        line = '%s' % node.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = '%s' % node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = '%s' % node.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.value
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def find_min(node : Node):
    current = node
    while current.left != None:
        current = current.left
    return current


bst = BinarySearchTree()
bst.insert(10)
bst.insert(15)
bst.insert(12)
bst.insert(7)

bst.visualize()
