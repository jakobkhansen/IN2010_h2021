import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.paths = []
        self.visited = False

    def __repr__(self) -> str:
        return f"Node({self.name}, {[x.name for x in self.paths]})"

def torn2pieces(lines):
    nodes = {}
    for line in lines[1:-1]:
        station = line.split()[0]
        nodes[station] = Node(station)

    for line in lines[1:-1]:
        node = nodes[line.split()[0]]
        for neighbour in line.split()[1:]:
            node.paths.append(nodes[neighbour])

    print(nodes)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(torn2pieces(lines))
main()
