# Oppgave: Avgjør O-notasjonen på hver prosedyre
# Dere kan bruke amortized kjøretid, så for eksempel hashmap har konstant-tid operasjoner

# Deque er implementert som en dobbelt-lenket lenkeliste
from collections import deque

def fill_stack(n : int):
    stack = []

    for i in range(n):
        stack.append(n)

    for i in range(n):
        print(stack.pop())

def fill_queue(n : int):
    queue = []

    for i in range(n):
        queue.append(n)

    for i in range(n):
        queue.pop(0)

def fill_deque(n : int):
    dq = deque()
    for i in range(n//2):
        dq.appendleft(i)

    while len(dq) > 0:
        dq.pop()

    for i in range(n//2):
        dq.append(i)

    while len(dq) > 0:
        dq.popleft()

def recursive_split(numbers : list[int]):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]

    mid = (len(numbers) // 2)
    sum += recursive_split(numbers[0:mid])
    sum += recursive_split(numbers[mid+1:])

    return sum

def crazy_loop(n : int):
    for i in range(n**2 - (n*n), 0, -1):
        print(i)


# Grafer, alle grafer inneholder V (noder) og E (edges)
# En edge inneholder (vekt, node1, node2)

def pairs(G):
    V,E = G

    pairs = []
    for i in range(len(V)):
        for j in range(i+1, len(V)):
            pairs.append((V[i], V[j]))
    return pairs

def sum_weights_in_graph(G):
    V,E = G

    weight_sum = 0
    for (weight, n1, n2) in E:
        weight_sum += weight

    # Alternativ:
    # sum(map(lambda x : x[0], E))

    return weight_sum
