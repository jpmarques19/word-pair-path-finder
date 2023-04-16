words = ["casa", "cosa", "cato", "cima", "pala", "palo", "papa", "pata", "pato", "pima", "pita", "pito", "pota", "poto", "tapa", "tata", "tima", "tita", "tito", "tota", "toto"]

# Sort the list
words.sort()

# Print the sorted list
print(words)


def word_distance(word1, word2):
    """
    calculate the distance between two words
    """
    if len(word1) != len(word2):
        return -1
    
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance
