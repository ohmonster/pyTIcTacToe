from initBoard import *
from string import printable


boardPositions=initBoardAsPositionList()

def makeColumn(startIndex):
    lastIndex=startIndex+7
    return list(range(startIndex,lastIndex,3))


def defineColumnWinners(firstRow):
    winningCols=[]
    for position in firstRow:
        winningCols.append(makeColumn(position))
    return winningCols

def defineDiagnonalWinners():
    return [[1,5,9],[3,5,7]]


def defineWinningLines():
    rowWinners = splitBoardToRows(boardPositions)
    colWinners = defineColumnWinners(rowWinners[0])
    diagonalWinners = defineDiagnonalWinners()
    return rowWinners+colWinners+diagonalWinners

#showBoard(boardPositions)
#print(defineWinningLines())


