### Examen 2018-2019
 ## Contrôle écrit (seulement)

# Question 1: The White Scarf
# for each exercise write two functions that
# i) duplicates the inputs to accomplish the task
# ii) uses a loop to add the characters sequentially

# 1.1 write a function "stars" that when inputting an int "lngth" produces a chaine of length lngth of "*"
# i)
def starsDup(lngth):
    return "*"*lngth

# ii)
def starsLoop(lngth):
    starStrng = ""
    for i in range (lngth):
        starStrng += "*"
    return starStrng

# 1.2 write a function "starsBandWhite" 
# inputs "lngth", "pos", "bandWdth"
# return
#   chain of characters of length "lngth"
#   where characters are "*" except for a
#   bandwidth "bandWdth" at starting positon "pos"
# i)
def starsBandWhiteDup(lngth, pos, bandWdth):
    return "*"*pos + " "*bandWdth + "*"*(lngth-pos-bandWdth)

#ii)
def starsBandWhiteLoop(lngth, pos, bandWdth):
    starStrng = ""
    for i in range (lngth):
        if i >= pos and i < pos+bandWdth:
            starStrng += " " 
        else:
            starStrng += "*"
    return starStrng

# 1.3 write a function "whiteScarfPoster"
# inputs: "lngth", "bndWidth"
# return
#   None
#   but prints in the terminal
#   lngth-bandWidth+1 rows
#   of strings length = lngth
#   where the resulting rectangle of stars has a white band
#   going from the top left corner to the bottom right 
#   need to use the function: starsBandWhite

def whiteScarfPoster(lngth, bandWidth):
    for i in range (lngth-bandWidth+1):
        print(starsBandWhiteDup(lngth, i,bandWidth))
    return None

# 2.1 sumList function
# input: list of numbers
# output: one integer --> sum of elements in list
def sumList(lst):
    if lst == []:
        return 0
    else:
        storeInt = 0
        for i in range(len(lst)):
            storeInt += lst[i]
        return storeInt

#2.2 normalise
# input: lst
# output: None
# aim is to directly modify the list to be normalised (divided by the sum of the list)

def normalise(lst):
    normBase = sumList(lst)
    for i in range(len(lst)):
        lst[i] = lst[i]/normBase
    return None

# 2.3 creeNorm
# Same as befor but we're returning a brand new normalised list
# Where the inputted list is unchanged

def createNorm(lst):
    normBase = sumList(lst)
    normLst = []
    for i in range(len(lst)):
        normLst += [lst[i]/normBase]
    return normLst

# 2.4 cumul (same as sumPrevious as seen in 2020, Q 2.4)
# except making this recursive is not required
# specifically states we need to create a new list
# two versions done: Loop and Recursive

def cumulLoop(lst):
    newLst = []
    if lst ==[]:
        return newLst
    elif len(lst) ==1:
        newLst += lst
    else:
        newLst += [lst[0]]
        for i in range(1, len(lst)):
            newLst += [lst[i] + newLst[i-1]]
    return newLst

def cumulRecurs(lst, newLst = []):
    if lst == []:
        return newLst
    elif newLst == []:
        return cumulRecurs(lst[1:], newLst + [lst[0]])
    else:
        return cumulRecurs(lst[1:], newLst + [newLst[-1] + lst[0]])

# Question 3
# 3.1 
# inserer
# input: lst, num, ind
# return: new lst with num inserted at index ind

def insert(lst, num, ind):
    if ind > len(lst):
        lst += [num]
    else:  
        return lst[:ind] + [num] + lst[ind:]
        
# 3.2
# indiceIns
# input lst and number n
# return an index of the list where:
# if the list is empty return 0
# ifnot return the index of the first element >= n
# if n is greater than all the elements in the list; return the length of the list

def indiceIns(lst, n):
    if lst == []:
        return 0
    else:
        for i in range(len(lst)):
            if lst[i] >= n:
                return i
        return len(lst)

# 3.3 triInsertion
# order a list in the ascending direction
# in 2018 they got them to build useful functions above that help

def orderLst(lst, newLst = []):
    if lst == []:
        return newLst
    elif newLst == []:
        return orderLst(lst[1:], newLst + [lst[0]])
    else:
        return orderLst(lst[1:], insert(newLst, lst[0], indiceIns(newLst, lst[0])))
  

# Question 4
# 4.1
# sumDiv23 
# input: integer n 
# return: sum of every smaller number of n divisble by2/3 
def sumDiv23(n, somme = 0):
    if n == 0:
        return somme
    elif n % 2 == 0 or n % 3 == 0:
        return sumDiv23(n-1, somme + n)
    else:
        return sumDiv23(n-1, somme)


# 4.2 
# recursive version of sumList in Q 2.1
# want to try not have a counter or keeper
# store sum in lst itself

def sumListRecurs(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        lst[1] = lst[0] + lst[1]
        return sumListRecurs(lst[1:])

# 4.3
# minimum
# input non-empty list
# return smallest element of the list

def minimum(lst):
    if len(lst) == 1:
        return lst[0]
    elif lst[0] < lst[1]:
        return minimum(lst[2:]+[lst[0]])
    else:
        return minimum(lst[2:]+[lst[1]])

# Question 5
# 5.1 
# How many comparisons?
# it makes n comparisons 0 --> n-1

# 5.2
# How is the complexity of this algorithm?
# Defn: complexity of an algorithm is a measure of time and/or space 
# required by an algorithm for an input of a given size (n)

# complexity in terms of time: large as it looks at each
# element one-by-one (main complexity based on time)
# complexity in terms of space: in-place: only requires a constant amount
# of additional memory space

# 5.3 
# How many comparisons does the function make?
# n again; I don't see where there's more comparisons but I guess there shooul be more
# I would have thought n + how many times it takes to swap with makes

# 5.4 
# time complexity is the same or larger as we have to first compare each element as before
# and then again for each swap, also each element is checked twice individually

# Question 6
# decomposer
# input a the list given and a money amount
# return a list of the smallest possible size that gives
# the money amount with the elements from the given list

demOptions = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def decompose(demOptions, datMoney, moneyList = []):
    limitDatMoney = round(datMoney, 2)
    if limitDatMoney == 0:
        return moneyList
    elif demOptions[0] > limitDatMoney:
        return decompose(demOptions[1:], limitDatMoney, moneyList)
    else:
        return decompose(demOptions, limitDatMoney - demOptions[0], moneyList + [demOptions[0]])
  
print(decompose(demOptions, 472.32))