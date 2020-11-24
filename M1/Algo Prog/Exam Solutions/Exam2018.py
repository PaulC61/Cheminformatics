# Question 1: The White Scarf
# for each exercise write two functions that
# i) duplicates the inputs to accomplish the task
# ii) uses a loop to add the characters sequentially

# write a function "stars" that when inputting an int "lngth" produces a chaine of length lngth of "*"
# i)
def starsDup(lngth):
    return "*"*lngth

# ii)
def starsLoop(lngth):
    starStrng = ""
    for i in range (lngth):
        starStrng += "*"
    return starStrng

print(starsDup(5))
print(starsLoop(5))