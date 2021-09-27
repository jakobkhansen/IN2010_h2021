import sys
from priorityqueue import PriorityQueue

class Node:
    def __init__(self, label) -> None:
        self.label = label
        self.neighbours = []

        self.finished = False
        self.relax = sys.maxsize # Ekstremt stor verdi
        self.previous = None

        self.heap_index = None

    def __repr__(self) -> str:
        return str(self.label) + ' ' + str(self.heap_index)

    def __lt__(self, other):
        return self.relax < other.relax


def dijkstra(start_node, end_node):
    pq = PriorityQueue()

    start_node.relax = 0
    pq.insert(start_node)

    while pq.size() > 0:
        current = pq.pop()
        for weight,edge in current.neighbours:
            potentialRelax = current.relax + weight

            if potentialRelax < edge.relax:
                edge.relax = potentialRelax
                edge.previous = current
                
                # If node not in queue yet, add it
                if edge.heap_index == None:
                    pq.insert(edge)
                else:
                    # If the node is in the queue, bubble the node upwards (updatekey)
                    pq.bubbleUp(edge.heap_index)
        current.finished = True

    shortest_path_weight = end_node.relax

    shortest_path = []

    current = end_node

    while current != None:
        shortest_path.append(current)
        current = current.previous

    shortest_path_string = ' '.join(reversed([x.label for x in shortest_path]))

    return shortest_path_weight, shortest_path_string



if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')


    a.neighbours.append((7, b))
    a.neighbours.append((9, c))
    a.neighbours.append((14, f))
    
    b.neighbours.append((10, c))
    b.neighbours.append((15, d))


    c.neighbours.append((11, d))
    c.neighbours.append((2, f))

    f.neighbours.append((9, e))

    shortest_path_weight, shortest_path = dijkstra(a, e)
    print(f"Shortest path weight: {shortest_path_weight}")
    print(f"Shortest path: {shortest_path}")
