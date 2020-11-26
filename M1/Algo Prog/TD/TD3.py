#TD3
#6 les nombres premiers(du d'abord il faut >2,apres divisible par 1 et lui meme)

n=int(input("please entre the numbr:")
def estPremiers(i,n): 
	for i in range(2,n):
		if n % i == 0:
			return False
		else:
			return True
		
