### Examen 2016-2017
 ## Contrôle écrit (seulement)
  
  # Important to know: this had to be solved using OCALM language, not Python
  # But, what's the difference? I did it using Python
  # But not all the exercices (without ex 1 and ex 4, cause it was useless)


  # 1. Déclarations élémentaires
    # 1.2. Corriger l'écriture des fonctions
def fct1(a,m1,m2):
    return m1<=a<=m2

def fct2(a,m1,m2):
    return not(m1<=a<=m2)

def fct3(a,b):
    return a>5 or b<3
     
  # 2. Fonctions
def fabs(x):
    return abs(x) # or return x if x>=0 else -x

def test_droite(a,b,c):
    return a!=0 and b!=0

import math
def distancepl(a,b,c,xp,yp):
    d=fabs(a*xp+b*yp+c)/math.sqrt(a**2+b**2)
    return d

def intersect(a,b,c,xp,yp,radius):
    if test_droite(a,b,c):
        d=distancepl(a,b,c,xp,yp)
        return d<=radius
    else:
        return None

  # 3. Enregistrements
def aire_rect(la,lo):
      return la*lo

def aire_cer(r):
    return math.pi*r**2

def test_espace(l,nt,r):
    return l>=(nt*r+2*(nt-1)+4)

def volume_plaque(la,lo,tla,tlo,r,ep):
    if test_espace(la,tla,r) and test_espace(lo,tlo,r):
        return (la*lo-(math.pi*r**2*tla*tlo))*ep
    else:
        return None
#here units of volume are mm^3, cause it was given in mm in the beginning

def prix_matiere(volume,densite,prix):
    return (volume*10**-6*densite)/1000*prix
# so here we just want to use the same units everywhere