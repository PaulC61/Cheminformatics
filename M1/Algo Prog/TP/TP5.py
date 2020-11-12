#%%
import Labyrinthe
import myGraph
import TP4
import TP6
laby = [[0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

def index(lstlst, n):
    if n == 2:
        return myGraph.findBlue(lstlst)
    else:
        if n == 3:
           return myGraph.findRed(lstlst)
        else:
            return "Try find something else"

def entrance(lstlst):
    return myGraph.findBlue(lstlst)

def exit(lstlst):
    return myGraph.findRed(lstlst)

def size_laby(lstlst):
    return TP4.numberOfRows(lstlst), TP4.numberOfColumns(lstlst)

def neighbour_laby_pixels(y, x, lstlst):
    lstNeighCoord = []
    if (0 <= y <= size_laby(lstlst)[0]-1) and (0 <= x <= size_laby(lstlst)[1]-1):
    
        if ((y >= 0 ) and (x < size_laby(lstlst)[1]-1)) or ((y >= size_laby(lstlst)[0]-1) and (x < size_laby(lstlst)[1]-1)):
            lstNeighCoord += [(y, x+1)]

        # if (y < size_laby(lstlst)[0]-1) and (x < size_laby(lstlst)[1]-1):
        #     lstNeighCoord += [ (y+1,x+1)]

        if ((y < size_laby(lstlst)[0]-1) and (x > 0)) or ((y < size_laby(lstlst)[0]-1) and (x < size_laby(lstlst)[1]-1)):
            lstNeighCoord += [(y+1,x)]

        # if (y < size_laby(lstlst)[0]-1) and (x > 0):
        #     lstNeighCoord += [(y+1, x-1)]

        if ((y > 0) and (x > 0)) or ((y <= size_laby(lstlst)[0]-1) and (x > 0)):
            lstNeighCoord += [(y, x-1)]

        # if (y > 0) and (x > 0):
        #     lstNeighCoord += [(y-1,x-1)]

        if ((y > 0) and (x >= 0)) or ((y > 0) and (x < size_laby(lstlst)[1]-1)):
            lstNeighCoord += [(y-1, x)]

        # if ((y > 0) and (x < size_laby(lstlst)[1]-1)):
        #     lstNeighCoord += [(y-1, x+1)]
    

    return lstNeighCoord

def neighbour_available_spaces(cell, lstlst):
    lstAllSpaces = neighbour_laby_pixels(cell[0], cell[1], lstlst)
    lstAvailableSpaces = []
    for i in range (len(lstAllSpaces)):
            if lstlst[lstAllSpaces[i][0]][lstAllSpaces[i][1]] != 0:
                lstAvailableSpaces += [lstAllSpaces[i]]

    # for j in range (len(lstAvailableSpaces)):
    #     if (lstAvailableSpaces[j] != myGraph.findRed(lstlst)):
    #         neighbour_available_spaces(lstAvailableSpaces[j], lstlst, lstAvailableSpaces)
    #     else:
    return lstAvailableSpaces


# assuming no fork


def finishLabyrinthe(laby, previousCells = [], currentCell = entrance(laby), nextCells = neighbour_available_spaces(entrance(laby), laby)):
    print(previousCells)
    if exit(laby) in nextCells:
        return previousCells + [exit(laby)]
    
    

    # elif nextCells in previousCells:
    #     return []

    else:
        for i in range(len(nextCells)):
            if nextCells[i] not in previousCells:
                previousCells + finishLabyrinthe(laby, previousCells + [currentCell], nextCells[i], neighbour_available_spaces(nextCells[i], laby))
            else:
                previousCells + []
        return previousCells
        # return finishLabyrinthe(laby, previousCells, currentCell)
    


        # previousCells + finishLabyrinthe(laby, previousCells + [currentCell], nextCells[0], neighbour_available_spaces(nextCells[0], laby))
    # return previousCells
















    # if nextCells == []:
    #     return []

    # elif nextCells in previousCells:
    #      return []
    
    # elif currentCell == exit(laby):
    #     return previousCells
  
    # elif nextCells[-1] in previousCells:
    #     return finishLabyrinthe(laby, previousCells, currentCell, nextCells[:-1])
    # # and then finally move on
    # else:
    #     return finishLabyrinthe(laby, previousCells + [currentCell], nextCells[-1], neighbour_available_spaces(nextCells[0], laby))
       
            



# def exploreLabyrinthe(laby, savedPositions = [entrance(laby)], currentPosition = entrance(laby)):

    # labExit = exit(laby)
    # nextPositions = neighbour_available_spaces(currentPosition, laby)
    # print("Saved Positions: ", savedPositions)
    # print("Next Positions: ", nextPositions)
    # if labExit in savedPositions:
    #     # return savedPositions + [labExit]
    #     return savedPositions[0:savedPositions.index(labExit)]
    # else:
    #     if nextPositions in savedPositions:
    #             savedPositions = []
    #             return savedPositions
    #     else:
    #         for i in range (len(nextPositions)):
                # if nextPositions[i] not in savedPositions:
                #     exploreLabyrinthe(laby, savedPositions + [nextPositions[i]], nextPositions[i])


        # if nextPositions not in savedPositions:
        #     oneRoute = []
        #     for i in range (len(nextPositions)):
        #         print(i)
        #         if nextPositions[i] not in savedPositions: 
        #           oneRoute =  exploreLabyrinthe(laby, savedPositions + [nextPositions[i]], nextPositions[i])
        #           print("One Route", oneRoute)
        #         if labExit in oneRoute:
        #            savedPositions += oneRoute 
        #         else:
        #             savedPositions += []
        #     return savedPositions

    
        


    
        


    # i need to list all available cells to the exit
    
    # neighbour cells function gives me all of them in a radius from one cell

    # I need to get the neighbour cells around the entrance
    # input the neighbour cell available into neighbour cell function
    # block off previous position (maybe using 4) from the next function

    # if the list does not reach the exit, return an empty list, not an available path as such 





index(laby, 2)
size_laby(laby)
print(finishLabyrinthe(laby))
TP4.draw_grid(laby, 25,)

# %%
