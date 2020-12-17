# okay 

# ingredient
# define a type: ingredient = (name, amount, cool) 
# constructor function create_ingredient

ingredient = "milk"
quant = 10
unit = "L"
cool = True

smolList = [("apple",1, "kg", True),("cookie", 10, "#", False),("milk", 500, "mL", True)]

def create_ingredient(ingredFunc, quantFunc, coolFunc):
    return ingredFunc, quantFunc, coolFunc

def is_in(ingName, ingLst):
    if ingLst == []:
        return False
    elif ingLst[0][0] != ingName:
        return is_in(ingName, ingLst[1:])
    else:
        return True

def total_weight(ingLst):
    weight = 0
    volume = 0
    quant = 0
    for i in range(len(ingLst)):
        if ingLst[i][2] == "kg":
            weight += ingLst[i][1]
        elif ingLst[i][2] == "mL":
            volume +=ingLst[i][1]
        else:
            quant += ingLst[i][1]

    return "Shop has weighted goods of " + str(weight) + "kg, items with " + str(volume) + " volume (mL) and " + str(quant) + " small items." 

def total_weight_simple(ingLst):
    quant = 0
    for i in range(len(ingLst)):
        quant += ingLst[i][1]
    return quant

def needs_fridge(ingLst, fridgeLst = []):
    if ingLst == []:
        return fridgeLst
    elif ingLst[0][3] == True:
        return needs_fridge(ingLst[1:], fridgeLst + [ingLst[0]])
    else:
        return needs_fridge(ingLst[1:], fridgeLst)


def search_quantity(name, ingLst):
    quant = 0
    for i in range(len(ingLst)):
        if ingLst[i][0] == name:
            quant += ingLst[i][1]
    return quant

def index(name, ingrLst):
    for i in range(len(ingrLst)):
        if ingrLst[i][0] == name:
            return i

def groceries(recipe, cupboard):
    groceryLst = []
    for i in range(len(recipe)):
        if search_quantity(recipe[i][0], cupboard) == 0:
            groceryLst += [recipe[i]]
        elif search_quantity(recipe[i][0], cupboard) < recipe[i][1]:
            groceryLst += [(recipe[i][0], recipe[i][1] - cupboard[index(recipe[i][0], cupboard)][1])]
    return groceryLst

# combine function
# given two lists of ingredients
# returns a list containing the ingredients needed for both recipes
# !! without redundancy
# we could define one list as the cupboard and one as the recipe, using the previous function

def combine(recipe1, recipe2):
    groceryLst = recipe1
    for i in range(len(recipe2)):
        if search_quantity(recipe2[i][0], groceryLst) == 0:
            groceryLst += [recipe2[i]]
        elif search_quantity(recipe2[i][0], groceryLst) != recipe2[i][1]:
            groceryLst = groceryLst[0:index(recipe2[i][0], groceryLst)] + [(recipe2[i][0], recipe2[i][1] + recipe1[index(recipe2[i][0], recipe1)][1])] + groceryLst[index(recipe2[i][0], groceryLst)+1:]
    
    return groceryLst

print(combine([('bread', 3),('brie',1),('butter',3)], [('bread', 2),('pears',10),('gnocchi',50),('butter',1),('brie',4)]))

