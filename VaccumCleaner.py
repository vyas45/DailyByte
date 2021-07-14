'''
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
'''

'''
To find if we will indeed return home, 
we need to keep a track of L-R and U-D compliments
As long as the compliments match we will be home
LRRRUUDDLL
'''
def findHome(moves):
    if (len(moves)%2 != 0):
        return False

    x = 0
    y = 0

    for item in moves:
        if (item == 'L'):
            x += 1
        elif (item == 'R'):
            x -= 1
        elif (item == 'U'):
            y += 1
        else:
            y -= 1

    return (x==y==0)

print(findHome("LR"))
print(findHome("URURD"))
print(findHome("RUULLDRD"))
