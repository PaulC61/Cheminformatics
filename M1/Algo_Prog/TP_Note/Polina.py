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