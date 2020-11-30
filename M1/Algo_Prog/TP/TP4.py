

#%%
import graph
intlst = [10,0,30,100,500]
couleurs = ["rouge", "orange", "jaune", "vert", "bleu", "indigo", "violet"]
exampleList = [1,1,0,0,1,0,1,0,1,0,1,1,1,0]

lstlst = [[0, 1, 1, 0, 1, 1, 1, 0],
		  [1, 0, 0, 1, 1, 0, 0, 1],
		  [0, 1, 0, 1, 1, 0, 0, 1],
		  [0, 1, 0, 1, 0, 0, 1, 1],
		  [1, 0, 1, 0, 0, 1, 1, 0],
		  [1, 1, 0, 0, 0, 1, 0, 1]]

def multiLoop(lst):
	for i in range (len(lst)):
		lst[i] *= 2
	return lst



def sexyNumbers():
	lst=[]
	for i in range (1,101):
		if i%2==0 or i%3==0 or (i%2 == 0 and i%3 ==0):
			lst=lst + [i]
	return lst

def copyAndMulti(lst):
	newlst = lst
	for i in range (len(newlst)):
		newlst[i] *= 2
	return newlst
	
def neighbour_pixels(y,x):
	lstNeighCoord=[(y,x+1),(y+1,x),(y,x-1),(y-1,x)]
	
	return lstNeighCoord
	
def lengthOfImage(lst, band_width):
	totalLength = (len(lst))*band_width
	
	return totalLength

def band_num(x, band_width):
	bandNum = x//band_width
	
	return bandNum
	
def draw_bands(bandLst, height_band, width_band):
	totalLength = lengthOfImage(bandLst,width_band)
	graph.ouvre_fenetre(height_band,totalLength)
	
	for y in range(height_band):
		for x in range(totalLength):
			if bandLst[band_num(x,width_band)] == 1:
				graph.plot(y,x)
	graph.attend_fenetre()

def rectangle(y1, y2, x1, x2, color):
	for x in range(x1, x2):
		for y in range(y1, y2):
			graph.plot(y,x, color)

def draw_bands2(bandLst, height_band, width_band):
	totalLength = lengthOfImage(bandLst, width_band)
	graph.ouvre_fenetre(height_band, totalLength)

	for bandStart in range(0,totalLength, width_band):
		if bandLst[band_num(bandStart,width_band)] == 1:
			rectangle(0, height_band, bandStart, bandStart + width_band)
	graph.attend_fenetre()
		
def numberOfRows(theList):
	numberRow = len(theList)
	
	return numberRow

def numberOfColumns(theList):
	numberColumn = len(theList[1])

	return numberColumn

def sizeOfImage(theList, size):
	height = numberOfRows(theList)*size
	width = numberOfColumns(theList)*size

	return height,width

def draw_grid(theList, size):
	graphHeight = sizeOfImage(theList, size)[0]
	graphWidth = sizeOfImage(theList, size)[1]
	
	graph.ouvre_fenetre(graphHeight, graphWidth)
	for y in range (graphHeight):
		for x in range (graphWidth):
			if theList[band_num(y, size)][band_num(x, size)] == 1:
				graph.plot(y, x, 'white')
			else:
				if theList[band_num(y, size)][band_num(x, size)] == 2:
					graph.plot(y, x, 'blue')
				else:
					if theList[band_num(y, size)][band_num(x, size)] == 3:
						graph.plot(y, x, 'red')
					else:
						graph.plot(y, x, 'black')
	graph.attend_fenetre()



# %%
