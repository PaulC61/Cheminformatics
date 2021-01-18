import graph
import TP4



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

# def rectangle(y1, y2, x1, x2, color):
# 	for x in range(x1, x2):
# 		for y in range(y1, y2):
# 			graph.plot(y,x, color)

def drawCell(row, column, size, color):
    TP4.rectangle(row*size, row*size+size, column*size, column*size+size, color)
    return None

def chessBoard(cellSize): 
    graph.ouvre_fenetre(cellSize*8,cellSize*8)
    for y in range(cellSize*8):
        for x in range(cellSize*8):
            if ((x%cellSize == 0) and (y%cellSize == 0)) and (((x//cellSize)+(y//cellSize))%2 == 0):
                drawCell(x//cellSize, y//cellSize, cellSize, "black")
            elif (x%cellSize == 0) and (y%cellSize==0):
                drawCell(x//cellSize, y//cellSize, cellSize, "white")
    

def drawAvailableMoves(row, column, cellSize):
    drawLst = availableMoves(row, column)
    for i in range(len(drawLst)):
        drawCell(drawLst[i][0], drawLst[i][1], cellSize, "red")
    return None

chessBoard(40)
drawAvailableMoves(3, 4, 40)
graph.attend_fenetre()