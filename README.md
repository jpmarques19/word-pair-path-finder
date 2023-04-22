# Word Pair Path Finder

This is an academic project developed in Python, designed to find the shortest path between word pairs within a given set of words. 

## Problem Statement

Given a set of words S and a sequence of k ordered word pairs, the program should decide whether there exists a path between each word pair in the set S. If such a path exists, the program should find the path with the minimum number of connections (word transformations) and calculate the total number of connections. If no path exists, the program should return -1.

## Input

The program takes two input files:

1. A file containing a set S of words in the following format:

```
word1
word2
...
wordn
```

2. A file containing k pairs of words in the following format:

```
word1a word1b
word2a word2b
...
wordka wordkb
```

## Output

The program generates a text file as output in the following format:

```
word1a num_connections1
...
word1b
word2a num_connections2
...
word2b
wordka num_connectionsk
...
wordkb
```

## Getting Started

1. Clone the repository
2. Install the required Python libraries if necessary
3. Run the script, providing the input files as arguments
4. View the generated output file

