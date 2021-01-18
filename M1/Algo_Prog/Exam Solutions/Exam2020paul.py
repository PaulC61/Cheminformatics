import math
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

def elucideanDistance(coord1, coord2):
    diff1 = coord1[0] - coord2[0]
    diff2 = coord1[1] - coord2[1]
    diffsq1 = diff1**2
    diffsq2 = diff2**2
    sumsq = diffsq1 + diffsq2
    return math.sqrt(sumsq)

def constructPolygon(tupleLst):
    poly = []
    for i in range(len(tupleLst)):
        if i == 0:
            poly += [(tupleLst[0],tupleLst[1])]
        elif i == len(tupleLst)-1:
            poly += [(tupleLst[i],tupleLst[0])]
        else:
            poly += [(tupleLst[i],tupleLst[i+1])]
    return poly

def perimPoly(polygon):
    perim = 0
    for i in range(len(polygon)):
        sideDist = elucideanDistance(polygon[i][0],polygon[i][1])
        perim += sideDist
    return perim

def split(k, polygon):
    beforeK = []
    afterK = []
    for i in range(len(polygon)):
        if i <= k-1:
            beforeK += [polygon[i][0]]
        else:
            afterK += [polygon[i][0]]

    return beforeK, afterK


def insertCoord(k, point, polygon):
    thesplit = split(k, polygon)
    newCoord = thesplit[0] + [point] + thesplit[1]
    return constructPolygon(newCoord)

# Question 4
# return number of elements that are less than or equal to lst[i]
def compte(i, lst):
    count = 0
    for j in range(i):
        if lst[j] <= lst[i]:
            count += 1
    return count

def ordre(lst):
    lst2 = []
    for i in range(len(lst)):
        lst2 += [compte(i, lst)]
    return lst2




def tri(lst):
    lst2 = []
    otherLst = ordre(lst)
    for i in range(len(lst)):
        if i == otherLst[i]:
            lst2 += [lst[i]]
        elif otherLst[i] - len(lst) == len(lst):
            lst2 = [lst[i]] + lst2
        elif otherLst[i] - len(lst) == 0:
            lst2 = lst2 + [lst[i]]
        else:
            lst2 = lst[0: i - otherLst[i]] + [lst[i]] + lst[i-otherLst[i]:]
    return lst2
    
def index(num, lst):
    for i in range(len(lst)):
        if lst[i] >= num:
            return i
    return 0

def insert(num, lst, index):
    if index > len(lst):
        lst += [num]
    else:
        for i in range(len(lst)):
            if i == index:
                lst = lst[0:i] + [num] + lst[i:]
    return lst




def sort(lst, newLst = []):
    if lst == []:
        return newLst
    elif newLst == []:
        return sort(lst[1:], newLst + [lst[0]])
    else:
        return sort(lst[1:], insert(lst[0], newLst, index(lst[0],newLst)))

lst = [3,9,3,4,1,8]
 
print(sort(lst))
