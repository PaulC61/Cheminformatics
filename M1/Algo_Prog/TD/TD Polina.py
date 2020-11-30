# The most useful functions written during TDs
# Fonction les plus importantes ecrites pendant les TPs

### TD2: types de base, expressions, variables, repetitions, fonctions

# 2: boucles "for" et "while"
# 2.5. somme des entiers pairs entre 0 et N
def somme_entiers_pairs(N):
    somme=0
    for i in range(0,N+1,2):
        somme+=i
    return somme

# 2.6. factoriel de N
def factoriel(N):
    produit=1
    for i in range(1, N+1):
        produit*=i
    return produit

### TD3: boleens et conditionnelles

# 3: divisibilite
# 3.3. annee bissextiles
def estBissextile(n):
    return n%400==0 or n%4==0 and n%100!=0       

# 3.4. nombre de jours dans un mois
def estPairs(n):
    return n%2==0    

def nbJoursDansMois(mois,annee):
    y=estPairs(mois)
    if 1<=mois<=12:
        if 1<=mois<=7:
            if y==False:
                return(31)
            if y==True and mois!=2:
                return(30)
            if mois==2:
                z=estBissextile(annee)
                if z==True:
                    return(29)
                else:
                    return(28)
        if 8<=mois<=12:
            if y==True:
                return(31)
            else:
                return(30)

# donne la date d'un jour qui est apres celui qu'on tape 
def jourApres(jour,mois,annee):
    nannee=annee
    nmois=mois
    njour=jour+1
    if jour==nbJoursDansMois(mois,annee):
        njour=1
        nmois=mois+1
    else:
        njour=jour+1
        nmois=mois
        nannee=annee
    if nmois==13:
        nmois=1
        nannee=annee+1
    return njour, nmois, nannee

# 4: tirage au sort
# 4.3. produit la chaine de caracters (40 caracteres) contienne 
# des * et O # distribue de facon aleatoire 
# et que la probabilite d'avoir * soit de 80%
import random
ligne=""
for i in range(40):
    if random.random() < 0.2:
        ligne=ligne+"*"
    else:
        ligne=ligne+"O"

# 5: boucles "while"
# 5.2.deux nombre pris au hasard, dont la somme est paire
def deuxSommePaire():
    a=1
    b=2
    "car pour tirage il faut entrer dans la boucle"
    while (a+b)%2:
        "(a+b)%2 peur etre egale a True ou a False, cela egale a 1 ou 0"
        a=random.randint(0,6) #ici on cherche le nombre entre 0 et 6
        b=random.randint(0,6)
    print(a,b)

# 6: les nombres premiers
# 6.1. si le nombre est premier (qui n'est divisible que par 1)
def estPremier(n):
    div=2 #diviseur
    while n%div!=0:
        div+=1
    return div==n

# 6.2. affichage de tous les nombres premiers avant un nombre n
def nombresPremiers(n):
    # version 1:
    for i in range(n):
        nombre=estPremier(i)
        print(nombre)
    # version 2:
    i=2
    while i<n:
        nombre=estPremier(i)
        print(nombre)

### TD4: tuples et listes

#2: lecture simple et modification en place
# 2.1. parcourt la liste et affiche ses elements multiplies par 2
# ne modifie pas la liste!
for e in lst:
    print(2*e)

# 2.2. meme chose que 2.1., mais en modifiant la liste donnee
# "effet de bord" - le fait qu'on modifie la liste donnee
# version 1:
for i in range(len(lst)):
    lst[i]*=2
# version 2:
for (i,e) in enumerate(lst):
    lst[i]=2*e

# 2.3. similare aux 2.1. et 2.2., mais on ecrit une fonction
def doubler(lst):
    lst2=[]
    for e in lst:
        lst+=[2*e]
    return lst2

# 2.4. transforme la chaine de carateres en liste des entiers
def strToIntList(lst):
    lst2=[]
    for e in lst:
        lst2+=[lst(e)]
    return lst2

# 3: lecture simple de listes
# 3.1. cherche 3 dans une liste
def contientUn3(lst):
   # version 1:
    il_y_est=False #par defaut il n'y a pas un 3 dans la liste donnee
    i=0
    while i<len(lst) and not il_y_est:
        il_y_est=(lst[i]==3)
        i+=1
    return il_y_est
    # version 2:
    i=0
    while i<len(lst) and lst[i]!=3:
        i+=1
    return not i==len(lst) #or i!=len(lst)

# 3.2. nombre d'elements pairs dans la liste donnee
def comptePairs(lst):
    nombre=0
    for e in len(lst):
        if lst[e]%2==0:
            nombre+=1
    return nombre

# petite remarque: on utilise boucle "for" quand on sait qu'on veut
# parcourir toute la liste definitivement
# on utilise boucle "while" quand on ne sait pas ou et quand
# on va s'arreter en parcourant la liste

# 3.3. minimum d'une liste
def minimum(lst):
    if len(lst)==0:
        print("ca va pas")
        return None
# donc, la precondition est lst!=[]
    a=1
    min=lst[0]
    while a<len(lst):
        if lst[a]<min:
            min=lst[a]
        a+=1
    return min

# 3.4. l'indice de dernier element egale a "a_trouver"
def indiceDernier(lst,a_trouver):
    l=len(lst)
    for i in range(l-1,-1,-1): #donne la liste enversee
    # mais il vaut mieux utiliser boucle while ici:
        l=len(lst)-1
    while l>=0 and lst(l)!=a_trouver:
        l-=1
    return l  

# 3.5. savoir si la liste est croissante ou pas
def estCroissante(lst):
    i=0
    while 1<(len(lst)-1) and lst[i]<=lst[i+1]:
        i+=1
    return i==len(lst)-1

# 4: construire une nouvelle liste
# 4.1. creer une lsite de n-elements egaux a 5
def cinqALaChaine(n):
    lst=[]
    for i in range(n):
        lst+=[5] # LES CROCHETS!
    return lst

# 4.2. creer une liste de n-elements represantants les flottants choisis au hasard entre 0 et 1
import random
def listeAlea(n):
    lst=[]
    for i in range(n):
        lst+=[random.random()] # LES CROCHETS!
    return lst # or return [5 for i in range(n)]

# 4.3. donne la liste des nombre premiers en utiisant la fonction estPremier (6.1. en TP3)
def listePremiers(n):
    lst=[]
    i=0
    while len(lst)<n:
        i+=1
        if estPremier(i):
            lst+=[]
    return lst

# 4.4. supprime un element dans la liste
def supprimeN(lst,a_supprimer):
    lst2=[]
    for e in lst:
        if e!=a_supprimer:
            lst2+=[a_supprimer]
    return lst2

# 4.5. inverser la liste
def inverser(lst):
    lst2=[]
    for i in range(len(lst)-1,-1,-1):
        lst2+=[lst[i]]
    return lst2

# 4.6. inserer un element dans la liste croissante
def insereCroiss(lst,a_inserer):
    lst2=[]
    i=0
    while i<len(lst) and a_inserer>lst[i]:
        lst2+=[lst[i]] # LES CROCHETS!
        i+=1
    lst2+=[a_inserer]
    while i<len(lst):
        lst2+=[lst[i]]
        i+=1
    return lst2

# 5: listes de listes
# 5.2. modifie la grille de facon a ce que la premiere ligne soit uniquement
# constituee de 1, le deuxieme ligne - de 2, la ligne n - de n
# grille=[[0,0,0,0,0,][meme chose][meme chose]]
# version 1:
def mgrille(haut,larg):
    for ligne in range(haut):
        for colonne in range(larg):
            grille[ligne][colonne]=ligne+1
# version 2:
def modif_grille(grille):
    hauteur=len(grille)
    largeure=len(grille[0])
    for ligne in range(hauteur):
        for colonne in range(largeure):
            grille[ligne][colonne]=ligne+1

# 5.3. generer une grille
haut=int(input())
larg=int(input())
def gen_grille(haut,larg):
    grille=[]
    for e in range(haut):
        ligne=[] # or larg=ligne*[e+1] - apres grille+=[ligne]
        for e in range(larg):
            larg+=[e+1]
        grille+=[ligne]
    return grille

### TD5: fonctions
# 1: le codage des caracteres
# 1.1. codage par les entiers: savoir si le suel caractere est minuscule
# ord - fonction qui retourne le code (entier) d'un caractere
# chr - fonction qui retourne le caractere a partir d'un code
def estMinuscule(str):
    if 97<=ord(str)<=122:
        return True
    else:
        return False
# mieux vaut ecrire: return ord("a")<=ord(str)<=ord("z")

# 1.2.2.1. decalage d'un caractere minuscule dans la chaine, les autres restent comme ils etaient avant
def decalageCar(str,decal):
    if not estMinuscule(str):
        return str
    else: 
        return ((ord(str)-ord("a"))+decal)%26+ord("a") 

# 1.2.2.2. tous les caracteres de chaine "message" sont decales
def decalageStr(message, decal):
    res=''
    for c in message:
        res+=decalageCar(c,decal)
    return res

# 1.2.2.3. coder une chaine de caracteres "message" avec decalage=5
def codage(message):
    a=decalage(message,5)
    return a

# 1.2.2.4. l'inverse de 1.2.2.3.
def decodage(message):
    a=decalage(message,-5)
    return a

# 3: arithmetique
# 3.1. savoir si n est divisible par b
def estDivisiblePar(n,b):
    n=abs(n)
    while n>0:
        n-=b
    return n==0

# 3.2. retourne le quotient de la division eucledienne de n par b
def quotientDivision(n,b):
    n=abs(n)
    q=0
    while n>=b:
        n-=b
        q+=1
    return q

# 3.3. a partir d'un entier n retourne nombre de chiffres de cet entier en base 10
def nbChiffres(n,base=10):
    l=0
    while n!=0:
        n//base
        l+=1
    return l

# 4: fractions
# 4.1. saisir la fraction sous forme d'un tuple
# num = numerateur
# den = denominateur
def frac_input():
    num=int(input("entrez le numerateur"))
    den=int(input("entrez le denominateur"))
    return num,den

# 4.2. saisir la fraction sous forme d'une chaine de caracteres
def frac_str(f):
    (n,d)=f # unpacking
    return str(n)+"/"+str(d) # or: return str(f[0])+"/"+str(f[0])

# 4.3. multiplications des fractions
def frac_mult():
    (n1,d1)=f1
    (n2,d2)=f2
    return n1*n2,d1*d2

# 4.4. fraction normalisee 
# pgcd = plus grand diviseur commun
def pgcd(a,b):
    # version ecrit par m. Schreck:
    while b!=0:
        a,b=b,a%b
    return a
    # version (recursive) du livre:
    r=a%b
    if r==0:
        return b
    else:
        return pgcd(b,r) 

def frac_normalize(f):
    (n,d)=f
    if n<=0 and d>0 or n>=0 and d<0:
        sign=-1
    else:
        sign=1
    p=pgcd(n,d)
    return sign*abs(n)//p, abs(d)//p

### TD6: recursivite

# 1: fonctions f(n) qu'on peut exprimer au moyen de f(n-1)
# 1.1. factoriel recursive
def fact_rec(n):
    return 1 if n==0 else n*fact(n-1)

# 1.2. multiplication recursive
def mult_rec(a,b):
    return 0 if b==0 else a+mult_rec(a,b-1)

# 1.3. somme des n premiers entiers
def sommeNPremiersEntiers(n):
    return o if n==0 else n+sommeNPremiersEntiers(n-1)

# 1.4. une fonction qui determine si un entier est premier
# deux etape
# premier: une fonction recursive qui determine si n est divisible par un entier inferier ou egale a p
"""def aUnDiviseur(n,p):
    if p>1:
        return n%p==0 #true
    if p=1:
        return aUnDiviseur(n,p-1) #false"""

def est_Premier(n):
    def aUnDiviseur(n,p):
        return False if p==1 else n%p==0 or aUnDiviseur(n,p-1)
    return not aUnDiviseur(n,n-1) # or (n,n//2)

# 1.5. afficher une chaine de caracteres n fois
def afficheNFois(n,message):
    if n!=0: #or >
        print(message)
        afficheNFois(n-1,message)

# 4: fonctions f(n) qu'on peut exprimer au moyen de f(n-1) et f(n-2)
# 4.1. fibonacci iteratif
def fiboIter():
    u1,u0=1,1
    for i in range(n):
        u1,u0=u1+u0,u1
    return u0

# 4.2. fibonacci recursif
def fiboRec():
    return 1 if n<=1 else fiboRec(n-1)+fiboRec(n-2)

# 5: fonctions portant sur des listes
# 5.1: calcul d'un nombre caracterisant la liste
# 5.1.1. somme des entiers de liste (recursive)
def sommeListe(lst):
    # version 1:
    if lst==[]:
        return 0
    else:
        return lst[0]+sommeListe(lst[1:])
    # version 2:
    if lst==[]:
        return 0
    else:
        p,*f=lst
        return p+sommeListe(f)

# 5.1.2. nombre des elements pairs dans la liste (recursif)
def comptePairs(lst):
    # version 1:
    if lst==[]:
        return 0
    elif lst[0]%2==0:
        return 1+comptePairs(lst[1:])
    else:
        return comptePairs(lst[1:]) 
    # version 2: 
    if lst==[]:
        return 0
    p,*f=lst
    if p%2==0:
        return 1+comptePairs(lst[1:])
    else: 
        return comptePairs(lst[1:])

# 5.3. donne l'indice d'un element de la liste egal a a_trouver (recursif)
def indice(lst,a_trouver):
    if lst!=[]:
        if lst[0]==a_trouver:
            return 0
        else:
            return 1+indice(lst[1:],a_trouver)

# 5.2: construction de listes
# 5.2.1. doubler recursif
def doublerRec(lst):
    # version 1:
    if lst==[]:
        return []
    else:
        return [2*lst[0]]+doublerRec(lst[1:])
    # version 2:
    def doubler_bis(lst,i):
        if i<len(lst):
            lst[i]*=2
            doubler_bis(lst,i+1)
    if lst!=[]:
            doubler_bis(lst,0)
    return lst

# 5.2.2. supprimer un element dqns la liste (recursif)
def supprimeRec(lst,a_supprimer):
    if lst==[]:
        return []
    f,*x=lst
    if f!=a_supprimer:
        return [f]+supprimeRec(lst[1:],a_supprimer) # lst[1:]=x
    else:
        return supprimeRec(lst[1:],a_supprimer) # lst[1:]=x

# 5.2.3. insere un element dans une liste croissante (recursif)
def insereDansTrie(lst,a_inserer):
    if lst==[]:
        return [a_inserer]
    p,*f=lst # p=lst[0]  f=lst[1:]
    if a_inserer<=p:
        return [a_inserer]+lst
    else: #pas necessaire
        return [p]+insereDansTrie(f,a_inserer)

# 5.2.4. partager une liste en deux parties de facon que sommes de ces deux soient le plus proche possible
def scissionEquilibree(lst):
    '''
    lst est une liste de nombres tries dans le sens croissant
    retourne deux listes dont la concatenation contient tous les elements de lst
    et dont la somme des elements est le plus proche possible l'une de l'autre
    '''
    def scinderEquilibreIntermed(lst):
        '''
        lst est une liste de nombres tries dans le sens croissant
        retourne deux listes dont la concatenation contient tous les elements de lst
        et dont la somme des elements est le plus proche possible l'une de l'autre
        Renvoie aussi les sommes respectives des deux listes
        '''
        res1=[]
        res2=[]
        som1=[]
        som2=[]
        if lst!=[]:
            (res1,som1,res2,som2)=scinderEquilibreIntermed(lst[1:])
            if som1<som2:
                res1+=[lst[0]]
                som1+=lst[0]
            else:
                res2+=[lst[0]]
                som2+=lst[0]
        return(res1,som1,res2,som2)
    (res1,som1,res2,som2)=scinderEquilibreIntermed(lst)
    return (res1,res2)

# 5.2.5. doubler (recursif) modifiant la liste
def doublerI(lst):
    def doublerIndicesInfN(lst,n):
        if n>=0:
            doublerIndicesInfN(lst,n-1)
            lst[n]*=2
    doublerIndicesInfN(lst,len(lst)-1)
    
# 6: recursion generalisee
# 6.1. si la liste est symmetrique
def estSym(lst):
    if lst==[]:
        return True
    else:
        return lst[0]==lst[-1] and estSym(lst[1:,-1])

# 6.2. dichotomie pour sin (recursif)
import math
def dicho(bmin,bmax,epsilon):
    if bmax-bmin<=epsilon: #arret
        return (bmax-bmin)/2
    else:
        milieu=(bmax-bmin)/2
        if math.sin(milieu)>0:
            return dicho(milieu,bmax,epsilon)
        else:
            return dicho(bmin,milieu,epsilon)

# 6.3. dichotomie pour une fonction
def dichotomieF(f,bmin,bmax,epsilon):
    if bmax-bmin<=epsilon:
        return (bmax+bmin)/2
    else:
        milieu=(bmax-bmin)/2
        if f(milieu)*f(bmin)>0:
            return dichotomieF(f,milieu,bmax,epsilon)
        else:
            return dichotomieF(f,bmin,milieu,epsilon)

def sq2(x):
    return x*x-2

print(dichotomieF(sq2,1,2,0.0001))

# 7: diviser pour regner
# 7.1: evaluation d'une expression completement parenthesee
def evalExpr(ex):
    if type(ex)==int or type(ex)==float:
        return ex
    e1,op,e2=ex
    if op=='+':
        return evalExpr(e1)+evalExpr(e2)
    elif op=='*':
        return evalExpr(e1)*evalExpr(e2)
    elif op=='-':
        return evalExpr(e1)-evalExpr(e2)
    elif op=='//':
        return evalExpr(e1)//evalExpr(e2)
    
    print(evalExpr((2,'+',(5,'*',8))))


       


             

