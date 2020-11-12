
#%%
import math

def doubler(lst):
    if lst==[]:
        return []
    else:
        return [lst[0]*2] + doubler(lst[1:])

def supprime (asup, lst):
    if lst == []:
        return []
    # else
    elif lst[0] == asup:
        return supprime(asup, lst[1:])
    
    else:
        return [lst[0]] + supprime(asup, lst[1:])

def insereDansTrie(lst, a_inserer):
    if lst == []:
        return [a_inserer]
    elif a_inserer < lst[0]:
        return [a_inserer] + lst
    else:
        print(lst[0], ' ', lst[1:])
        return [lst[0]] + insereDansTrie(lst[1:], a_inserer)



# recursive with decreasing list
# Divides ordered list in two where they add up to each other as best they can
# I think I just need to order a list, and go every two places


def scissionEquilibrium(lstToSplit, lst1=[], lst2 = []):
    lstToSplit.sort()
    print("Sorted List:", lstToSplit)
    if lstToSplit == []:
        return lst1, lst2
    elif len(lstToSplit) == 1:
        return lst1 + [lstToSplit[-1]], lst2
    elif len(lstToSplit) == 2:
        return lst1 + [lstToSplit[-1]], lst2 + [lstToSplit[-2]]
    else:
        return scissionEquilibrium(lstToSplit[:-2], lst1 + [lstToSplit[-1]], lst2 + [lstToSplit[-2]])

print(scissionEquilibrium([13, 14, 5, 8, 8, 9, 6, 21, 24, 27, 31, 41]))

# recursion generalised
def isSymmetric(lst):
    if lst==[]:
        return True
    else:
        # making a larger boolean that reaches into the rest of the list
        return lst[0] == lst[-1] and isSymmetric(lst[1:-1])
        
def isSymmetricCorrction(lst):
    if len(lst) < 2:
        return True
    elif lst[0] != lst[-1]:
        return False
    else:
        return isSymmetricCorrction(lst[1:-1])

# this is the same question but for sin(x) = 0
# essentially the question asks to find the zeros as before

def dichotomieSin(bmin, bmax, epsilon):
    if bmax-bmin <= epsilon:
        return (bmax + bmin)/2
    else:
        midPoint = (bmax + bmin)/2
        if math.sin(midPoint)>0:
            return dichotomieSin(midPoint, bmax, epsilon)
        else:
            return dichotomieSin(bmin, midPoint, epsilon)

def dichotomieAnyFunction(f, bmin, bmax, epsilon):
    if bmax - bmin <= epsilon:
        return (bmax + bmin)/2
    else:
        midPoint = (bmax + bmin)/2
        if f(midPoint)*f(bmin)>0: # if (f(midpoint) > 0 and f(bmin) > 0) or (f(midpoint) < 0 and f(bmin) <0 )
            # for 0 values along the positive x-axis
            return dichotomieAnyFunction(f, midPoint, bmax, epsilon)
        else:
            # for 0 values along the negative x-axis
            return dichotomieAnyFunction(f, bmin, midPoint, epsilon)

def sq2(x):
    return x*x-2



print(isSymmetric([1,2]))
print(dichotomieSin(1.7, 4, 0.0000001))
print(dichotomieAnyFunction(sq2, 1, 2, 0.00001))

# %%
