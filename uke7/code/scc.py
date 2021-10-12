# Velger å implementere dette med nabolister for å vise hvordan man kan reversere kanter
# Tror egentlig nabomatrise vil være raskere i praksis her, selvom kompleksiteten er lik

class Node:
    def __init__(self, label) -> None:
        self.edges = []
        self.label = label
        self.visited = False

    def __repr__(self) -> str:
        return str(self.label)



def scc(nodes):
    # First DFS
    stack = []
    visited = set()

    for node in nodes:
        if node not in visited:
            dfs_first(node,stack, visited)

    # Second DFS
    components = []
    visited = set()

    reverse_edges(nodes)

    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_second(node, component, visited)
            components.append(component)

    # Reverse edges back to original, not strictly necessary
    reverse_edges(nodes)

    return components
        


def dfs_first(node, stack, visited):
    visited.add(node)
    for edge in node.edges:
        if edge not in visited:
            dfs_first(edge, stack, visited)

    stack.append(node)


def dfs_second(node, component, visited):
    component.append(node)
    visited.add(node)
    for edge in node.edges:
        if edge not in visited:
            dfs_second(edge, component, visited)

def reverse_edges(nodes):
    new_edges = {node : [] for node in nodes}

    for node in nodes:
        for edge in node.edges:
            new_edges[edge].append(node)
    for node in nodes:
        node.edges = new_edges[node]



def test():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')

    a.edges.append(b)

    b.edges.append(c)
    b.edges.append(d)

    c.edges.append(a)
    c.edges.append(f)

    e.edges.append(d)

    f.edges.append(g)

    g.edges.append(h)

    h.edges.append(i)

    i.edges.append(f)

    nodes = [a,b,c,d,e,f,g,h,i]


    components = scc(nodes)

    print(components)




if __name__ == "__main__":
    test()
