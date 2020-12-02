### Examen 2017-2018
 ## Contrôle écrit (seulement)
 
  # 1. Les types des variables
ingredient='poivre' #chaine de caracteres
quantite=20 #nombre entier
frais=True #booleen
def creer_ingredient(ingredient,quantite,frais):
    ingredient_decrit=(ingredient,quantite,frais)
    return ingredient_decrit
# so by this step i mean that lst_des_ingredients=[(ingredien_decrit),(...),(...)]

  # 2. Savoir si l'ingrédient est dans ls liste
def est_dans(ing,lst_des_ingredients):
    compteur=0
    for i in range(len(lst_des_ingredients)):
        if lst_des_ingredients[i][0]==ing:
            compteur+=1
    return compteur!=0

  # 3. La quantité totale
def poids_total(lst_des_ingredients):
    poids=0
    for (ingredient,quantite,frais) in lst_des_ingredients:
        poids+=quantite
    return poids

  # 4. Savoir quels ingredients doivent être conservés au frais
def au_frais(lst_des_ingredients):
    lst_au_frais=[]
    for (ingredient,quantite,frais) in lst_des_ingredients:
        if frais==True:
            lst_au_frais+=[ingredient]
    return lst_au_frais

  # 5. Savoir le quantité d'un ingrédient dont le nom est donné
def chercher_quantite(ing,lst_des_ingredients):
    for i in range(len(lst_des_ingredients)):
        if ing==lst_des_ingredients[i][0]:
            return lst_des_ingredients[i][1]
        if not est_dans(ing,lst_des_ingredients):
            return 0

  # 6. Les ingrédients manquants
def courses(recette,placard):
    lst_a_acheter=[]
    for i in range(len(recette)):
        if not est_dans(recette[i][0],placard):
            lst_a_acheter+=[(recette[i][0],recette[i][1])]
        elif est_dans(recette[i][0],placard):
            for j in range(len(placard)):
                if recette[i][0]==placard[j][0]:
                    lst_a_acheter+=[(recette[i][0],abs(placard[i][1]-recette[j][1]))] 
    return lst_a_acheter
  
  # 7. Ingrédients à acheter pour deux recettes
''' I use max_liste and min_liste just to be sure, that all the ingredients wiil be taken into account.
You can try without it, but you will see that if the lenghts of two lists of ingredients are different,
the order of putting lists as arguments of function will influence the resulting list.
For example, if lst1 is shorter than lst2, so contains less ingredients than lst2, the other ingredients of lst2
won't be taken into account (just here, for this script I wrote).
If you know more elegant way to write this function, please, let me know :))'''
def rassembler(lst_des_ingredients1,lst_des_ingredients2):
    lst_commun=[]
    max_liste=[]
    min_liste=[]
    if len(lst_des_ingredients1)>=len(lst_des_ingredients2):
        max_liste=lst_des_ingredients1
        min_liste=lst_des_ingredients2
    else:
        max_liste=lst_des_ingredients2
        min_liste=lst_des_ingredients1
    for i in range(len(max_liste)):
        if not est_dans(max_liste[i][0],min_liste):
            lst_commun+=[(max_liste[i][0],max_liste[i][1])]
        elif est_dans(max_liste[i][0],min_liste):
            for j in range(len(min_liste)):
                if max_liste[i][0]==min_liste[j][0]:
                    lst_commun+=[(max_liste[i][0],max_liste[i][1]+min_liste[j][1])]
    return lst_commun

  # 8. Donner les résultats des fonctions écrites à une recette donnée
ma_recette=[('beurre',250,True),('sucre',50,False),('farine',200,False),('pommes',600,False),('badiane',10,False)]
mon_placard=[('lardons',150,True),('sucre',500,False),('farine',100,False),('pommes',1000,False),('badiane',5,False)]
'''réponces:
print(poids_total(ma_recette)) donne 1110
print(au_frais(ma_recette)) donne ['beurre']
print(est_dans('farine',ma_recette)) donne True
print(est_dans('lait',ma_recette)) donne False
print(chercher_quantite('pommes',ma_recette)) donne 600
print(courses(ma_recette,mon_placard)) donne [('beurre', 250), ('sucre', 450), ('farine', 100), ('pommes', 400), ('badiane', 5)]'''
  
  # 9. Désolé, je comprends pas la consigne 