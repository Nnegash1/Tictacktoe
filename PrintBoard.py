import numpy as np

#declare the board
BOARD = np.zeros((3,3))

#print the current state of the board
def printBoard():
    for i in range(len(BOARD)):
        for j in range(len(BOARD)):
            print(BOARD[i][j], "  ",  end="")
        print("\n")
    
#prompt the user for input
def prompt():
    value = input("Please insert location in index format: [1 1]")
    return value


'''
    Update board and check if the current index is aready marked 
'''
def updateBoard(value, current_player):
    index_1 = int(value[0])
    index_2 = int(value[2])
    
    while BOARD[index_1][index_2] != 0.0:
        value = prompt()
        index_1 = int(value[0])
        index_2 = int(value[2])
        
    if current_player == '1':
        BOARD[index_1][index_2] = 1
    elif current_player == '2':
        BOARD[index_1][index_2] = 2
        

#check for the winner
def check_winner(player):
    flag = True
    '''
    ROW Check:
        winning state:
        0,0->0,1->0,2
        1 0->1 1->1 2
        2 0->2 1->2 2
    Vertical Check:
        Winning state:
        0 0->1 0->2 0
        0 1->1 1->2 1
        0 2->1 2->2 2
    Diagonal Check:
        0 0->1 1->2 2
        2 2->1 1->2 0
        '''

    #check for Row winner
    if BOARD[0][0] == 1.0 and BOARD[0][1] == 1.0 and BOARD[0][2] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][0] == 2.0 and BOARD[0][1]== 2.0 and BOARD[0][2] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[1][0] == 1.0 and BOARD[1][1] == 1.0 and BOARD[1][2] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[1][0] == 2.0 and BOARD[1][1] == 2.0 and BOARD[1][2] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[2][0] == 1.0 and BOARD[2][1] == 1.0 and BOARD[2][2] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[2][0] == 2.0 and BOARD[2][1] == 2.0 and BOARD[2][2] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    #check for Vertical Check
    if BOARD[0][0] == 1.0 and BOARD[1][0] == 1.0 and BOARD[2][0] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][0] == 2.0 and BOARD[1][0] == 2.0 and BOARD[2][0] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][1] == 1.0 and BOARD[1][1] == 1.0 and BOARD[2][1] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][1] == 2.0 and BOARD[1][1] == 2.0 and BOARD[2][1] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][2] == 1.0 and BOARD[1][2] == 1.0 and BOARD[2][2] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[0][2] == 2.0 and BOARD[1][2] == 2.0 and BOARD[2][2] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag

    #Diagonal Check
    if BOARD[0][0] == 1.0 and BOARD[1][1] ==1.0 and BOARD[2][2] == 1.0:
        print("Game Over:",player, "is the winner")
        print("Diagonal Check")
        flag = False
        return flag
    if BOARD[0][0] == 2.0 and BOARD[1][1] == 2.0 and BOARD[2][2] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[2][2] == 1.0 and BOARD[1][1] == 1.0 and BOARD[2][0] == 1.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    if BOARD[2][2] == 2.0 and BOARD[1][1] == 2.0 and BOARD[2][0] == 2.0:
        print("Game Over:",player, "is the winner")
        flag = False
        return flag
    
    return flag

#max amount of moves
counter = 9
END = 9
#players declaration
player1 = 1.0
player2 = 2.0
start = input("who wants to start insert 1 or 2: ")
current_player = ""

#check who will go first
if(start == '1'):
    current_player = '1'
else:
    current_player = '2'

#loop till one player win else all the possible positions are marked 
while(counter <=END):    
    printBoard()
    value = prompt()
    updateBoard(value, current_player)
    if check_winner(current_player) == False:
        printBoard()
        break
    counter -= 1
    
    if current_player == '1':
        current_player = '2'
    else:
        current_player = '1'

if counter == 0:
    print("Draw")











