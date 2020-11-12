import random
def a_the_string(i):
	Astring = i*"A"
	return Astring

def aSpace_the_string(intSpace, intA):
	spaceString = intSpace*" "
	Astring = intA*"A"
	
	entireString = spaceString + Astring
	return entireString

def stringRandom(intSpace, intString):
	spaceString = intSpace*" "
	theString = ""
	for i in range(intString):
		randomInt = random.randint(0,100)
		if randomInt<20:
			theString = theString + "*"
		else:
			theString = theString + "O"
	entireString = spaceString + theString
	print(entireString)
	return None

def column(n):
	for i in range(10):
		print(a_the_string(n))
	
	return None
	
def diagonel_1(n):
	for i in range(1, n+1):
		Astring = i*"A"
		print(Astring)
		
	return None
		
def diagonel_2(n):
	stringSpace = n-1
	stringA = 1
	for i in range(n):
		
		print(aSpace_the_string(stringSpace, stringA))
		stringSpace = stringSpace - 1
		stringA = stringA + 1
		
	return None
		
def sapin(n):
	leftSpaces=n-1
	leftA = 1
	for i in range(n):
		leftSideOfTree = aSpace_the_string(leftSpaces, leftA)
		rightSideOfTree = a_the_string(i)
		print(leftSideOfTree + rightSideOfTree)
		leftSpaces = leftSpaces - 1
		leftA = leftA + 1
	
	print(aSpace_the_string(n-1, 3))
	return None

def sapin2(n):
	for i in range(n):
		print((n-i)*" " + (2*i+1)*"A")
	print(aSpace_the_string(n-1, 3))
	return None

def XmasSapin(n):
	for i in range(n):
		stringRandom(n-i, 2*i+1)
	print(stringRandom(n-1, 3))
	return None

column(5)
diagonel_1(10)
diagonel_2(10)
sapin(20)
sapin2(20)
stringRandom(5, 20)
XmasSapin(30)
