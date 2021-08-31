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

class BinarySearchTree:

    def __init__(self):
        self.root = None

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




bst = BinarySearchTree()
bst.insert(10)
bst.insert(15)
bst.insert(12)
