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

