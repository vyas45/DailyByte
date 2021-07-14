'''
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
'''

def isCapital(str):
    if (len(str) == 0):
        return True
    
    count = 0

    for item in str:
        if item.isupper():
            count += 1

    # If all are upper or none upper
    if (count == len(str) or count == 0 or (count == 1 and str[0].isupper())):
        return True
    else:
        return False


print(isCapital("USA"))
print(isCapital("Calvin"))
print(isCapital("compUter"))
print(isCapital("coding"))
