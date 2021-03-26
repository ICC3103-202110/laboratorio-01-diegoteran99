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
    for i in range(2):
        row = []
        for j in range(0,int(len(card_list)/2)):
            row.append(card_list[k])
            k += 1
        board.append(row)   
    return board

def board_censor(board):
    print("   |",end="")
    for j in range(len(board[0])):
        print('',j,"|",end="")
    print()
    print()
    for i in range(len(board)):
        print(i," |",end="")
        for j in range(len(board[i])):
            print('',board[i][j],"|",end="")
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

def coord(R,C,covered_board,board):
    covered_board[R][C] = board[R][C]
    board_censor(covered_board)
    return board[R][C]

def clean(first_R,first_C,second_R,second_C):
    covered_board[first_R][first_C]="▓"
    covered_board[second_R][second_C]="▓"

def erase_cards(first_R,first_C,second_R,second_C):
    covered_board[first_R][first_C]=" "
    covered_board[second_R][second_C]=" "
    
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

def valid(R,C,board):
    if R<0 or R>1 or C<0 or R>len(board) or C>len(board[0]) or board[R][C]!="▓":
        print("Not valid\n")
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
print()
card_list = numbers(cards)
board = board(card_list)
covered_board = covered_board(board)
board_censor(covered_board)
p1_points = 0
p2_points = 0
player=1

while count(covered_board) > 0:
    print("\nNow it's playing Player",player)
    print()

    move1_R = int(input("Select a row (0 or 1): "))
    move1_C = int(input("Select a column (0,1,2,3,etc): "))
    print()
    while valid(move1_R,move1_C,covered_board) == False:
        move1_R = int(input("Select a row (0 or 1): "))
        move1_C = int(input("Select a column (0,1,2,3,etc): "))
        print()
    card1 = coord(move1_R, move1_C, covered_board, board)
    print()

    move2_R = int(input("Select a row (0 or 1): "))
    move2_C = int(input("Select a column (0,1,2,3,etc): "))
    print()
    while valid(move2_R,move2_C,covered_board) == False:
        move2_R = int(input("Select a row (0 or 1): "))
        move2_C = int(input("Select a column (0,1,2,3,etc): "))
        print()
    card2 =coord(move2_R,move2_C, covered_board, board)
    print()
    
    if card1 == card2:
        print("It's correct, keep playing!")
        erase_cards(move1_R,move1_C,move2_R,move2_C)
        if player==1:
            p1_points += 1
        else:
            p2_points += 1
    else:
        print("Wrong\n")
        clean(move1_R,move1_C,move2_R,move2_C)
        board_censor(covered_board)
        player = change_player(player)

if p1_points > p2_points:
    print("The winner is Player 1 with", p1_points, "pairs")
elif p1_points < p2_points:
    print("The winner is Player 2 with", p2_points, "pairs")
else:
    print("It´s a tie, both player made", p1_points, "pairs")