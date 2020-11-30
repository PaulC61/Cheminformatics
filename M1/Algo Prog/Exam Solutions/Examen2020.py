### Examen 2019-2020
 ## Contrôle écrit
  
  # 1. Décomposition fonctionnelle
  # 1.1. Fonctions de divisibilité
def estDivisiblePar(n,p):
    return n%p==0

def listeDiviseursStrict(n):
    lstdeDiv=[]
    div=1
    while div<n:
        if n%div==0:
            lstdeDiv+=[div]
        div+=1
    return lstdeDiv

def sommeListe(lst):
    somme=0
    for i in range(len(lst)):
        somme+=lst[i]
    return somme

  # 1.2. Fonctions nombre parfait
def estParfaitJust(n):
    listeDesDiv=listeDiviseursStrict(n)
    sommeDesDiv=sommeListe(listeDesDiv)
    return (n==sommeDesDiv, listeDesDiv)

def sommeVersChaine(lst):
    chaine=''
    for i in range(len(lst)-1):
        chaine+=str(lst[i])+' + '
    chaine+=str(lst[len(lst)-1])
    return chaine

def justifieParfait(n):
    (OuiOuNon,ListeDesDiv)=estParfaitJust(n)
    PrhaseOui='est parfait car égal à la somme de ses diviseurs:'
    PhraseNon='n est pas parfait car différent de la somme de ses diviseurs stricts qui vaut:'
    ChaineDeSomme=sommeVersChaine(ListeDesDiv)
    return (str(n)+' '+PrhaseOui+' '+ChaineDeSomme) if OuiOuNon else (str(n)+' '+PhraseNon+' '+ChaineDeSomme)
    
  # 2. Récursivité
  # 2.1. Indices
def indices(elem,lst):
    listeDesIndices=[]
    for i in range(len(lst)):
        if elem==lst[i]:
            listeDesIndices+=[i]
    return listeDesIndices

  # 2.2. Maximum d’une liste
def maximum(lst):
    if len(lst)==1:
        return lst[0]
    else:
        MaxNombre=maximum(lst[1:])
        return MaxNombre if MaxNombre>lst[0] else lst[0]

  # 2.3. Somme d’une liste
def somme(lst):
    if lst==[]:
        return 0
    else:
        return lst[0]+somme(lst[1:])

  # 2.4. Somme préfixe
  # Polina's version 
''' seems to be not recursive, cause only use the recursive function somme'''
def somme_prefixe(lst):
    lst2=[]
    if len(lst)<=1:
        return lst
    else:
        for i in range(len(lst)):
            lst2+=[somme(lst[:i+1])]
            i+=1
        return lst2
# Paul's version (brilliant)
def sumPrevious(lst, n=0, newLst = []):
    if n == len(lst):
        return newLst
    elif n == 0:
        return sumPrevious(lst, n+1, newLst + [lst[n]])
    else:
        return sumPrevious(lst, n+1, newLst + [somme(lst[:n+1])])        

  # 3. Listes et Tuples
  # 3.1. Distance euclidienne
import math
def distEucl(p,q):
    xp,yp=p
    xq,yq=q
    d=math.sqrt((xq-xp)**2+(yq-yp)**2)
    return d

  # 3.2. Construction Polygone
def construitPoly(lst):
    listePoly=[]
    for i in range(len(lst)):
        if i<len(lst)-1:
            listePoly+=[(lst[i],lst[i+1])]
        if i==(len(lst)-1):
            listePoly+=[(lst[i],lst[0])]
    return listePoly

  # 3.3. Périmètre
def perimPolyg(listePoly):
    perim=0
    for i in range(len(listePoly)):
        cote=distEucl(listePoly[i][0],listePoly[i][1])
        perim+=cote
    return perim

  # 3.4. Découpe
def decoupe(listePoly,k):
    liste1=[]
    liste2=[]
    for i in range(k):
        liste1+=[listePoly[i][0]]
    for i in range(k,len(listePoly)):
        liste2+=[listePoly[i][0]]
    return liste1, liste2

  # 3.5. Insertion d’un sommet
def insertSommet(listePoly,p,k):
    liste1,liste2=decoupe(listePoly,k)
    if k<1 or k>len(listePoly):
        return listePoly
    if k==len(listePoly):
        listeALaFin=liste2+[p]+liste1
        poly=construitPoly(listeALaFin)
    else:
        listeNouvPoly=liste1+[p]+liste2
        poly=construitPoly(listeNouvPoly)
    return poly

  # 4. Tri d’une liste
  # 4.1. Compte
def compte(lst,i):
    nombreElemInfOuEg=0
    for elem in lst:
        if elem<lst[i] or elem==lst[i] and elem in lst[:i]:
            nombreElemInfOuEg+=1
    return nombreElemInfOuEg

''' fonction pour moi, pas dans l'exercice
def indice(lst,i):
    for x in range(len(lst)):
        if lst[x]==i:
            indice=x
    return indice'''

  # 4.2. Ordre
def ordre(lst):
    lst2=[]
    for i in range(len(lst)):
        lst2+=[compte(lst,i)]
    return lst2

''' réponse: cette fonction rend la liste (lst2) dont les éléments représentent
le nombre d'éléments de la liste donnée (lst) inférieurs ou égaux à l'élément 
lst[i] (*et dans le dernier cas ces éléments sont de plus situés avant lst[i])
de chaque éléments de liste donnée (lst). Donc, elle affiche nouvelle liste (lst2)
qui dans le cas de lst=[3,9,3,4,1,8] est celle-ci: lst2=[1,5,3,3,0,4] '''

  # 4.3. Tri
''' "Trier une liste" means order it in the ascending direction 
the elegant recursive version is in 2018 exam's solution made by Paul (3.3),
here is an iterated version of this function

So, as I understood, this function should sort the list lst based on lst2 obtained
by function ordre, which actually gives us the information of future index of the element 
in new list lst2 created by function tri. It means that for 1 in lst we obtain 0 in lst2,
so this is the min number in lst. For 9 in lst we obtain 5 in lst2 == len(lst), so this 
is the max number, cause other 4 elements is smaller than this element'''

def tri(lst):
    lst2=lst
    lstOrdre=ordre(lst)
    for i in range(len(lstOrdre)-1):
        minimum=i
        nextElement=i+1
        while nextElement<len(lstOrdre):
            if lst2[nextElement]<lst2[minimum]:
                minimum=nextElement
            nextElement+=1
        lst2[i],lst2[minimum]=lst2[minimum],lst2[i]
    return lst2

  # 4.4. Propriétés
''' les algorithmes de tri élémentaires (2 types): par sélection et par insertion
--- Version de Paul est par insertion, qui est un tri stable (conservant l'ordre d'apparition des éléments égaux) 
et un tri en place (il n'utilise pas de tableau auxiliaire). La complexité du tri par insertion est Θ(n^2).
--- Version de moi est par sélection, qui est un tri en place (les éléments sont triés directement dans la structure),
un tri stable (l'ordre d'apparition des éléments égaux est préservé) ''' 

## TP noté
  # 1. Les cases accessibles
  # 1.1. Les cases voisines de (lgn,col)
def un_pas_de_dame_inf(lgn,col):
    deplacements=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    lst_voisins=[]
    for (dy,dx) in deplacements:
        lst_voisins+=[(dy+lgn,dx+col)]
    return lst_voisins

  # 1.2. Les cases situées dans la même direction que les voisins de (lgn,col), mais à N cases de (lgn,col)
  # cas d'une échiquier infinie
def N_pas_dame_inf(lgn,col,N):
    deplacements=[(-N,-N),(-N,0),(-N,N),(0,-N),(0,N),(N,-N),(N,0),(N,N)]
    lst_voisins=[]
    for (dy,dx) in deplacements:
        lst_voisins+=[(dy+lgn,dx+col)]
    return lst_voisins

  # 1.3. Savoir si la case(lgn,col) est sur l’échiquier
def est_sur_echiquier(lgn,col):
    return 0<=lgn<8 and 0<=col<8

  # 1.4. Même chose que dans 1.2. mais pour une échiquier finie
def N_pas_dame_fini(lgn,col,N):
    lst_voisins_fini=[]
    lst_voisins_inf=N_pas_dame_inf(lgn,col,N)
    for i in range (len(lst_voisins_inf)):
            if est_sur_echiquier(lst_voisins_inf[i][0],lst_voisins_inf[i][1]):
                lst_voisins_fini+=[lst_voisins_inf[i]]
    return lst_voisins_fini

  # 1.5. Tous les cases accessibles pour una dame
def cases_accessibles_dame(lgn,col):
    lst_cases=[]
    for N in range(1,7):
        lst_cases+=N_pas_dame_fini(lgn,col,N)
    return lst_cases

  # 2. Dessiner des cases
import graph
  # 2.1. Colorier la case de l'échiquier
def dessine_case(lgn,col,lcase,color):
    for x in range(lcase*col,lcase*(col+1)):
        for y in range(lcase*lgn,lcase*(lgn+1)):
            graph.plot(y,x,color)

  # 2.2. Dessine l'échiquier
def rectangle(y1,y2,x1,x2):
	for x in range(x1,x2):
		for y in range(y1,y2):
			graph.plot(y,x)

def echiquier(lcase):
    for m in range (0,8,2):
        for n in range(0,8,2):
            echiquier_1=rectangle(m*lcase,(m+1)*lcase, n*lcase, (n+1)*lcase)
    for m in range (1,8,2):
        for n in range(1,8,2):
            echiquier_2=rectangle(m*lcase,(m+1)*lcase, n*lcase, (n+1)*lcase)
    return echiquier_1,echiquier_2

  # 3. Dessiner les cases accessibles
def dessine_case_accessiles(lgn,col,lcase):
    partie_echiquier=echiquier(lcase)
    lst_cases_accessibles=cases_accessibles_dame(lgn,col)
    for (ligne,colonne) in lst_cases_accessibles:
        partie_rouge=dessine_case(ligne,colonne,lcase,"red")
    
'''graph.ouvre_fenetre(300,400)

graph.attend_fenetre()'''