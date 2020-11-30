import graph
import Labyrinthe

laby=Labyrinthe.creer(11,15)
"""
for ligne in laby:
	print(ligne)
	
entr=entree(laby)
sort=sortie(laby)
print(entr,sort)
"""

# exercice 1 (l'entrée et la sortie)
def coord(laby,n):
	for ligne in range(len(laby)):
		for colonne in range(len(laby[0])):
			if laby[ligne][colonne]==n:
				return (ligne,colonne)
	return None

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
	
def taille_laby(laby):
	nombre_de_lignes=len(laby)
	nombre_de_colonnes=len(laby[0])
	return (nombre_de_lignes,nombre_de_colonnes)

def voisins_laby_fin(lgn,col,nb_lignes,nb_colonnes):
	nb_lignes,nb_colonnes=taille_laby(laby)
	deplacements=[(0,1),(0,-1),(1,0),(-1,0)]
	lst_voisins=[]
	for (dy,dx) in deplacements:
		if lgn+dy<nb_lignes and col+dx<nb_colonnes:
			lst_voisins+=[(dy+lgn,dx+col)]
	return lst_voisins

def voisins_laby_acc(coord,laby):
	lgn,col=coord
	nb_lignes,nb_colonnes=taille_laby(laby)
	deplacements=[(0,1),(0,-1),(1,0),(-1,0)]
	lst_voisins=[]
	for (dy,dx) in deplacements:
		if lgn+dy<nb_lignes and col+dx<nb_colonnes and laby[lgn+dy][col+dx]!=0:
			lst_voisins+=[(dy+lgn,dx+col)]
	return lst_voisins

# exercice 3 (parcours de cellules)
labyr=[[0,0,0,0,0,0,0],
[0,2,1,1,0,3,0],
[0,0,0,1,0,1,0],
[0,0,0,1,1,1,0],
[0,0,0,0,0,0,0]]

def exploreVoie(laby,depart):
	depart=entree(laby)
	arrive=sortie(laby)
	ca=depart #ca = cellule d'avant
	cc=voisins_laby_acc(ca,laby)[0] #donne le voisin accessible pour ca, cc = cellule courant
	#ligne ci-dessous donne element #0 dans la liste "choix" créée pour cela 
	chemin=[ca]
	choix=voisins_laby_acc(cc,laby)
	while cc!=arrive and len(choix)==2:
		chemin+=[cc]
		if choix[0]==ca:
			ca=cc
			cc=choix[1]
		else:
			ca=cc
			cc=choix[0]
		choix=voisins_laby_acc(cc,laby)
	return [] if cc!=arrive else chemin





