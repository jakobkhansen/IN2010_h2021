# Algoritme som finner separasjonsnoder  i en graf
# Blir kalt Hopcroft-Tarjan, men disse to har laget mange algoritmer, så det er vanskelig
# å finne informasjon basert på dette navnet.

# Kompleksitet: O(|V| + |E|)

class Node:
    def __init__(self, label) -> None:
        self.label = label
        self.edges = []
        self.visited = False
        self.index = 0
        self.low = 0
        self.child_count = 0

    def __repr__(self) -> str:
        return str(self.label)

def hopcroft_tarjan(current : Node, depth = 1):
    current.visited = True

    current.low = depth
    current.index = depth

    for edge in current.edges:
        if not edge.visited:
            current.child_count += 1
            hopcroft_tarjan(edge, depth + 1)
            current.low = min(current.low, edge.low)
            if current.index != 1 and current.index <= edge.low:
                print(f'{current} is an articulation point')
        else:
            current.low = min(current.low, edge.index)

    if current.index == 1 and current.child_count > 1:
        print(f'{current} is an articulation point')

def test():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    add_undirected_edge(a,b)
    add_undirected_edge(a,c)
    add_undirected_edge(b,c)

    add_undirected_edge(c,d)
    add_undirected_edge(c,e)

    add_undirected_edge(e,f)
    add_undirected_edge(d,f)

    add_undirected_edge(f,g)
    add_undirected_edge(f,h)
    add_undirected_edge(g,h)


    hopcroft_tarjan(a)

def add_undirected_edge(a, b):
    a.edges.append(b)
    b.edges.append(a)





if __name__ == "__main__":
    test()
