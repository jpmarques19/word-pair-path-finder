import time
from binary_search import binary_search
from bfs import bfs
from helpers import read_input_file
from helpers import read_dictionary_file

class WordGraph:
    def __init__(self, input_pairs, unique_words):
        self.length_word_dict = self.create_length_word_dict(input_pairs, unique_words)
        self.length_word_lookup = self.create_length_word_lookup(self.length_word_dict)
        self.word_length_graphs = self.create_word_length_graphs(self.length_word_dict, self.length_word_lookup)

    def create_length_word_dict(self, input_pairs, unique_words):
        unique_lengths = list(set(len(pair[0]) for pair in input_pairs))
        length_word_dict = {length: sorted([word for word in unique_words if len(word) == length]) for length in unique_lengths}
        return length_word_dict

    def create_length_word_lookup(self, length_word_dict):
        length_word_lookup = {length: {word: idx for idx, word in enumerate(words)} for length, words in length_word_dict.items()}
        return length_word_lookup

    def generate_new_words(self, word):
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                yield word[:i] + c + word[i+1:]

    def is_adjacent(self, word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

    def create_word_length_graphs(self, length_word_dict, length_word_lookup):
        word_length_graphs = {}

        for word_length, words_with_same_length in length_word_dict.items():
            adjacency_list = []

            for word1 in words_with_same_length:
                neighbors = []

                for new_word in self.generate_new_words(word1):
                    if new_word in length_word_lookup[word_length]:
                        word2_index = length_word_lookup[word_length][new_word]
                        word2 = words_with_same_length[word2_index]

                        if self.is_adjacent(word1, word2):
                            neighbors.append(word2_index)

                adjacency_list.append(neighbors)

            word_length_graphs[word_length] = adjacency_list

        return word_length_graphs

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



def main():
    input_pairs = read_input_file("../data/input_08.txt")
    unique_words = read_dictionary_file("../data/dicionario1.txt")
    word_graph = WordGraph(input_pairs, unique_words)
    word_pair_processor = WordPairProcessor(word_graph)

    with open('output.txt', 'w') as output_file:
        for index, (word_a, word_b) in enumerate(input_pairs):
            processed_pair = word_pair_processor.process_word_pair(word_a, word_b)
            output_file.write(processed_pair)
            if index < len(input_pairs) - 1 and not input_pairs[index + 1]:
                output_file.write('\n')

if __name__ == "__main__":
    
    start_time = time.time()
    main()
    end_time = time.time()

print("Total execution time = ", end_time - start_time, "seconds", (end_time - start_time) / 60, "minutes")


