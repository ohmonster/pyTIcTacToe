def initBoardAsPositionList(): 
    return list(range(1,10))

def splitBoardToRows(playingBoard): 
    gameRows= [playingBoard[:3], playingBoard[3:6],playingBoard[6:]]
    return gameRows


def showBoard(playingBoard,boardTitle=""):
    if len(boardTitle)>0:
        print(boardTitle)
        
    for row in splitBoardToRows(playingBoard):
        strRow=(str(i) for i in row)
        numberedBoard = " ".join(strRow)
        print(numberedBoard)

#def showBoardWithoutPositions(playingBoard,boardTitle=""):

