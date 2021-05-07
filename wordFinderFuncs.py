# Project 3 Word Finder
# 
# Name: Roshni Vakil
# Instructor: Dr. S. Einakian
# Section: 9/10

#creates a point object from two provided coordinates
#int + int --> Point
class Point:
    def __init__(self, row, column):
        self.__row = row
        self.__column = column
    def __repr__(self):
        return "row: " + str(self.__row) + " column: " + str(self.__column)
    def getRow(self):
        return self.__row
    def getColumn(self):
        return self.__column
    def setRow(self, value):
        self.__row = value
    def setColumn(self, value):
        self.__column = value


#purpose: gets input for puzzle
#None --> list
def getPuzzleList():
    longPuzzle = input()
    rows, cols = (10, 10)
    puzzle = []
    for i in range(cols):
        col = []
        puzzle.append(col)
        for j in range(rows):
            col.append(longPuzzle[10*i+j])
    return(puzzle)


#purpose: gets input for puzzle
#None --> list
#def getPuzzle():
    #1) asks the user for input for puzzle
    #2) stores it in a 100 character string
    #3) creates a new empty 2D list
    #4) takes the first 10 characters from the 100 character string, and adds it to a string representing line 1
    #5) adds that string to the 2D list
    #6) repeat steps 4-5 for every following set of 10 characters in the 100 character string
    #6) return that 2D list


#purpose: gets input for puzzle
#list  --> None
def printPuzzleString(twoDList: list):
    print("Puzzle: \n")
    for list in range(len(twoDList)):
        for letter in twoDList[list]:
            print(letter, end = "")
        print()


#purpose: gets an input list for words we are searching for
#None --> list
def getWords():
    words = input()
    listOfWords = words.split()
    return listOfWords


#purpose: gets an input list for words we are searching for
#None --> list
#def getWords():
    #1) create an empty place (list) to store the words that we are going to search for
    #2) asks the user if they have a word they are searching for
       #2.1) if the answer is no, give option to end program
       #2.2) if yes, ask again
    #3) add this to the empty list of words we are searching for
    #4) asks the user of they have any other words they are looking for
       #4.1) if the answer is yes, add this to the empty list of values we are searching for and repeat step 4
       #4.2) if no, return this list


#purpose: checks for given word spelled forward
#list + String --> Point
def forward_and_basis_for_other_functions(puzzleList: list, word: str):
    totalCount = 0
    for i in range(len(puzzleList)):
        count = 0
        failed = "n"
        for j in range(len(puzzleList[0])):
            totalCount += 1
            if failed =="y":
                j -= 1
            if puzzleList[i][j].lower() == word[count].lower():
                if count == 0:
                    returnVal = Point(i, j)
                count += 1
            elif puzzleList[i][j].lower() != word[count].lower() and count > 0:
                count = 0
                failed = "y"
            if count == len(word):
                return returnVal
    return "N"

#purpose: checks for given word spelled forward
#list + String --> Point
#def forward(list, word):
    #1) get the length of the given word
    #2) while the word is not found, do the following:
       #2.1) go through each character in each line incrementally until we reach the index where the word is no longer possible in that line
                  #2.1.1)if the current character matches the current character of the given word (character that starts at 0 and increments):
                          #2.1.1.1) store start location (point object)
                          #2.1.1.2) move to the next character in both the puzzle and the given word
                          #2.1.1.3) repeat step 2.1.1 without re-storing start location
                                    #2.1.1.3.1) if at any point the word is found return start location
                  # 2.1.2) if not, repeat all of step 2.1 with current character in puzzle if had gone through at least one interation of 2.1.1.
                  # 2.1.3) else, move one unit forward in the puzzle line and repeat 2.1
       #2.2) move to next line and repeat all of 2.1
       #2.3) if we finish without finding the word return None location


#purpose: checks for given word spelled backward
#list + String --> Point
def backward(puzzleList: list, word: str):
    backwardList = []
    for i in range(len(puzzleList)):
        backwardList.append([])
        for j in range(len(puzzleList[i]) - 1, -1, -1):
            backwardList[i].append(puzzleList[i][j])
    temp = forward_and_basis_for_other_functions(backwardList, word)
    if temp != "N":
        temp.setColumn(9 - temp.getColumn())
    return temp


#purpose: checks for given word spelled backward
#list + String --> Point
#def backward(list, word):
    #1) get the length of the given word
    #2) while the word is not found do the following:
          #2.1) go through each character in each line incrementally until we reach the index where the word is no longer possible in that line
                #2.1.1) if the current character matches the current character of the given word (character that starts at length - 1 and then decrements):
                         #2.1.1.1) store start location (point object)
                         #2.1.1.2) move to the next character in both the puzzle and the given word
                         #2.1.1.3) repeat step 2.1.1 without restoring start location
                                    #2.1.1.3.1) if at any point the word is found return start location
                #2.1.2) if not, repeat all of step 2.1 with current character in puzzle if had gone through at least one interation of 2.1.1.
                #2.1.3) else, move one unit forward in the puzzle line and repeat 2.1
          #2.2) move to next line and repeat all of 2.1
          #2.3) if we finish without finding the word return None location


#purpose: checks for given word spelled upward
#list + String --> Point
def upward(puzzleList: list, word: str):
    upwardList = []
    for i in range(len(puzzleList[0])):
        upwardList.append([])
        for j in range(len(puzzleList) - 1, -1, -1):
            upwardList[i].append(puzzleList[j][i])
    temp = forward_and_basis_for_other_functions(upwardList, word)
    if temp != "N":
        newRow = temp.getColumn()
        temp.setColumn(temp.getRow())
        temp.setRow(abs(9-newRow))
    return temp


#purpose: checks for given word spelled upward
#list + String --> Point
#def upward(list, word):
    #1) get the length of the given word
    #2) while the word is not found do the following:
        #2.1) go through each character at a given index value for each string of 10 letters (start at the 0th index, then 1st, etc) where it is possible that the word could be found below
                #2.1.1) if the current character matches the current character of the given word (character that starts at length - 1 an then decrements):
                        #2.1.1.1) store start location (point object)
                        #2.1.1.2) move to the next character in both the puzzle and the given word
                        #2.1.1.3) repeat step 2.1.1 without restoring start location
                                    #2.1.1.3.1) if at any point the word is found return start location
                #2.1.2) if not, repeat all of step 2.1 with current character in puzzle if had gone through at least one interation of 2.1.1.
                #2.1.3) else, move one unit to the next line in the puzzle and repeat 2.1
         #2.2) move to next index value and repeat all of 2.1
         #2.3) if we finish without finding the word return None location


#purpose: checks for given word spelled downward
#list + String --> Point
def downward(puzzleList: list, word: str):
    downwardList = []
    for i in range(len(puzzleList[0])):
        downwardList.append([])
        for j in range(len(puzzleList)):
            downwardList[i].append(puzzleList[j][i])
    temp = forward_and_basis_for_other_functions(downwardList, word)
    if temp != "N":
        newRow = temp.getColumn()
        temp.setColumn(temp.getRow())
        temp.setRow(newRow)
    return temp


#purpose: checks for given word spelled downward
#list + String --> Point
#def downward(list, word):
    #1) get the length of the given word
    #2) while the word is not found do the following:
          #2.1) go through each character at a given index value for each string of 10 letters (start at the 0th index, then 1st, etc) where it is possible that the word could be found below
                #2.1.1) if the current character matches the currrent character of the given word (starts at 0 and increments):
                        #2.1.1.1) store start location (point object)
                        #2.1.1.2) move to the next character in both the puzzle and the given word
                        #2.1.1.3) repeat step 2.1.1 without restoring start location
                                    #2.1.1.3.1) if at any point the word is found return start location
                #2.1.2) if not, repeat all of step 2.1 with current character in puzzle if had gone through at least one interation of 2.1.1.
                #2.1.3) else, move one unit to the next line in the puzzle and repeat 2.1
          #2.2) move to next index value and repeat all of 2.1
          #2.3) if we finish without finding the word return None location


#purpose: checks for given word spelled diagonally
#list + String --> Point
def diagonally(puzzleList: list, word: str):
    diagonalList = []
    diagonalList.append([])
    for i in range(len(puzzleList)):
        for j in range(len(puzzleList[i])):
            if i == j:
                diagonalList[0].append(puzzleList[i][j])
    temp = forward_and_basis_for_other_functions(diagonalList, word)
    if temp != "N":
        temp.setRow(temp.getColumn())
    else:
        temp = backward(diagonalList, word)
        if temp != "N":
            temp.setRow(temp.getColumn())
    return temp


#purpose: checks for given word spelled diagonally
#list + String --> Point
#def diagonally(list, word):
    #1) get the length of the given word
    #2) while the word is not found do the following:
          #2.1) go through each character in each line incrementally until we reach the index where the word is no longer possible diagonally (not enough characters left to the right)
                #2.1.1) if the current character matches the current character of the given word (starts at 0 and increments):
                        #2.1.1.1) store start location (point object)
                        #2.1.1.2) move to the next character in the given word and the next character on the next line in the puzzle (move one unit down diagonally)
                        #2.1.1.3) repeat step 2.1.1 without restoring start location
                                    #2.1.1.3.1) if at any point the word is found return start location
                #2.1.2) if not, repeat all of step 2.1 with the character 1 unit to the right of the location value
          #7.2.2) move to next line and repeat all of 2.1
          #7.2.3) if we finish without finding the word return None location


