import random

def numbers(cartas):
    card_list = []
    for i in range(1,(cartas)+1):
        card_list.append(i)
        card_list.append(i)
    random.shuffle(card_list)
    return card_list

def board(card_list):
    board = []
    k = 0
    for i in range(0,2):
        row = []
        for j in range(0,int(len(card_list)/2)):
            row.append(card_list[k])
            k += 1
        board.append(row)   
    return board

def board_censor(board):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    print("   |",end="")
    for j in range(len(board[0])):
        print('',abc[j],"|",end="")
    print()
    print()
    abc_num = 0
    for i in range(len(board)):
        print(abc[abc_num]," |",end="")
        for j in range(len(board[i])):
            print('',board[i][j],"|",end="")
        abc_num += 1
        print()
    return board

def board2(board):
    board2 = []
    for i in range(len(board)):
        row2 = []
        for j in range(len(board[i])):
            row2.append('?')
        board2.append(row2)
    return board2

def coord(a,b, board2, board):
    board2[a][b] = board[a][b]
    board_censor(board2)
    return board[a][b]

def clean(a1,b1,a2,b2):
    board2[a1][b1]="?"
    board2[a2][b2]="?"

def print_board(board): 
    for i in board:
        for j in i:
            print(j," ",end="")
        print()
    return board

def change_player(player):
    if player==1:
        player=2
    else:
        player=1
    return player

def valid(a,b,board):
    if a<0 or a>len(board) or b<0 or b>len(board[0]) or board[a][b] != '?':
        print("Not valid")
        return False
    
    return True

def count(board):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
           if board[i][j] == '?':
              counter += 1
    return counter

cartas = int(input('numero de cartas: '))
card_list = numbers(cartas)
board = board(card_list)
board2 = board2(board)
print(board2)
print('board')
print_board(board)
print('censored board')
board_censor(board2)



#----------------------------------------------------------
p1_points = 0
p2_points = 0
player=1


while count(board2) > 0:
    print("Now it's playing Player",player)
    move1_p1_a = int(input(': '))
    move1_p1_b = int(input(': '))
    while valid(move1_p1_a,move1_p1_b,board2) == False:
            move1_p1_a = int(input(': '))
            move1_p1_b = int(input(': '))
    
    p1_card1 = coord(move1_p1_a,move1_p1_b, board2, board)
    
    move2_p1_a = int(input(': '))
    move2_p1_b = int(input(': '))
    while valid(move2_p1_a,move2_p1_b,board2) == False:
            move2_p1_a = int(input(': '))
            move2_p1_b = int(input(': '))
    
    p1_card2 =coord(move2_p1_a,move2_p1_b, board2, board)
    
    if p1_card1 == p1_card2:
        print("It's a match, keep playing!")
        if player==1:
            p1_points += 1
        else:
            p2_points += 1
    else:
        print("Wrong")
        clean(move1_p1_a,move1_p1_b,move2_p1_a,move2_p1_b)
        board_censor(board2)
        player = change_player(player)
if p1_points > p2_points:
    print("The winner is Player 1 with", p1_points, "pairs")
elif p1_points < p2_points:
    print("The winner is Player 2 with", p2_points, "pairs")
else:
    print("It´s a tie")