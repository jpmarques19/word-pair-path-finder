def word_distance(word1, word2):
    """
    calculate the distance between two words
    """
    if len(word1) != len(word2):
        return -1
    
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance
#%%
words = ["casa", "cosa", "cato", "cima", "pala", "palo", "papa", "pata", "pato", "pima", "pita", "pito", "pota", "poto", "tapa", "tata", "tima", "tita", "tito", "tota", "toto"]

# Sort the list
words.sort()

# Print the sorted list
print(words)

#%%
from bfs import bfs
from bfs import adicionaAresta
#create an adjacency matrix where edges exist only when the distance between two words is 1
grafo = [[] for i in range(len(words))] # O grafo é representado por uma lista de adjacências. Cada posição i da lista grafo contém uma lista com os vértices adjacentes ao vértice i.
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if word_distance(words[i], words[j]) == 1:
            adicionaAresta(grafo, i, j)

print(grafo)
#%%

# Executa a bfs entre os vértices 0 e 4 e devolve o menor n'umero de arestas entre os vértices 0 e 4
print(bfs(len(words), grafo, 0, 2))

print(words[9], words[16])

#%%

# cria o grafo
n = 10 # número de vértices do grafo
grafo = [[] for i in range(n)] # O grafo é representado por uma lista de adjacências. Cada posição i da lista grafo contém uma lista com os vértices adjacentes ao vértice i.
adicionaAresta(grafo, 0, 1) # adiciona as arestas entre os vértices  0 e 1
adicionaAresta(grafo, 0, 2) # adiciona as arestas entre os vértices  0 e 2
adicionaAresta(grafo, 1, 3) # adiciona as arestas entre os vértices  1 e 3
adicionaAresta(grafo, 3, 4) # adiciona as arestas entre os vértices  3 e 4
adicionaAresta(grafo, 2, 4) # adiciona as arestas entre os vértices  2 e 4

print(grafo)
#%%

#print grafo in ascii
for i in range(len(grafo)):
    print(words[i], end=' ')
    for j in range(len(grafo[i])):
        print(words[grafo[i][j]], end=' ')
    print()
