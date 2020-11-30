
#%%
import Labyrinthe
import TP4
laby = Labyrinthe.creer(15,11)
for line in laby:
    print(line)

def findRed(laby):
    for y in range (len(laby)):
        for x in range (len(laby[0])):
            if laby[y][x] == 3:
                isRedThere = True
                return y, x
    if isRedThere == False:
        return None

def findBlue(laby):
    isBlueThere = False
    for y in range (len(laby)):
        for x in range (len(laby[0])):
            if laby[y][x] == 2:
                isBlueThere = True
                return y, x
    if isBlueThere == False:
        return None  

# print(findBlue(laby))
# print(findRed(laby))
# TP4.draw_grid(laby, 30)


# %%
