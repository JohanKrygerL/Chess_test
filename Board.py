import numpy as np

class Piece:
    def __init__(self, type, color):
        self.type = type
        self.color = color

class Player:
    def __init__(self, color):
        self.color = color
        pass



def create_board():

    board = [[Piece("0","0") for i in range(8)] for j in range(8)]

    #setting up the black pieces
    for i in range(8):
        for j in range(2):
            board[i][j].color = "b"
    for i in range(8):
        board[1][i].type = "p"

    board[0][0].type = "r"
    board[0][7].type = "r"
    board[0][1].type = "k"
    board[0][6].type = "k"
    board[0][2].type = "b"
    board[0][5].type = "b"
    board[0][3].type = "e"
    board[0][4].type = "q"
    
    #setting up the white pieces:
    for i in range(8):
        for j in range(6,8):
            board[i][j].color = "W"
    for i in range(8):
        board[6][i].type = "P"

    board[7][0].type = "R"
    board[7][7].type = "R"
    board[7][1].type = "K"
    board[7][6].type = "K"
    board[7][2].type = "B"
    board[7][5].type = "B"
    board[7][3].type = "E"
    board[7][4].type = "Q"
    

    for i in range(8):
        for j in range(8):
            print(board[i][j].type, end = " ")
        print()

    
    return board



def make_move(board, move, player):


    
