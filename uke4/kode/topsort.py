class Task:
    def __init__(self, name : str) -> None:
        self.name = name
        self.dependers = []
        self.inEdges = 0

    def __repr__(self) -> str:
        return self.name

def top_sort(tasks : list[Task]):
    stack = []

    for node in tasks:
        for depender in node.dependers:
            depender.inEdges += 1

    for node in tasks:
        if node.inEdges == 0:
            stack.append(node)

    taskCounter = 0
    output = []
    while len(stack) > 0:
        current = stack.pop()
        taskCounter += 1
        output.append(current.name)

        for depender in current.dependers:
            depender.inEdges -= 1
            if depender.inEdges == 0:
                stack.append(depender)

    if taskCounter < len(tasks):
        return "Cycle"

    return "\n".join(output)

def test():
    a = Task('A')
    b = Task('B')
    c = Task('C')
    d = Task('D')
    e = Task('E')
    f = Task('F')
    g = Task('G')

    a.dependers.append(b)
    a.dependers.append(c)

    b.dependers.append(c)
    b.dependers.append(d)

    c.dependers.append(d)
    c.dependers.append(e)

    d.dependers.append(g)

    e.dependers.append(g)

    f.dependers.append(d)

    tasks = [a,b,c,d,e,f,g]

    print(top_sort(tasks))

if __name__ == "__main__":
    test()


