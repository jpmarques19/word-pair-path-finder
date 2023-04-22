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