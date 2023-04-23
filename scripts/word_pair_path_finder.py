import time
from helpers import read_input_file
from helpers import read_dictionary_file
from word_graph import WordGraph
from word_pair_processor import WordPairProcessor

def main():
    input_pairs = read_input_file("../data/input_08.txt")
    unique_words = read_dictionary_file("../data/dicionario.txt")
    word_graph = WordGraph(input_pairs, unique_words)
    word_pair_processor = WordPairProcessor(word_graph)

    with open('../data/output.txt', 'w') as output_file:
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


