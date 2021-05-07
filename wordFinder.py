# Main Program
# Project 3 – Word Finder
#
# Name: Roshni Vakil
# Section: 9/10
# Date: 2/20/21
#
from wordFinderFuncs import *


def main():
    puzzle = getPuzzleList()
    print(puzzle)
    printPuzzleString(puzzle)
    listOfWords = getWords()
    print()
    for word in listOfWords:
        print(word, ": ", end ='')
        if forward_and_basis_for_other_functions(puzzle, word) != "N":
            print("(FORWARD)", forward_and_basis_for_other_functions(puzzle, word))
        elif backward(puzzle, word) != "N":
            print("(BACKWARD)", backward(puzzle, word))
        elif upward(puzzle, word) != "N":
            print("(UP) ", upward(puzzle, word))
        elif downward(puzzle, word) != "N":
            print("(DOWN)", downward(puzzle, word))
        elif diagonally(puzzle, word) != "N":
            print("(DIAGONAL)", diagonally(puzzle, word))
        else:
            print("word not found")


if __name__ == '__main__':
    main()