**Report 1: Non-Optimized Algorithm**

## Introduction

### Problem Description

The problem involves finding the shortest path between pairs of words within a given set of words, with the condition that two words are connected if they have a word distance of 1 (i.e., they differ by exactly one character). The program should find the path with the minimum number of connections (word transformations) and calculate the total number of connections. If no path exists, the program should return -1.

## Non-Optimized Algorithm

### Description of the Non-Optimized Algorithm

The non-optimized algorithm consists of the following steps:

1. Read the input words from a file and sort them using the `merge_sort` function.
2. Create an adjacency list representing the connections between words using the `create_adjacency_list` function.
3. Read the input word pairs from a file.
4. For each word pair, perform a breadth-first search (BFS) using the `bfs` function to find the shortest path between the words. If a path is found, write the path and the number of connections to the output file. If no path exists, write -1 to the output file.

The building blocks of the non-optimized algorithm are as follows:

- `merge_sort`: A sorting algorithm used to sort the input words.
- `binary_search`: A searching algorithm used to find the index of a word in the sorted list of words.
- `create_adjacency_list`: A function to create an adjacency list representing the connections between words.
- `bfs`: A breadth-first search algorithm used to find the shortest path between two words.

## Merge Sort

Merge sort is a sorting algorithm used to sort the input words. It is a divide-and-conquer algorithm that works by recursively dividing the input list into two halves, sorting each half, and then merging the sorted halves to produce the final sorted list.

### Pseudocode for Merge Sort

```
function merge_sort(vector):
    if len(vector) <= 1:
        return vector

    mid = len(vector) // 2
    left_half = merge_sort(vector[:mid])
    right_half = merge_sort(vector[mid:])

    return merge(left_half, right_half)
```

## Binary Search

Binary search is a searching algorithm used to find the index of a word in the sorted list of words. It works by repeatedly dividing the search interval in half and comparing the middle element of the interval with the target value. If the middle element matches the target value, its index is returned. If the middle element is less than or greater than the target value, the search continues on the left or right half of the interval, respectively, until the target value is found or the interval becomes empty.

### Pseudocode for Binary Search

```
function binary_search(v, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if target == v[mid]:
            return mid
        elif target < v[mid]:
            high = mid - 1
        elif target > v[mid]:
            low = mid + 1
    return -1
```

## Adjacency List Generation

The adjacency list generation algorithm creates a list of lists representing the connections between words in the input list. Each inner list contains the indices of words connected to the corresponding word in the input list, where two words are connected if their word distance is 1. The algorithm groups words by length and iterates over each word, generating new words by replacing one character at a time and checking if the generated word exists in the input words. If a connection is found, an edge is added to the adjacency list.

### Pseudocode for Adjacency List Generation

```
function create_adjacency_list(words):
    grafo = [[] for _ in range(len(words))]
    
    words_set = set(words)
    
    words_by_length = defaultdict(list)
    for idx, word in enumerate(words):
        words_by_length[len(word)].append((idx, word))

    for word_indices in words_by_length.values():
        for idx, word in word_indices:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word in words_set and new_word != word:
                        new_idx = words.index(new_word)
                        if new_idx not in grafo[idx]:
                            adicionaAresta(grafo, idx, new_idx)

    return grafo
```

## Breadth-First Search (BFS)

The BFS algorithm is used to find the shortest path between two words in the adjacency list. It works by traversing the graph using a queue data structure and maintaining a list of visited nodes. For each node visited, the algorithm checks if it is the destination node. If so, the path is reconstructed using the previous node information and returned. If not, the algorithm continues to explore the neighbors of the current node.

### Pseudocode for BFS

```
function bfs(n, grafo, v_origem, v_destino):
    visitado = [False] * n
    dist = [float('inf')] * n
    prev = [None] * n
    fila = [v_origem]
    visitado[v_origem] = True
    dist[v_origem] = 0

    while fila:
        u = fila.pop(0)
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
```

## Time and Space Complexity Analysis

- Merge sort: Time complexity is O(n log n), where n is the number of input words. Space complexity is O(n), as it requires additional space for merging.
- Binary search: Time complexity is O(log n), where n is the number of input words. Space complexity is O(1), as it only requires constant additional space.
- Adjacency list generation: Time complexity is O(n^2), where n is the number of input words, as the algorithm iterates over each word and character. Space complexity is O(n^2), as it stores connections between words in the adjacency list.
- BFS: Time complexity is O(n + m), where n is the number of input words and m is the number of edges in the graph. Space complexity is O(n), as it requires additional space for the visited list, distance list, and previous node list.

## Results

### Datasets Used

- Dataset 1: dicionario1.txt (list of words)
- Dataset 2: input_08.txt (list of word pairs)

### Runtime

- Total running time: xx.xx seconds (Please run the program and replace xx.xx with the actual runtime)

## Conclusion

The non-optimized algorithm can find the shortest path between pairs of words in a given set of words, using BFS to traverse the adjacency list generated from the input
