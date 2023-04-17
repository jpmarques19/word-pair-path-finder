from merge_sort import merge_sort
from binary_search import binary_search
from bfs import bfs
from create_adjacency_list import create_adjacency_list
import time

start_time = time.time()


f_in = open("dicionario1.txt", "r")

lista_palavras = f_in.readlines()
lista_palavras = [palavra.replace('\n', '') for palavra in lista_palavras]

dicionario_ordenado = merge_sort(lista_palavras)

adj_list = create_adjacency_list(dicionario_ordenado)

print(binary_search(dicionario_ordenado, 0, len(dicionario_ordenado) - 1, "engeheiro"))

f_in_input_01 = open("input_08.txt", "r")
lines = f_in_input_01.readlines()

output_file = open("output.txt", "w")

for line in lines:
    word1, word2 = line.strip().split(" ")
    word1_idx = binary_search(dicionario_ordenado, 0, len(dicionario_ordenado) - 1, word1)
    word2_idx = binary_search(dicionario_ordenado, 0, len(dicionario_ordenado) - 1, word2)

    if word1_idx == -1 or word2_idx == -1:
        output_file.write(f"{word1} -1\n{word2}\n\n")
        continue

    path = bfs(len(dicionario_ordenado), adj_list, word1_idx, word2_idx)

    if path is None:
        output_file.write(f"{word1} -1\n{word2}\n\n")
    else:
        path_length = len(path) - 1
        output_file.write(f"{word1} {path_length}\n")
        for idx in path[1:-1]:
            output_file.write(f"{dicionario_ordenado[idx]}\n")
        output_file.write(f"{dicionario_ordenado[path[-1]]}\n\n")

output_file.close()

end_time = time.time()
total_time = end_time - start_time
print(f"Total time: {total_time:.2f} seconds")
