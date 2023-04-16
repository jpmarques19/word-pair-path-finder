def adicionaAresta(grafo,u,v):
    grafo[u].append(v)
    grafo[v].append(u)

# Procura em largura (devolve o menor n'umero de arestas entre v_origem e v_destino ou -1, caso não exista um caminho entre v_origem e v_destino)
""" def bfs(n, grafo, v_origem, v_destino):
    
    if (v_origem == v_destino): return 0
    #if (v_origem >= n or v_destino >= n): return -1
    # cria lista dos vértives visitados (inicializada a False)
    visitado = [False] * n
    # cria uma lista que guarda, para cada vértice v, o menor número de arestas entre v_origem e v (inicializada a infinito).
    dist = [float('inf')] * n
    fila = []
    fila.append(v_origem)
    visitado[v_origem] = True
    dist[v_origem]=0
 
    while fila:
        u = fila.pop(0)
        for v in grafo[u]:
            if visitado[v] == False:
                fila.append(v)
                visitado[v] = True
                dist[v]=dist[u]+1
                if v == v_destino:
                    return dist[v_destino]
    return -1 """

# programa principal


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


# cria o grafo
n = 10 # número de vértices do grafo
grafo = [[] for i in range(n)] # O grafo é representado por uma lista de adjacências. Cada posição i da lista grafo contém uma lista com os vértices adjacentes ao vértice i.
adicionaAresta(grafo, 0, 1) # adiciona as arestas entre os vértices  0 e 1
adicionaAresta(grafo, 0, 2) # adiciona as arestas entre os vértices  0 e 2
adicionaAresta(grafo, 1, 3) # adiciona as arestas entre os vértices  1 e 3
adicionaAresta(grafo, 3, 4) # adiciona as arestas entre os vértices  3 e 4
adicionaAresta(grafo, 2, 4) # adiciona as arestas entre os vértices  2 e 4

# Executa a bfs entre os vértices 0 e 4 e devolve o menor n'umero de arestas entre os vértices 0 e 4
print(bfs(n, grafo, 0, 4))

print(grafo)