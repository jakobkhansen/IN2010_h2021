# Naboliste løsning
from queue import Queue

class Node:
    def __init__(self, value) -> None:
        self.value : int = value
        self.neighbours : list[Node] = []
        self.visited : bool = False

    def __repr__(self) -> str:
        return str(self.value)

def dfs(node : Node) -> None:
    print(node)
    node.visited = True
    for neighbour in node.neighbours:
        if not neighbour.visited:
            dfs(neighbour)



def bfs(start_node : Node) -> None:
    queue = Queue()

    start_node.visited = True
    queue.put(start_node)

    while not queue.empty():
        current = queue.get()
        print(current)
        for neighbour in current.neighbours:
            if not neighbour.visited:
                neighbour.visited = True
                queue.put(neighbour)


def test():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')


    undirected_edge(a,b)
    undirected_edge(b,c)
    undirected_edge(b,d)
    undirected_edge(c,h)
    undirected_edge(d,e)
    undirected_edge(d,f)
    undirected_edge(f,e)
    undirected_edge(f,g)


    print("--- DFS ---")
    dfs(a)

    for node in [a,b,c,d,e,f,g,h]: 
        node.visited = False

    print("\n--- BFS ---")
    bfs(a)

def undirected_edge(a, b):
    a.neighbours.append(b)
    b.neighbours.append(a)

test()

