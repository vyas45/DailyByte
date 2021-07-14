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
def findHome(str):
    moveMap = {'L':0, 'R':0, 'U':0, 'D':0}
    for item in str:
        moveMap[item] += 1

    return (moveMap['L'] == moveMap['R'] and moveMap['U'] == moveMap['D'])

print(findHome("LR"))
print(findHome("URURD"))
print(findHome("RUULLDRD"))
