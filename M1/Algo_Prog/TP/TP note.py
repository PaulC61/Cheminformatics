#Oleneva


def affiche_morpion(grille):
    taille = len(grille)
    print("   "+"   ".join(str(i) for i in range(taille)))
    lignes = [str(i)+"  "+" | ".join(grille[i]) for i in range(len(grille))]
    div = "\n  "+"---+"*(taille-1)+"---\n"
    print(div.join(lignes))

def creer_ligne(n):
    liste=[]
    for i in range(n):
        liste+=[' ']
    return liste

def creer_grille(n):
    liste2=[]
    for i in range(n):
        liste2+=[creer_ligne(n)]
    return liste2

def joueur_suivant(joueur,noms):
    if joueur==noms[0]:
        return noms[1]
    else:
        return noms[0]

def inserer(coord,grille,pion):
    if coord[0]<len(grille) and coord[1]<len(grille[0]) and grille[coord[0]][coord[1]]==' ':
        grille[coord[0]][coord[1]]=pion
        return True
    else:
        return False

def ligne_gagnante(grille,ligne,pion,long):
    counter=0
    for i in range(long):
        if grille[ligne][i]==pion:
            counter+=1
    return counter==long

def colonne_gagnante(grille,col,pion,long):
    counter=0
    for i in range(long):
        if grille[i][col]==pion:
            counter+=1
    return counter==long

def diagonale_descendante_gagnante(grille,pion,long):
    counter=0
    for i in range(long-1):
        if grille[i][i]==grille[i+1][i+1] and grille[i][i]==pion:
            counter+=1
    return counter==(long-1)

def diagonale_montante_gagnante(grille,pion,long):
    counter=0
    for i in range(long-1,0,-1):
        if grille[i][long-1-i]==grille[i-1][long-1-i+1] and grille[i][long-1-i]==pion:
            counter+=1
    return counter==(long-1)

def grille_gagnante(grille,pion,long):
    for i in range(len(grille)):
        cas1=ligne_gagnante(grille,i,pion,long)
        cas2=colonne_gagnante(grille,i,pion,long)
        cas3=diagonale_descendante_gagnante(grille,pion,long)
        cas4=diagonale_montante_gagnante(grille,pion,long)
    return cas1 or cas2 or cas3 or cas4

