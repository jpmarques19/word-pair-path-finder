def bfs(n, grafo, v_origem, v_destino):
    visitado = [False] * n
    dist = [float('inf')] * n
    prev = [None] * n
    fila = []
    fila.append(v_origem)
    visitado[v_origem] = True
    dist[v_origem] = 0

    while fila:
        u = fila.pop(0)
        if grafo[u] is not None:
            for v in grafo[u]:
                if not visitado[v]:
                    fila.append(v)
                    visitado[v] = True
                    dist[v] = dist[u] + 1
                    prev[v] = u

                    if v == v_destino:
                        path = []
                        while v is not None:
                            path.append(v)
                            v = prev[v]
                        return path[::-1]
                    
    return None

def bi_bfs(n, grafo, source, target):
    # Initialize forward and backward searches
    forward_q = [source]
    forward_visited = [False] * n
    forward_visited[source] = True
    forward_dist = [0] * n
    backward_q = [target]
    backward_visited = [False] * n
    backward_visited[target] = True
    backward_dist = [0] * n
    intersection_node = None

    while forward_q and backward_q:
        # Perform one step of forward search
        forward_node = forward_q.pop(0)
        for neighbor in grafo[forward_node]:
            if not forward_visited[neighbor]:
                forward_visited[neighbor] = True
                forward_dist[neighbor] = forward_dist[forward_node] + 1
                forward_q.append(neighbor)
            # Check for intersection
            if backward_visited[neighbor]:
                intersection_node = neighbor
                break
        if intersection_node is not None:
            break

        # Perform one step of backward search
        backward_node = backward_q.pop(0)
        for neighbor in grafo[backward_node]:
            if not backward_visited[neighbor]:
                backward_visited[neighbor] = True
                backward_dist[neighbor] = backward_dist[backward_node] + 1
                backward_q.append(neighbor)
            # Check for intersection
            if forward_visited[neighbor]:
                intersection_node = neighbor
                break
        if intersection_node is not None:
            break

    if intersection_node is None:
        # No path found
        return None

    # Construct the path
    path = [intersection_node]
    node = intersection_node
    while node != source:
        # Backtrack in the forward search
        for neighbor in grafo[node]:
            if forward_dist[neighbor] == forward_dist[node] - 1:
                path.append(neighbor)
                node = neighbor
                break
    path.reverse()
    node = intersection_node
    while node != target:
        # Backtrack in the backward search
        for neighbor in grafo[node]:
            if backward_dist[neighbor] == backward_dist[node] - 1:
                path.append(neighbor)
                node = neighbor
                break

    return path
