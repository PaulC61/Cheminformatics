"""
#exercice 1.1 (multiplier chaque element)
lst=[5,0,50,200]
def multipl_lst(lst):
	for i in range (len(lst)):
		lst[i]*=2
	print (lst)
multipl_lst(lst)
"""
"""
#exercice 1.2 (creer un liste, div 2 ou 3)
lst=[]
for i in range(1,101):
	if i%2==0 or i%3==0:
		lst+=[i]
print (lst)
"""
"""
#exercice 1.3 (creer un nouveau list dont chaque element*2)
lst=[5,0,50,200]
lst2=[]
for i in range (len(lst)):
	lst2+=[lst[i]*2]
print (lst)
print(lst2)
"""
"""
#exercice 1.4 (coordonnees des pixels)
couleurs=["rouge","orange","jaune","vert","bleu","indigo","violet"]

y=int(input("Input coordonne y "))
x=int(input("Input coordonne x "))
def pixels_voisins(y,x):
	deplacement=[(0,1),(0,-1),(1,0),(-1,0)]
	lst_voisins=[]
	for (dy,dx) in deplacement:
		lst_voisins+=(dy+y,dx+x)
	return (lst_voisins)
print (pixels_voisins(y,x))
"""
"""
#exercice 2.1 (dessiner les bandes noires et blanches - parcourir les pixels)
import graph 

def largeur_image(lst,largeur_bande):
	largeur_total=largeur_bande*len(lst)
	return largeur_total
	
def num_bande(y,x,largeur_bandes):
	num_bande=x//largeur_bandes
	return num_bande
		
def dessine_bandes1(lst,hauteur, largeur_bandes):
	largeur=largeur_image(lst,largeur_bandes)
	graph.ouvre_fenetre(hauteur,largeur)
	for y in range(hauteur):
		for x in range(largeur):
			bande=num_bande(y,x,largeur_bandes)
			if lst[bande]==0: 
				graph.plot(y,x)
			
lst=[1,1,0,0,1,0,1,0,1,1,1,0]
dessine_bandes1(lst,50,20)
graph.attend_fenetre()
"""
"""
#exercice 2.2 (dessiner les bandes noires et blanches - dessiner des rectangles)
import graph

def largeur_image(lst,largeur_bande):
	largeur_total=largeur_bande*len(lst)
	return largeur_total

def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)
			
def dessine_bandes2(lst,hauteur, largeur_bandes):
	largeur=largeur_image(lst,largeur_bandes)
	graph.ouvre_fenetre(hauteur,largeur)
	for i in range(len(lst)):
		if lst[i]==0:
			 rect=rectangle(0,hauteur,i*largeur_bandes,(i+1)*largeur_bandes)

lst=[1,1,0,0,1,0,1,0,1,1,1,0]
dessine_bandes2(lst,50,20)
graph.attend_fenetre()
"""
"""
#exercice 3 (lst de lst des bandes)
import graph

lstlst=[[0,1,1,0,1,1,1,0],
[1,0,0,1,1,0,0,1],
[0,1,0,1,1,0,0,1],
[0,1,0,1,0,0,1,1],
[1,0,1,0,0,1,1,0],
[1,1,0,0,0,1,0,1]]

def nb_lignes(lstlst):
	nombre_de_lignes=len(lstlst)
	return nombre_de_lignes

def nb_colonnes(lstlst):
	nombre_de_colonnes=len(lstlst[0])
	return nombre_de_colonnes

def taille_image(lstlst, taille):
	lignes=nb_lignes(lstlst)
	colonnes=nb_colonnes(lstlst)
	hauteur=taille*lignes
	largeur=taille*colonnes
	return (hauteur,largeur)
	
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def dessine_grille(lstlst,taille):
	haut,larg=taille_image(lstlst,taille)
	graph.ouvre_fenetre(haut,larg)
	for ligne in range(nb_lignes(lstlst)):
		for colonne in range(nb_colonnes(lstlst)):
			if lstlst[ligne][colonne]==0:
				rectangle(ligne*taille,(ligne+1)*taille, colonne*taille, (colonne+1)*taille)
	
dessine_grille(lstlst,40)
graph.attend_fenetre()
"""
"""
#exercice 4.2 (labyrinthe)
import graph
import Labyrinthe
laby=Labyrinthe.creer(11,15)

def nb_lignes(laby):
	nombre_de_lignes=len(laby)
	return nombre_de_lignes

def nb_colonnes(laby):
	nombre_de_colonnes=len(laby[0])
	return nombre_de_colonnes

def taille_image(laby, taille):
	lignes=nb_lignes(laby)
	colonnes=nb_colonnes(laby)
	hauteur=taille*lignes
	largeur=taille*colonnes
	return (hauteur,largeur)
	
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def dessine_grille(lstlst,taille):
	haut,larg=taille_image(lstlst,taille)
	graph.ouvre_fenetre(haut,larg)
	for ligne in range(nb_lignes(lstlst)):
		for colonne in range(nb_colonnes(lstlst)):
			if lstlst[ligne][colonne]==0:
				rectangle(ligne*taille,(ligne+1)*taille, colonne*taille, (colonne+1)*taille)
	
dessine_grille(laby,40)
graph.attend_fenetre()
"""

#exercice 4 (labyrinthe)
import graph
import Labyrinthe
laby=Labyrinthe.creer(11,15)
	
def entree(laby):
	for ligne in range(len(laby)):
		for colonne in range(len(laby[0])):
			if laby[ligne][colonne]==2:
				return (ligne,colonne)
	return None
	
def sortie(laby):
	for ligne in range(len(laby)):
		for colonne in range(len(laby[0])):
			if laby[ligne][colonne]==3:
				return ligne,colonne
	return None

def taille_image(laby, taille):
	lignes=len(laby)
	colonnes=len(laby[0])
	hauteur=taille*lignes
	largeur=taille*colonnes
	return (hauteur,largeur)
	
def rectangle(y1,y2,x1,x2,colour="black"):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x,colour)

def dessine_labyrinthe(laby,taille):
	haut,larg=taille_image(laby,taille)
	graph.ouvre_fenetre(haut,larg)
	for ligne in range(len(laby)):
		for colonne in range(len(laby[0])):
			if laby[ligne][colonne]==0:
				rectangle(ligne*taille,(ligne+1)*taille, colonne*taille, (colonne+1)*taille)
	e1,e2=entree(laby)
	s1,s2=sortie(laby)
	rectangle(e1*taille,(e1+1)*taille, e2*taille, (e2+1)*taille,"blue")
	rectangle(s1*taille,(s1+1)*taille, s2*taille, (s2+1)*taille,"red")
			
dessine_labyrinthe(laby,40)
graph.attend_fenetre()
		


	
			


















