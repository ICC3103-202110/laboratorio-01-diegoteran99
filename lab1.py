import random

def numbers(cards):
    card_list = []
    for i in range(1,(cards)+1):
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
    abc = "abcdefghijklmnopqrstuvwxyz"
    print("   |",end="")
    for j in range(len(board[0])):
        print('',abc[j],"|",end="")
    print()
    abc_num = 0
    for i in range(len(board)):
        print(abc[abc_num]," |",end="")
        for j in range(len(board[i])):
            print('',board[i][j],"|",end="")
        abc_num += 1
        print()
    return board

def covered_board(board):
    covered_board = []
    for i in range(len(board)):
        row2 = []
        for j in range(len(board[i])):
            row2.append("▓")
        covered_board.append(row2)
    return covered_board

def coord(a,b, covered_board, board):
    covered_board[a][b] = board[a][b]
    board_censor(covered_board)
    return board[a][b]

def clean(a1,b1,a2,b2):
    covered_board[a1][b1]="▓"
    covered_board[a2][b2]="▓"

def erase_cards(a1,b1,a2,b2):
    covered_board[a1][b1]=" "
    covered_board[a2][b2]=" "

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
    if a<0 or a>len(board) or b<0 or b>len(board[0]) or board[a][b] != "▓" or board[a][b] == " ":
        print("Not valid")
        return False
    return True

def count(board):
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
           if board[i][j] == "▓":
              counter += 1
    return counter

cards = int(input("Select the number of cards: "))
card_list = numbers(cards)
board = board(card_list)
covered_board = covered_board(board)
print(covered_board)
print("board")
print_board(board)
print("censored board")
board_censor(covered_board)

#-------------------------------------------------------------------------------
p1_points = 0
p2_points = 0
player=1

while count(covered_board) > 0:
    print("Now it's playing Player",player)
    move1_p1_a = int(input(": "))
    move1_p1_b = int(input(": "))
    while valid(move1_p1_a,move1_p1_b,covered_board) == False:
            move1_p1_a = int(input(": "))
            move1_p1_b = int(input(": "))
    
    p1_card1 = coord(move1_p1_a,move1_p1_b, covered_board, board)
    print()
    
    move2_p1_a = int(input(": "))
    move2_p1_b = int(input(": "))
    while valid(move2_p1_a,move2_p1_b,covered_board) == False:
            move2_p1_a = int(input(": "))
            move2_p1_b = int(input(": "))
    
    p1_card2 =coord(move2_p1_a,move2_p1_b, covered_board, board)
    print()
    
    if p1_card1 == p1_card2:
        print("It's correct, keep playing!")
        erase_cards(move1_p1_a,move1_p1_b,move2_p1_a,move2_p1_b)
        if player==1:
            p1_points += 1
        else:
            p2_points += 1
    else:
        print("Wrong\n")
        clean(move1_p1_a,move1_p1_b,move2_p1_a,move2_p1_b)
        board_censor(covered_board)
        player = change_player(player)

if p1_points > p2_points:
    print("The winner is Player 1 with", p1_points, "pairs")
elif p1_points < p2_points:
    print("The winner is Player 2 with", p2_points, "pairs")
else:
    print("It´s a tie")