import graph


def isOnChessboard(row,column):
    return (row >= 0 and row < 8) and (column >= 0 and column < 8)

def nextToQueenFini(row, column):
    infinBoardLst=[(row-1,column), (row-1,column+1), (row,column+1), (row+1,column+1), (row+1,column), (row+1,column-1), (row,column-1), (row-1,column-1)]
    restrBoardLst = []
    for i in range(len(infinBoardLst)):
        if isOnChessboard(infinBoardLst[i][0], infinBoardLst[i][1]) == True:
            restrBoardLst += [infinBoardLst[i]]
    return restrBoardLst


def N_ToQueenFini(row, column, n):
    infinBoardLst = [(row-n,column), (row-n,column+n), (row,column+n), (row+n,column+n), (row+n,column), (row+n,column-n), (row,column-n), (row-n,column-n)]
    restrBoardLst = []
    for i in range(len(infinBoardLst)):
        if isOnChessboard(infinBoardLst[i][0], infinBoardLst[i][1]) == True:
            restrBoardLst += [infinBoardLst[i]]
    return restrBoardLst

def availableMoves(row, column):
    lstAvailSpaces = []
    for i in range(1, 8):
        if N_ToQueenFini(row, column, i) != []:
            lstAvailSpaces += N_ToQueenFini(row, column, i)
        else:
            return lstAvailSpaces



print(availableMoves(3,2))

