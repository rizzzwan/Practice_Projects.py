def sum(a,b,c):
    return a + b +c

def printnoard(xState,yState):
    zero = 'X' if xState[0] else ('O' if yState[0] else 0)
    one = 'X' if xState[1] else ('O' if yState[1] else 1) 
    two = 'X' if xState[2] else ('O' if yState[2] else 2) 
    three = 'X' if xState[3] else ('O' if yState[3] else 3) 
    four = 'X' if xState[4] else ('O' if yState[4] else 4) 
    five = 'X' if xState[5] else ('O' if yState[5] else 5) 
    six = 'X' if xState[6] else ('O' if yState[6] else 6) 
    seven = 'X' if xState[7] else ('O' if yState[7] else 7) 
    eight = 'X' if xState[8] else ('O' if yState[8] else 8) 
    print (f" {zero} | {one} | {two} |")
    print ("-------------")
    print (f" {three} | {four} | {five} |")
    print ("-------------")
    print (f" {six} | {seven} | {eight} |")
    
def checkWin(xState,yState):
    Win = [ [0,1,2],[0,3,6],[0,4,8],[2,4,6],[3,4,5],[6,7,8],[1,4,7],[2,5,8]]
    for win in Win :
        if (sum (xState[win[0]],xState[win[1]],xState[win[2]]) ==3):
                print ("\033[92mCONGRATS\033[0m",p1name,"\033[92mYOU WON THE MATCH!!!!\033[0m")
                return 1
        for win in Win :
            if (sum (yState[win[0]],yState[win[1]],yState[win[2]]) ==3):
                print ("\033[92mCONGRATS\033[0m",p2name,"\033[92mYOU WON THE MATCH!!!!\033[0m")
                return 0
    return -1
def checkTie(xState,yState):
    if all(xState[i] ==1 or yState[i] ==1 for i in range (9)):
        return True
    return False

xState = [0,0,0,0,0,0,0,0,0]
yState = [0,0,0,0,0,0,0,0,0]
turn = 1
print ("    \033[1m    Tic Tac Toe game\033[0m")
p1name = input ("Enter 1st Player's NAME: ")
p2name = input ("Enter 2nd Player's NAME: ")

print ("[X] is ",p1name, "and [O] is ",p2name,)
while True:
    printnoard (xState,yState)
    if turn == 1:
        print (p1name,"'s Turn")
        value = int(input("Please Enter a value: "))
        xState [value] = 1
    else:
        print (p2name,"'s Turn")
        value = int(input("Please Enter a value: "))
        yState [value] = 1

    cwin = checkWin(xState,yState)
    if cwin != -1:
        print ("MATCH OVER")
        break
    
    if checkTie(xState,yState):
        print ("\033[91mIts a TIE\033[0m")
    turn = 1 - turn


