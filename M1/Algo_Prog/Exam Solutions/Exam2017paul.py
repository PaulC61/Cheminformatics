# okay 

# ingredient
# define a type: ingredient = (name, amount, cool) 
# constructor function create_ingredient

ingredient = "milk"
quant = 10
cool = True

smolList = [("apple",10,True),("cookie",18,False),("milk",3, True)]

def create_ingredient(ingredFunc, quantFunc, coolFunc):
    return ingredFunc, quantFunc, coolFunc

def is_in(ingName, ingLst):
    print(ingLst)
    if ingLst == []:
        return False
    elif ingLst[0][0] != ingName:
        return is_in(ingName, ingLst[1:])
    else:
        return True

print(is_in("milk", smolList))