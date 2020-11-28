# premiere partie: une fenetre blanche
import graph
graph.ouvre_fenetre(120,160) # open a window
# so your code will be here
graph.attend_fenetre() # make the opened window stay

# deuxieme partie: un point
graph.plot(20,30) 

# trosieme partie: une ligne
for x in range (160):
	graph.plot(40,x)

# quatrieme partie: une ligne + fonction
def ligne_horiz(y,larg):
	for x in range(larg):
		graph.plot(y,x)

# exercice 1: un segment
def segment_horiz(y,x1,x2):
	for x in range(x1,x2):
		graph.plot(y,x)

# exercice 1: un carre
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

# exercice 2: les rayures
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def rayures_vertic(haut,larg,larg_bande):
	nombre=larg//larg_bande
	for n in range(1,nombre,2):
		rayon=rectangle(0,haut, n*larg_bande, (n+1)*larg_bande)

# exercice 3: damier
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def damier(haut,larg, cote):
	nombre_horiz=larg//cote
	nombre_vertic=haut//cote
	for m in range (0,nombre_vertic,2):
		for n in range(0,nombre_horiz,2):
			dame_1=rectangle(m*cote,(m+1)*cote, n*cote, (n+1)*cote)
		for m in range (1,nombre_vertic,2):
			for n in range(1,nombre_horiz,2):
				dame_2=rectangle(m*cote,(m+1)*cote, n*cote, (n+1)*cote)

#exercice 4: sapin 	not finished
import graph
def sapin(haut, larg):
	Numb_espace=haut-1
	Numb_point=1
	for i in range(0,9*haut):
		for x in range(larg):
			graph.plot (haut,Numb_espace)
			Numb_espace-=1
			Numb_point+=2
	###for larg in range(haut-2,haut+38):
		###graph.plot(haut,larg)



	

