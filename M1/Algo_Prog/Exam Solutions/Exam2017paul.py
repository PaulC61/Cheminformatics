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

print(search_quantity("cookie", smolList))

