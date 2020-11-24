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

print(starsBandWhiteDup(10, 3, 2))
print(starsBandWhiteLoop(10, 3, 2))