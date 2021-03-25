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
    return print(board2)

def print_board(board): 
    for i in board:
        for j in i:
            print(j," ",end="")
        print()
    return board

cartas = int(input('numero de cartas: '))
card_list = numbers(cartas)
board = board(card_list)
board2 = board2(board)
print(board2)
print('board')
print_board(board)
print('censored board')
board_censor(board2)
coord(0,0,board2,board)