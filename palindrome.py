'''
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
'''

def isPalin(str):
    i = 0
    j = len(str)-1

    while (i<=j):
        while(i<j and not str[i].isalnum()):
            i += 1
        while(i<j and not str[j].isalnum()):
            j -= 1
        if(str[i].lower() != str[j].lower()):
            print(str, " is not a palindrome")
            return
        i += 1
        j -= 1

    print(str," is a plaindrome")

isPalin("level")
isPalin("algorithm")
isPalin("A man, a plan, a canal: Panama.")

