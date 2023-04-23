def read_input_file(file_path):
    with open(file_path, "r") as file_in:
        input_pairs = [line.strip().split() for line in file_in.readlines()]
    return input_pairs

def read_dictionary_file(file_path):
    with open(file_path, "r") as file_di:
        unique_words = list(set(line.strip() for line in file_di.readlines()))
    return unique_words