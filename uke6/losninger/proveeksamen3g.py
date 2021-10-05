from collections import deque

def order_critical_agents(V, E, oscar):
    critical_agents = []

    bfs(V, E, oscar)

    return critical_agents


def bfs(V, E, start):
    # Kjører et BFS søk fra start som bare reiser via ordre-kanaler.
    # Hvis en node har en ordre-kanal ut fra seg (som ikke allerede er besøkt)
    # Er dette en ordrekritisk agent, legg til critical_agents

    critical_agents = []

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while len(queue) > 0:
        current = queue.popleft()

        is_critical = False

        for (current, v, is_order_channel) in E:
            if is_order_channel and v not in visited:
                is_critical = True
                queue.append(v)
                visited.add(v)


        if is_critical or current == start:
            critical_agents.append(current)

    return critical_agents

        
