# 1. Dessiner un sapin
# 1.1. Une chaine de caractères
def a_la_chaine(n):
		st=n*'A'
		return st

# 1.2. Une chaine de caractères avec espace avant elle
def a_la_chaine2(esp,n):
	st2=esp*' '+n*'A'
	return st2

# 1.3. Une colonne de caractères
def colonne(n):
	ligne=a_la_chaine(n)+'\n'
	print(10*ligne)

# 1.4. Un triangle rectangle de caractères
def diagonale1(n):
	for i in range(1,n):
		print(i*'A', '\b')

# 1.5. Même chose qu'en 1.4. mais les deux cathètes sont à droite
def diagonale2(n):
	for i in range(1,n):
		print((n-i)*' ', i*'A', '\b') 

# 1.6. Sapin
def sapin(n):
	Numb_espace=n-1
	Numb_A=1
	for i in range(n):
		print (Numb_espace*" " + Numb_A*"A")
		Numb_espace-=1
		Numb_A+=2
	print((n-2)*" " + 3*"A")

# Sapin avec les jouets (de TP3)
import random
def sapin_jouets(n):
	Numb_espace=n-1
	Numb_ligne=0
	for i in range(n):
		ligne=""
		for i in range(2*Numb_ligne+1):
			ligne+="O" if random.random()<0.2 else "*"
		print (Numb_espace*" "+ligne)
		Numb_espace-=1
		Numb_ligne+=1		
	print((n-2)*" " + 3*"*")

# 2. Projet labyrinthe: afficher des images
# 2.1. Le module graph
# 2.1.1. Une fenêtre blanche
import graph
graph.ouvre_fenetre(120,160) # open a window
# so your code will be here
graph.attend_fenetre() # make the opened window stay

# 2.1.2. Un point
graph.plot(20,30) 

# 2.1.3. Une ligne
for x in range (160):
	graph.plot(40,x)

# 2.1.4. Une ligne + fonction
def ligne_horiz(y,larg):
	for x in range(larg):
		graph.plot(y,x)

# 2.2. À vous de jouer
# 2.2.1. Un segment
def segment_horiz(y,x1,x2):
	for x in range(x1,x2):
		graph.plot(y,x)

# 2.2.2. Un rectangle
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

# 2.2.3 Les rayures
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def rayures_vertic(haut,larg,larg_bande):
	nombre=larg//larg_bande
	for n in range(1,nombre,2):
		rayon=rectangle(0,haut, n*larg_bande, (n+1)*larg_bande)

# 2.3. Pour aller plus loin (difficile) :))
# 2.3.1. Un damier
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

# 2.3.2. Un sapin 
принцип как с ёлкой из звёздочек
только здесь вместо звёздочек пиксели
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



	

