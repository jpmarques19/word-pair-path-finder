from bfs import adicionaAresta
from word_sort import word_distance

def create_adjacency_list(words):
    #create an adjacency list where edges exist only when the distance between two words is 1
    grafo = [[] for i in range(len(words))] # O grafo é representado por uma lista de adjacências. Cada posição i da lista grafo contém uma lista com os vértices adjacentes ao vértice i.
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if word_distance(words[i], words[j]) == 1:
                adicionaAresta(grafo, i, j)
