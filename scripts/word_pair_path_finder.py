from merge_sort import merge_sort
from binary_search import binary_search
from bfs import bfs, bi_bfs
from create_adjacency_list import create_adjacency_list
import time


def read_words_from_file(filename):
    with open(filename, "r") as f_in:
        words = f_in.readlines()
    return [word.replace('\n', '') for word in words]


def main(bfs_option="bfs"):
    start_time = time.time()

    word_list = read_words_from_file("../data/dicionario1.txt")

    sorted_word_list = merge_sort(word_list)

    adjacency_list = create_adjacency_list(sorted_word_list)

    input_lines = read_words_from_file("../data/input_08.txt")

    with open("../data/output.txt", "w") as output_file:
        for line in input_lines:
            word1, word2 = line.strip().split(" ")
            word1_idx = binary_search(sorted_word_list, 0, len(sorted_word_list) - 1, word1)
            word2_idx = binary_search(sorted_word_list, 0, len(sorted_word_list) - 1, word2)

            if word1_idx == -1 or word2_idx == -1:
                output_file.write(f"{word1} -1\n{word2}\n\n")
                continue

            if bfs_option == "bi_bfs":
                path = bi_bfs(len(sorted_word_list), adjacency_list, word1_idx, word2_idx)
            else:
                path = bfs(len(sorted_word_list), adjacency_list, word1_idx, word2_idx)

            if path is None:
                output_file.write(f"{word1} -1\n{word2}\n\n")
            else:
                path_length = len(path) - 1
                output_file.write(f"{word1} {path_length}\n")
                for idx in path[1:-1]:
                    output_file.write(f"{sorted_word_list[idx]}\n")
                output_file.write(f"{sorted_word_list[path[-1]]}\n\n")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total running time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
