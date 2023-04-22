from collections import defaultdict
import datrie

def adicionaAresta(grafo,u,v):
    grafo[u].append(v)
    grafo[v].append(u)
    
def word_distance(word1, word2):
    """
    Calculate the distance between two words.
    """
    if len(word1) != len(word2):
        return -1

    return sum(char1 != char2 for char1, char2 in zip(word1, word2))

def create_adjacency_list(words):
    grafo = [[] for _ in range(len(words))]

    # Group words by length
    words_by_length = defaultdict(list)
    for idx, word in enumerate(words):
        words_by_length[len(word)].append((idx, word))

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for word_indices in words_by_length.values():
        trie = datrie.Trie(alphabet)
        for idx, word in word_indices:
            trie[word] = idx

        for idx1, word1 in word_indices:
            for i in range(len(word1)):
                for char in alphabet:
                    candidate_word = word1[:i] + char + word1[i+1:]
                    if candidate_word in trie:
                        idx2 = trie[candidate_word]
                        if idx1 != idx2 and word_distance(word1, words[idx2]) == 1:
                            adicionaAresta(grafo, idx1, idx2)

    return grafo




