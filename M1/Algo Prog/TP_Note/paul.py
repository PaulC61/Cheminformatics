import graph

def nextToQueen(row, column):
    return [(row-1,column), (row-1,column+1), (row,column+1), (row+1,column+1), (row+1,column), (row+1,column-1), (row,column-1), (row-1,column-1)]

def nNextToQueen(row, column, n):
    return [(row-n,column), (row-n,column+n), (row,column+n), (row+n,column+n), (row+n,column), (row+n,column-n), (row,column-n), (row-n,column-n)]

def isOnChessboard(row,column):
    return (row >= 0 and row < 8) and (column >= 0 and column < 8)

print(nNextToQueen(3,7,3))
print(isOnChessboard(7,0))

