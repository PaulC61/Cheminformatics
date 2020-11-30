#TD2
#1.11
'''
nom=input("choisir un nom:")
expression="je te salue " + nom +"!"
print(expression)
'''

#1.12
'''
euro=float(input("un valeur de euro"))
dollars=1.13*euro
valeur=float(dollars)
print(valeur)
'''

#1.13
'''
dollars=float(input("un valeur de dollars"))
expression=str(dollars)
print(expression)
'''

#1.14
'''
euro=float(input("un valeur de euro"))
dollars=1.13*euro
expression=str(euro)+ " euro equivalent a " + str(dollars) + " dollars"
print(expression)
'''
#1.2
'''
rev_imp=float(input("un valeur de revenue imposable"))
rev_net_imp=0.9*rev_imp
nb_parts=float(input("un valeur de nb_parts"))
montant=rev_net_imp*0.14-1372.98*nb_parts
print(motant)
'''

#2.1
'''
for i in range(100):
	print("unistra")
#2.2
for i in range(0,501):
	print(i)
	
#2.3
for n in range(0,501):
	u=2*n+3
	print(u)

#2.4
somme=0
for i in range(50):
	somme+=i
print(somme)
'''

#2.5
'''
somme=0
for i in range(0,101,2):
	somme+=i	
print(somme)
'''
#2.6
'''
def factoriel(n):
	if n==0:
		return 1
	else:
		fac=1
		for i in range(1,n+1):
			fac*=i
		return fac
print(factoriel(1))
'''

		
