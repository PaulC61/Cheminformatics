# question 1
# a number is considered a perfect number when 
# the sum of it's divisors returns said number

def justifieParfait(number):
    summ = 0
    i = number
    while i > 1:
        if number%i ==0:
            summ += number//i
        i -= 1
    return summ == number

# set of functions they wanted us to use

#1.1 estdivisibleby
# n/p??

def isDivisibleBy(n,p):
    return n%p == 0

# 1.2 listeDiviseursStrict
# given a number, return it's strict diviseurs

def listeDiviseursStrict(n):
    divLst = []
    for i in range(1, n):
        if isDivisibleBy(n,i) == True:
            divLst += [i]
    return divLst

def sommeLstLoop(lst):
    somme = 0
    for i in range(len(lst)):
        somme += lst[i]
    return somme

def estParfaitJust(n):
    theList = listeDiviseursStrict(n)
    somme = sommeLstLoop(theList)
    return (somme == n, theList)

def sommeVersChaine(lst):
    chainChar = ""
    for i in range(len(lst)):
        if i != len(lst) -1:
            chainChar += str(lst[i]) + " + "
        else:
            chainChar += str(lst[i])
    return chainChar

def justifieParfait(n):
    check = estParfaitJust(n)
    if check[0] == True:
        return str(n) + " is a perfect number as the sum of its divisors are equal to itself:\n" + sommeVersChaine(check[1]) + " = " + str(sommeLstLoop(check[1]))
    else:
        return str(n) + " is not a perfect number as the sum of its divisors are not equal to itself:\n" + sommeVersChaine(check[1]) + " = " + str(sommeLstLoop(check[1]))


# 2. Recursivity
# 2.1

def indices(char, charLst, indexLst = [], count = 0):
    if charLst == []:
        return indexLst
    elif char == charLst[0]:
        return indices(char, charLst[1:], indexLst + [count], count+1)
    else:
        return indices(char, charLst[1:], indexLst, count+1)

def maximum(lst):
    if len(lst) == 1:
        return lst[0]
    elif lst[0] > lst[1]:
        return maximum([lst[0]] + lst[2:])
    else:
        return maximum(lst[1:])
        
def somme(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return somme([lst[0] + lst[1]] + lst[2:])

def somme_prefixe(origLst, newLst = []):
    if origLst == []:
        return newLst
    elif newLst == []:
        return somme_prefixe(origLst[1:], newLst + [origLst[0]])
    else:
        return somme_prefixe(origLst[1:], newLst + [newLst[-1] + origLst[0]])

print(somme_prefixe([1,2,3,4,5,6]))