# Paul Clarke
# tic tac toe or nots & crosses
# each player designated by a chain of characters of length 1 'X' or 'O'

noms = ('X', 'O')

def affiche_morpion(grille):
    taille = len(grille)
    print("   "+"   ".join(str(i) for i in range(taille)))
    lignes = [str(i)+"  "+" | ".join(grille[i]) for i in range(len(grille))]
    div = "\n  "+"---+"*(taille-1)+"---\n"
    print(div.join(lignes))


def creer_ligne(n):
    ligne = []
    for i in range(n):
        ligne += [' ']
    return ligne

def creer_grille(n):
    grille = []
    for i in range(n):
        grille += [creer_ligne(n)]
    return grille

def joueur_suivant(pion, nomLst):
    if nom == nomLst[1]:
        return 'O'
    else:
        return 'X'

def inserer(coord, grille, pion):
    if (coord[0] < 3 and coord[0] >= 0) and (coord[1] < 3 and coord[1] >= 0) and (grille[coord[0]][coord[1]] == ' '):
            grille[coord[0]] = grille[coord[0]][:coord[1]] + [pion] + grille[coord[0]][coord[1]:]
            return True
    else:
        return False

def ligne_gagnante(grille, ligne, pion, long):
    for i in range(long):
        if grille[ligne][i] != pion:
            return False
    return True

def colone_gagnante(grille, col, pion, long):
    for i in range(long):
        if grille[i][col] != pion:
            return False
    return True

def diagonale_descendante_gagnante(grille, pion, long):
    for i in range(long):
        if grille[i][i] != pion:
            return False
    return True

def diagonale_montante_gagnante(grille, pion, long):
    for i in range(long):
        if grille[i][-(i+1)] != pion:
            return False
    return True


def coup(grille, joueur):
    joueur_input_lign = input('Jouer ' + joueur + ': quelle ligne?') 
    joueur_input_colonne = input('Jouer ' + joueur + ': quelle collone?')
    if inserer((int(joueur_input_lign), int(joueur_input_colonne)), grille, joueur) == False:
        print("Coup Invalide")
        return False
    else:
        inserer((int(joueur_input_lign),int(joueur_input_colonne)), grille, joueur)
        return True

# noms = ('x', 'o')

# def jeu(size, noms, joueur, turns = 0):
#     thisGrille = creer_grille(size)
#     if turns <= size*size:
#         valide = False
#         valide = coup(thisGrille, joueur)
#         affiche_morpion(thisGrille)
#         if ligne_gagnante() or colone_gagnante or diagonale_descendante_gagnante or diagonale_montante_gagnante ==

#     return joueur + ' wins!'

# Tests
# print(creer_ligne(8))
# print(creer_grille(8))
# affiche_morpion(creer_grille(3))
# print(joueur_suivant('O', ('O', 'X')))   # 'X'0
# print(joueur_suivant('X', ('O', 'X')))   # 'O'
# grille = creer_grille(3)
# valide = inserer((0,0),grille,'O')
# print(valide)
# valide = inserer((3,0),grille,'O')
# print(valide)
# valide = inserer((1,1),grille,'X')
# print(valide)
# valide = inserer((1,1),grille,'X')
# print(valide)
# affiche_morpion(grille)
# grille1 = [['O',' ','O'],
#             ['O','X',' '],
#             ['O','O','X']]
# grille2 = [['X',' ','O'],
#             ['O','X',' '],
#             ['X','O','O']] 

# print(colone_gagnante(grille1,0, 'O',3))
# print(colone_gagnante(grille2,0, 'O',3))

# grille1 = [['X',' ','O'],
#         ['O','X',' '],
#         ['X','O','X']]
# grille2 = [['X',' ','O'],
#        ['O','X',' '],
#        ['O','O','O']] 

# print(diagonale_descendante_gagnante(grille1,'X',3)) # True
# print(diagonale_descendante_gagnante(grille2,'X',3)) # False

# grille1 = [['X',' ','O'],
#        ['X','O',' '],
#        ['O','O','X']]
# grille2 = [['X',' ','O'],
#        ['O','X',' '],
#        ['X','O','O']] 

grille = [['X',' ','O'],
        ['O','X',' '],
        ['X','O','O']] 

# print(diagonale_montante_gagnante(grille1,'O',3)) #True
# print(diagonale_montante_gagnante(grille2,'O',3)) #False

print(coup(grille, 'O')) # le joueur "O" saisi la ligne 1, puis la colonne 1, ça doit afficher True
print(coup(grille, 'X')) # le joueur "X" saisi lui aussi la ligne 1, puis la colonne 1, ça doit afficher "Coup invalide" puis False