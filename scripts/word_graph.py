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