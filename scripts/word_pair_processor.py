from binary_search import binary_search
from bfs import bfs

class WordPairProcessor:
    def __init__(self, word_graph):
        self.word_graph = word_graph

    def process_word_pair(self, word_a, word_b):
        length = len(word_a)
        if (binary_search(self.word_graph.length_word_dict[length], 0, len(self.word_graph.length_word_dict[length]) - 1, word_a) == -1 or
            binary_search(self.word_graph.length_word_dict[length], 0, len(self.word_graph.length_word_dict[length]) - 1, word_b) == -1):
            return f"{word_a} -1\n{word_b}\n\n"

        if word_a == word_b:
            return f"{word_a} 0\n{word_b}\n\n"

        words_list = self.word_graph.length_word_dict[length]
        index_a = words_list.index(word_a)
        index_b = words_list.index(word_b)
        num_words = len(words_list)
        graph = self.word_graph.word_length_graphs[length]
        path_a_b = bfs(num_words, graph, index_a, index_b)

        if path_a_b is None:
            return f"{word_a} -1\n{word_b}\n\n"
        else:
            path_length = len(path_a_b) - 1
            path_string = "\n".join(words_list[i] for i in path_a_b[1:])
            return f"{word_a} {path_length}\n{path_string}\n{word_b}\n"
