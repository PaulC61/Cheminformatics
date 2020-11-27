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
  # every element in new list must be the sum of previous elements
lst = [1,5,7]
newlst= [1,6,13]
#Polina's version 
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

def sumPrevious(lst, n=0, newLst = []):
    # do case of single digit list
    # ways it should fail
    # when the lst is empty, when the lst is length 1 (reduce the size)
    # if n == len(lst): this covers zero case,
    # elif: deal with the first index, if n==0, sumPrevious(lst, n+1)
    # else
    if n == len(lst):
        return newLst
    elif n == 0:
        return sumPrevious(lst, n+1, newLst + [lst[n]])
    else:
        return sumPrevious(lst, n+1, newLst + [somme(lst[:n+1])])
        

print(sumPrevious([3, 8, 10, 1]))
    # create new list
    # sum(lst[0])
    #




def somme_prefixe(lst, n = 0):
    lst2=[]
    lst2=[lst[0]+somme(lst[1:])]
    return lst2

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
''' *j'ai pas trop compris la consigne: les elements inférieures à lst[i]
doivent aussi être avant l'indice i dans la liste? En tout cas, j'ai considéré
que non, mais c'est simplement corrigible si jamais'''
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

lst=[3,9,3,4,1,8]

''' réponse: cette fonction rend la liste (lst2) dont les éléments représentent
le nombre d'éléments de la liste donnée (lst) inférieurs ou égaux à l'élément 
lst[i] (*et dans le dernier cas ces éléments sont de plus situés avant lst[i])
de chaque éléments de liste donnée (lst). Donc, elle affiche nouvelle liste (lst2)
qui dans le cas de lst=[3,9,3,4,1,8] est celle-ci: lst2=[1,5,3,3,0,4] '''

  # 4.3. Tri
''' ehm, je comprends pas ce qu'il faut faire '''
def tri(lst):
    lst2=lst
    lstOrdre=ordre(lst)

  # 4.4. Propriétés

 




