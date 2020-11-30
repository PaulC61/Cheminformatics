import graph

def nextToQueen(row, column):
    return [(row-1,column), (row-1,column+1), (row,column+1), (row+1,column+1), (row+1,column), (row+1,column-1), (row,column-1), (row-1,column-1)]

def isOnChessboard(row,column):
    return (row >= 0 and row < 8) and (column >= 0 and column < 8)

def nNextToQueenFini(row, column, n):
    infinBoardLst = [(row-n,column), (row-n,column+n), (row,column+n), (row+n,column+n), (row+n,column), (row+n,column-n), (row,column-n), (row-n,column-n)]
    restrBoardLst = []
    for i in range(len(infinBoardLst)):
        if isOnChessboard(infinBoardLst[i][0], infinBoardLst[i][1]) == True:
            restrBoardLst += [infinBoardLst[i]]
    return restrBoardLst



print(nNextToQueenFini(3,7,3))

