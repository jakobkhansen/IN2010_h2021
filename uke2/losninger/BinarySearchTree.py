from typing import Optional


# Node class, represents a node in a BST
class Node:
    def __init__(self, value : int) -> None:
        self.value : int = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.height : int = 0

    # Prints a node in a more clean fashion when doing print(node)
    def __repr__(self) -> str:
        left_val = str(self.left.value) if self.left != None else "None"
        right_val = str(self.right.value) if self.right != None else "None"

        return f"Node({self.value}, {left_val}, {right_val})"

    # Updates the height of a given node
    # Assumes that self.left and self.right have updated heights
    def update_height(self) -> None:
        self.height = max(height(self.left), height(self.right)) + 1

    
    # Visualizes a subtree with root in this node
    def visualize(self):
        display(self)

# Returns the height of a node or null-pointer
def height(node : Optional[Node]) -> int:
    if node == None:
        return -1
    return node.height

# Returns the balance of a node or null-pointer
def balanceFactor(node : Optional[Node]) -> int:
    if node == None:
        return -1;

    return height(node.left) - height(node.right)

# Rotates left with top as the top node, middle as the right child of top
def leftRotate(top) -> Node:
    middle = top.right;

    b = middle.left;

    middle.left = top;
    top.right = b;

    top.update_height()
    middle.update_height()

    return middle

# Rotates right with top as the top node, middle as the left child of top
def rightRotate(top) -> Node:
    middle = top.left;

    b = middle.right

    middle.right = top;
    top.left = b;

    top.update_height()
    middle.update_height()

    return middle

# Performs balancing if node is unbalanced
def balance(node : Node) -> Node:

    if balanceFactor(node) < -1:
        if balanceFactor(node.right) > 0:
            node.right = rightRotate(node.right)
        return leftRotate(node)

    if balanceFactor(node) > 1:
        if balanceFactor(node.left) < 0:
            node.left = leftRotate(node.left)
        return rightRotate(node)

    return node

# BST implementation with AVL tree rotations
# Supports search and insertion
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Visualizes the tree
    def visualize(self):
        if self.root != None:
            self.root.visualize()
        else:
            print("Empty tree")

    # Insert value in tree, balance if necessary
    def insert(self, value : int) -> None:
        if self.root == None:
            self.root = Node(value)
            return

        self.root = self.insert_recursive(value, self.root)

    def insert_recursive(self, value : int, current : Optional[Node]) -> Node:

        if current == None:
            current = Node(value)

        # Left
        elif value < current.value:
            current.left = self.insert_recursive(value, current.left)

        # Right
        elif value >= current.value:
            current.right = self.insert_recursive(value, current.right)

        # Oppdater høyde på vei opp i rekursjonen
        current.update_height()

        # Balanser treet og returner eventuelt ny node
        return balance(current)


    # Search for a node in the tree
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

# Disse to metodene hjelper bare med å visualisere et binært søketre i terminalen. Bruk
# bst.visualize() for å visualisere bst i terminalen.

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

bst = BinarySearchTree()

for i in range(100):
    bst.insert(i)

bst.visualize()
