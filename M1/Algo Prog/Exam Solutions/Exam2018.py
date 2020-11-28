
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


lst = [4,2,5,6,3,8,1]

print(insert(lst, 18, 0))