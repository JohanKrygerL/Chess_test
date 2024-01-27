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
    

    # for i in range(8):
    #     for j in range(8):
    #         print(board[i][j].type, end = " ")
    #     print()

    
    return board

def valid_move_rook(board, move):



    if (move[0] == move[2]):
        #the piece is moving along the rows
        move_vector = move[3]-move[1]
        vector_sign = 1

        if (move_vector < 0):
            vector_sign = -1

        #for if it only moves 1 square
        if (abs(move_vector) == 1):
            if(board[move[0]][move[1]].color == board[move[2]][move[3]].color):
                print("you are trying to move to the same color")
                return False 
            return True

        for i in range(abs(move_vector)-1):

            if(board[move[0]][move[1]+(1+i*vector_sign)].type != "0" ):
                print("you can't jump over other pieces")
                return False
        return True

    if (move[1] == move[3]):
        #the piece is moving along the rows
        move_vector = move[2]-move[0]
        vector_sign = 1

        if (move_vector < 0):
            vector_sign = -1

        #for if it only moves 1 square
        if (abs(move_vector) == 1):
            if(board[move[0]][move[1]].color == board[move[2]][move[3]].color):
                print("you are trying to move to the same color")
                return False 
            return True

        for i in range(abs(move_vector)-1):

            if(board[move[0]+(1+i*vector_sign)][move[1]].type != "0" ):
                print("you can't jump over other pieces")
                return False
        return True
    
    print("couldn't move the rook there")
    return False




def make_move(board, move, player):
    
    if (move[0] == move[2] and move[1] == move[3]):
        print("can't move the piece to the same spot")
        return False
    
    #if the move is out of bounds
    for i in range(4):
        if (move[i] > 7 and move[i] < 0 ):
            print("Move was out of bounds")
            return False
    

    #checks if the color of the piece at the first position is the same as the player
    if(board[move[0]][move[1]].color == player.color):

        moving_piece = board[move[0]][move[1]]

        if(moving_piece.type.lower() == "r"):

            #checking if the move is a valid move
            if (valid_move_rook(board, move)):
                #make move
                print("the move is valid")
                board[move[2]][move[3]] = board[move[0]][move[1]]
                board[move[0]][move[1]] = Piece("0","0")
                return True


            





        return False
    print("this is not your piece")
    return False

def start_game():
    board = create_board()
    p1 = Player("b")
    p2 = Player("W")
    print(p1.color, p2.color)




    for i in range(8):
        for j in range(8):
            print(board[i][j].type, end = " ")
        print()    

    while(True):


        print(make_move(board, [4,0,4,2],p1))
        for i in range(8):
            for j in range(8):
                print(board[i][j].type, end = " ")
            print()

        return True    
        


start_game()
    
