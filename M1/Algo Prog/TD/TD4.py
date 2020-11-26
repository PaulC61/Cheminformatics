#td4
#1.1
'''
c=(0,255,255)
def intensite(c):
	intens=(c[0]+c[1]+c[2])/3
	return float(intens)
print(intensite(c))

#1.2
def sommbre(c):
	b=(c[0]//2,c[1]//2,c[2]//2)
	return b
print(sommvre(c))
'''

#2.1
'''
lst=[1,2,3]
for e in lst:
	print(2*e)

for i in range(len(lst)):
	print(lst[i]*2)

#2.2
for i in range(len(lst)):
	lst[i]*=2
print(lst)
'''

#2.3
'''
lst=[1,2,3]

def doubler(lst):
	l=[]
	
	for i in range(len(lst)):
		l=l+[lst[i]*2]
	return l 
print(doubler(lst))

#2.4
lst=["1","2","3"]
def strToIntLst(lst):
	l=[]
	for i in range(len(lst)):
		l=l+[int(lst[i])]
	return l
print(strToIntLst(lst))
'''	
#3.1
'''
lst=[1,2,0,8,9]
def contientUn3(lst):
	i=0
	while i<len(lst) and lst[i]!=3:
			i+=1
	return i!=len(lst)

print(contientUn3(lst))
'''


#3.2
lst=[1,2,0,8,9]
def comptepairs(lst):
	l=[]
	for i in range(len(lst)):
		if lst[i] % 2 == 0:
			l=[lst[i]]+l
		return l
print(comptepairs(lst))

