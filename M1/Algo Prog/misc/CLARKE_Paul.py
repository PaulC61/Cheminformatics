
wordPal = "kayak"

wordNotPal = "sorry you had to watch that"

# must use while loop
def palindromeWhile(string):
    isPalindrome = True
    i = len(string) - 1
    j = 0
    while j < len(string):
        if string[i] != string[j]:
            isPalindrome = False
            return isPalindrome
        else:  
            i -= 1
            j += 1
    return isPalindrome
# must be recursive
def palindromeRec(strng, i = 1, j = 0, isPalindrome = True):
    if strng[len(strng)-i] != strng[j]:
         isPalindrome = False
         return isPalindrome
    else:
        if j == len(strng)-1:
            isPalindrome = True
            return isPalindrome
        else:
            return palindromeRec(strng, i + 1, j + 1)

def palindromeRecSimple(strng):
    if len(strng)<2: 
        return True 
    else:
        strng[0] == strng[-1] and palindromeRecSimple(strng[1:-1]) 

print(palindromeRec(wordPal))