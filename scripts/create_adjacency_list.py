from collections import defaultdict

def word_distance(word1, word2):
    return sum(a != b for a, b in zip(word1, word2))

def adicionaAresta(grafo, idx1, idx2):
    grafo[idx1].append(idx2)
    grafo[idx2].append(idx1)

def create_adjacency_list(words):
    grafo = [[] for _ in range(len(words))]
    
    # Create a set of words for faster lookup
    words_set = set(words)
    
    # Group words by length
    words_by_length = defaultdict(list)
    for idx, word in enumerate(words):
        words_by_length[len(word)].append((idx, word))

    for word_indices in words_by_length.values():
        for idx, word in word_indices:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Generate a new word with one character replaced
                    new_word = word[:i] + c + word[i+1:]
                    
                    # If the generated word exists in the input words, add an edge
                    if new_word in words_set and new_word != word:
                        new_idx = words.index(new_word)
                        if new_idx not in grafo[idx]:
                            adicionaAresta(grafo, idx, new_idx)

    return grafo
