from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_indices = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_indices.append(index)

    def search(self, word, max_distance):
        candidates = []

        stack = [(self.root, 0, 0, False)]  # node, index, distance, visited

        while stack:
            node, index, distance, visited = stack.pop()

            if index == len(word) and distance <= max_distance:
                candidates.extend(node.word_indices)

            if not node.children or distance > max_distance:
                continue

            if not visited:
                stack.append((node, index + 1, distance, True))
                for char, child in node.children.items():
                    stack.append((child, index + 1, distance + (char != word[index]), False))

        return candidates

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

    for word_indices in words_by_length.values():
        trie = Trie()
        for idx, word in word_indices:
            trie.insert(word, idx)

        for idx1, word1 in word_indices:
            candidates = trie.search(word1, max_distance=1)
            for idx2 in candidates:
                if idx1 != idx2 and word_distance(word1, words[idx2]) == 1:
                    adicionaAresta(grafo, idx1, idx2)

    return grafo


