# Dessiner un sapin de Noël (est dans TP2)
# 2. Boucle while, nombre mystère
import random
myst=random.randint(0,100)
nombre=int(input("devine le nombre"))
while nombre!=myst:
	if nombre>myst:
		print("moins")
	else:
		print("plus")
	nombre=int(input())
if nombre==myst:
	print("felicitations!")

# 3. Projet labyrinthe : dessiner des images
# 3.0. Exemple donné (écran noir)
import graph
def noir(haut,larg):
	for y in range(haut):
		for x in range(larg):
			graph.plot(y,x)
			
# 3.1. Une ligne noir au début
def bande_noire_gauche(haut,larg,larg_bande):
	for y in range(haut):
		for x in range(larg_bande):
			graph.plot(y,x)

#3.2. Un rectangle noir
def rectangle_noir(haut,larg,y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

# 3.3.1. Un rectangle blanc VERSION 1
def rectangle_blanc(haut,larg,y1,y2,x1,x2):
	for y in range(haut):
		for x in range(x1):
			graph.plot(y,x)
	for x in range(x1,x2):
		for y in range (y1):
			graph.plot(y,x)
	for x in range(x1,x2):
		for y in range (y2,haut):
			graph.plot(y,x) 
	for y in range(haut):
		for x in range(x2,larg):
			graph.plot(y,x)

# 3.3.2. Un rectangle blanc VERSION 2
def rectangle_blanc(haut,larg,y1,y2,x1,x2):
	for y in range(haut):
		for x in range(larg):
			if x1>x or x>x2 or y1>y or y>y2:
				graph.plot(y,x)

# 4. et 5. Nnuméros de bandes noirs et blanches
''' num_bande=x//larg_bande
noire: num_bande%2!=0
blanche: num_bande%2==0 '''

# 6. Les rayures verticales avec comparaison
def rayures_vertic_new(haut,larg,larg_bande):
	for y in range(haut):
		for x in range(larg):
			num_bande=x//larg_bande
			if num_bande%2!=0:
				graph.plot(y,x)

''' or like this:
x_i=x%(2*larg_bande)
if a<=x_i<=2*larg_bande:
graph.plot(y,x)
'''
#  9.1. Un damier avec comparaison VERSION 1
def damier_new(haut,larg,larg_bande):
	for y in range(haut):
		for x in range(larg):
			num_bande_horiz=x//larg_bande
			num_bande_vertic=y//larg_bande
			if (num_bande_horiz%2==0 and num_bande_vertic%2==0) or (num_bande_horiz%2!=0 and num_bande_vertic%2!=0):
				graph.plot(y,x)

# 9.2. Un damier avec comparaison VERSION 2
def damier_new(haut,larg,larg_bande):
	for y in range(haut):
		for x in range(larg):
			x_i=x%(2*larg_bande)
			y_i=y%(2*larg_bande)
			if (0<=x_i<=larg_bande and 0<=y_i<=larg_bande) or (larg_bande<=x_i<=(2*larg_bande) and larg_bande<=y_i<=(2*larg_bande)):
				graph.plot(y,x)

# 10. Un damier multicolore
''' DOESN'T WORK PROPERLY: creats damier where every case is made by pixels of different colors '''
import random
def damier_multicolore(haut,larg,larg_bande):
    numb_couleur=random.randint(0,9)
    couleur=["black","white","red","green","blue","yellow","cyan","magenta","orange","darkgrey"]
    couleur_chosi=couleur[numb_couleur]
    for y in range(haut):
        for x in range(larg):
            numb_couleur=random.randint(0,9)
            couleur_chosi=couleur[numb_couleur]
            num_bande_horiz=x//larg_bande
            num_bande_vertic=y//larg_bande
            if (num_bande_horiz%2==0 and num_bande_vertic%2==0) or (num_bande_horiz%2!=0 and num_bande_vertic%2!=0):
                graph.plot(y,x,couleur_chosi)
			
graph.ouvre_fenetre(120,160)
damier_multicolore(120,160,20)
graph.attend_fenetre()