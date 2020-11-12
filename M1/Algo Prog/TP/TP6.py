#%%
from os import curdir
import random
import math
import os

def geometricSequence(base, ratio, index, i=1):
    if i == index:
        return base
    else:
        base = base*ratio
        return geometricSequence(base, ratio, index, i + 1)

def geometricSequenceCorrection(n, u0, q):
    return u0 if n<=0 else q*geometricSequenceCorrection(n-1, u0, q)

def oneOverNSquare(N, theSum = 0, i = 1):
    if i == N:
        return theSum
    else:
        theSum += 1/(i**2)
        return oneOverNSquare(N, theSum, i+1)

def oneOverNSquareCorr(n):
    if n==1:
        return 1
    else:
        return 1./(n*n) + oneOverNSquareCorr(n-1)



# def randomNumberlst(n, valmax, iterator = 0, theLst = []):
#     if iterator == n:
#         return theLst
#     else:
#         theLst += [random.randint(0,valmax)]
#         return randomNumberlst(n, valmax, iterator + 1, theLst)

def randomNumberlst(n, valmax, theLst = []):
    if n == 0:
        return theLst
    else:
        return randomNumberlst(n-1, valmax, theLst + [random.randint(0,valmax)])



lstyBoi = [9, 5, 3, 17, 6, 8]

def invertFunction(lst, invertLst = []):
    if lst == []:
        return invertLst
    else :
        invertLst += [lst[-1]]
        del lst[-1]
        return invertFunction(lst, invertLst)

# def pathFunction(targetValue, lst, iterator = 0, newLst = []):
#     if targetValue in newLst:
#         return newLst
#     else:
#         if iterator == len(lst)-1:
#             newLst = []
#             return newLst
#         else:
#             return pathFunction(targetValue, lst, iterator + 1, newLst + [lst[iterator]])


def pathFunction(targetValue, lst, newLst = []):
    if lst == [] and targetValue not in newLst:
        return lst
    elif targetValue in newLst:
        return newLst
    else:
        return pathFunction(targetValue, lst[1:], newLst + [lst[0]])

def chemo(lst, xx, acc):
    if lst == []:
        return []
    if lst[0] == xx:
        return acc + [xx]
    else:
        return chemo(lst[1:], xx, acc+[lst[0]])


def deleteSpacesAndApost(string):
    if string == '':
        return ''
    elif string[0] == ' ' or string[0] == ',':
        return deleteSpacesAndApost(string[1:])
    else:
        return string[0] + deleteSpacesAndApost(string[1:])

# needs to include sentences, so delete spaces

def isPalindrome(strng): 
    workingStrng = deleteSpacesAndApost(strng)
    print(workingStrng)
    if workingStrng == '':
        return True
    elif workingStrng[0] != workingStrng[-1]:
        return False
    else:
        return isPalindrome(workingStrng[1:-1])

def dichotomieCarre(bmin, bmax, epsilon): 
    if bmax-bmin <= epsilon:
        return (bmax+bmin)/2
    else:
        midPoint = (bmax+bmin)/2
        if midPoint*midPoint-2 > 0:
            return dichotomieCarre(midPoint, bmax, epsilon)
        else:
            return dichotomieCarre(bmin, midPoint, epsilon)
    
def dichotomieFunc(f, bmin, bmax, epsilon):
    if bmax-bmin <= epsilon:
        return (bmax+bmin)/2
    else:
        midPoint = (bmax+bmin)/2
        if f(midPoint)*f(bmin) > 0:
            return dichotomieFunc(f, midPoint, bmax, epsilon)
        else:
            return dichotomieFunc(f, bmin, midPoint, epsilon)

def getSin(x):
    return math.sin(x)

def sq2(x):
    return x*x-2

def listedir():
    if os.path.isfile(os.path.curdir) == True:
        return os.path.abspath
    else:
        return os.walk(True,os.path.abspath)
    



# print(geometricSequence(4, 2, 4))
# print(oneOverNSquare(998))
# print(randomNumberlst(5, 67))
# print(pathFunction(2, lstyBoi))
# print(deleteSpacesAndApost('Do you like green eggs and ham? Yes sir, I do'))
# print(invertFunction(lstyBoi))
print(isPalindrome('engage le jeu que je le gagne'))
print(dichotomieFunc(sq2,1, 2, 0.00001))
print(dichotomieFunc(getSin, 1.7, 4, 0.0000001))
# print(isADirectory('\Documents'))
# print(os.getcwd())
# os.chdir('/Users/Paul/Documents')

# os.removedirs('OS-Demo-PathDir/Sub-Dir-1')
print(os.path.isdir(os.path.curdir))
print(listedir())

# print(os.listdir())
# %%
