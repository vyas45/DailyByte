'''
Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
'''

def reverseString1(str):
    print(str[::-1])

def reverseString(string):
    i = len(string)-1
    newstr = ""

    while(i>=0):
        newstr += string[i]
        i -= 1
    print("Reversed string is ", newstr)

reverseString("Cat")
reverseString("The Daily Byte")
reverseString("civic")
