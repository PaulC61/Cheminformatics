# question 1
# a number is considered a perfect number when 
# the sum of it's divisors returns said number

def justifieParfait(number):
    summ = 0
    i = number
    while i > 1:
        if number%i ==0:
            summ += number//i
        i -= 1
    return summ == number

print(justifieParfait(140))