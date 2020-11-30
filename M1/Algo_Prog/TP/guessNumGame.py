import random
def mystNumGame():
	user_input = ""
	mystInt = random.randint(0,99)
	print(mystInt)
	while user_input != str(mystInt):
		user_input = input("Yo guess a number between 0 and 99 \n")
	print("Ah class, good man/woman/whatever \n")
	user_input2 = input("Do you want to play again? \n")
	if user_input2 == "Yes" or user_input2 == "yes":
		mystNumGame()
	else:
		print("fine have it your way then")
	
	return None
	
mystNumGame()
