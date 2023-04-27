import time
from binary_search import binary_search


def adj(pal1, pal2):
    """
    Verifica se duas palavras são adjacentes.
    Duas palavras são adjacentes se, alterando apenas uma letra a uma delas, as palavras tornam-se iguais.
    """
    if pal1 == pal2:
        return False

    count = sum(p1 != p2 for p1, p2 in zip(pal1, pal2))
    return count == 1


def adiciona_aresta(grafo, u, v):
    """Adiciona uma aresta entre os vértices 'u' e 'v'."""
    grafo[u].append(v)
    grafo[v].append(u)


def bfs(n, grafo, v_origem, v_destino):
    """
    Procura em largura.
    Devolve o menor número de arestas entre v_origem e v_destino
    ou -1, caso não exista um caminho entre v_origem e v_destino.
    """
    
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
                    return dist
    return -1


def main():
    # Ficheiros de entrada e saída
    ficheiro_input = "../data/input_08.txt"
    ficheiro_dicionario = "../data/dicionario.txt"
    ficheiro_saida = "../data/output.txt"

    # Ler pares de palavras do ficheiro de entrada
    with open(ficheiro_input, "r") as f_in:
        pals_ab = [linha.strip().split() for linha in f_in.readlines()]

    # Obter comprimentos únicos das palavras nos pares
    comprimentos = sorted(list({len(pal1) for pal1, _ in pals_ab}))

    # Ler palavras do ficheiro de dicionário
    with open(ficheiro_dicionario, "r") as f_di:
        dicionario = [linha.strip() for linha in f_di.readlines()]

    # Criar um dicionário com palavras agrupadas por comprimento
    dicionario_por_comprimento = {
        comprimento: sorted(pal for pal in dicionario if len(pal) == comprimento)
        for comprimento in comprimentos
    }

    # Construir grafos para cada comprimento de palavra
    grafos = {}
    # Iterar sobre cada comprimento de palavra e suas palavras correspondentes
    for comprimento, palavras in dicionario_por_comprimento.items():
        n = len(palavras)
        # Criar um grafo vazio com uma lista para cada palavra
        grafo = [[] for _ in range(n)]
        # Iterar sobre cada par de palavras no conjunto de palavras
        for j, pal1 in enumerate(palavras):
            for k, pal2 in enumerate(palavras[j + 1:], start=j + 1):
                # Verificar se as palavras são adjacentes
                if adj(pal1, pal2):
                    # Adicionar aresta entre as palavras no grafo
                    adiciona_aresta(grafo, j, k)
        # Armazenar o grafo no dicionário de grafos
        grafos[comprimento] = grafo

    # Processar pares de palavras e escrever os resultados no ficheiro de saída
    with open(ficheiro_saida, "w") as f_out:
        for pal1, pal2 in pals_ab:
            comprimento = len(pal1)
            palavras = dicionario_por_comprimento[comprimento]
            grafo = grafos[comprimento]

            # Se uma das palavras não estiver no dicionário, escrever -1
            if (
                binary_search(palavras, 0, len(palavras) - 1, pal1) == -1
                or binary_search(palavras, 0, len(palavras) - 1, pal2) == -1
            ):
                f_out.write(f"{pal1} -1\n{pal2}\n\n")
            # Se as palavras forem iguais, escrever 0
            elif pal1 == pal2:
                f_out.write(f"{pal1} 0\n{pal2}\n\n")
            else:
                v1, v2 = palavras.index(pal1), palavras.index(pal2)
                n = len(palavras)
                dist = bfs(n, grafo, v1, v2)

                # Se não houver caminho entre as palavras, escrever -1
                if dist == -1:
                    f_out.write(f"{pal1} {dist}\n{pal2}\n\n")
                else:
                    maxv = max(d for d in dist if d != float("inf"))

                    # Escrever o caminho entre as palavras
                    f_out.write(f"{pal1} {maxv}\n")
                    for i in range(1, maxv):
                        if i in dist:
                            elem = dist.index(i)
                            f_out.write(f"{palavras[elem]}\n")
                    f_out.write(f"{pal2}\n\n")


if __name__ == "__main__":
    tempo_inicial = time.time()
    main()
    tempo_final = time.time()
    print("Tempo de execução = ", tempo_final - tempo_inicial, "segundos =", (tempo_final - tempo_inicial) / 60, "minutos")
