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
    for i in range(2):
        for j in range(8):
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
    for i in range(6,8):
        for j in range(8):
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

def execute_move(board, move):
    print("the move is valid")
    board[move[2]][move[3]] = board[move[0]][move[1]]
    board[move[0]][move[1]] = Piece("0","0")


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

        for i in range(1,abs(move_vector)):

            if(board[move[0]][move[1]+(i*vector_sign)].type != "0" ):
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

        for i in range(1,abs(move_vector)):

            if(board[move[0]+(i*vector_sign)][move[1]].type != "0" ):
                print("you can't jump over other pieces")
                return False
        return True
    

    return False

def valid_move_pawn(board, move):

    #white pawns
    if (board[move[0]][move[1]].color == "W"):
        #checks if the player wants to move 1 forward for white
        if(move[0] == move[2]+1 and move[1] == move[3]):
            if(board[move[2]][move[3]].type == "0"):
                return True
        
        #check if player wants to move 2 jumps in first move for white:
        if(move[0] == move[2]+2 and move[1] == move[3] and move[0] == 6):
            #also checks if the pieces is trying to jump over somehting
            if(board[move[2]][move[3]].type == "0" and board[move[2]+1][move[3]].type == "0"):
                return True

        #Trying to caputre
        if(move[0] == move[2]+1 and (move[1] == move[3]+1 or move[1] == move[3]-1)):
            if(board[move[2]][move[3]].color == "b" ):
                return True

    #Black pawns
    if (board[move[0]][move[1]].color == "b"):
        #checks if the player wants to move 1 forward for black
        if(move[0] == move[2]-1 and move[1] == move[3]):
            if(board[move[2]][move[3]].type == "0"):
                return True
        
        #check if player wants to move 2 jumps in first move for black:
        if(move[0] == move[2]-2 and move[1] == move[3] and move[0] == 1):
            #also checks if the pieces is trying to jump over somehting
            if(board[move[2]][move[3]].type == "0" and board[move[2]-1][move[3]].type == "0"):
                return True

        #Trying to caputre
        if(move[0] == move[2]-1 and (move[1] == move[3]+1 or move[1] == move[3]-1)):
            if(board[move[2]][move[3]].color == "W" ):
                return True


    
    print("couldn't move the pawn there")
    return False

def valid_move_knight(board, move):
    if(board[move[2]][move[3]].color == board[move[0]][move[1]].color ):
        print("trying to move piece onto own color")
        return False
    
    v1 = move[2]-move[0]
    v2 = move[3]-move[1]

    if (abs(v1) == 1 and abs(v2) == 2):
        return True
    if (abs(v1) == 2 and abs(v2)== 1):
        return True

def valid_move_bishop(board, move):

    v1 = move[2]-move[0]
    v2 = move[3]-move[1]


    if(board[move[2]][move[3]].color == board[move[0]][move[1]].color ):
        print("trying to move piece onto own color")
        return False

    if(abs(v1) == abs(v2)):
        #for getting the sign of the vector:
        v1_sign = int(v1/abs(v1))
        v2_sign = int(v2/abs(v2))
        #if moving only one square
        if(abs(v1) == 1):
            return True
        for i in range(1,abs(v1)):
            if(board[move[0]+(i*v1_sign)][move[1]+(i*v2_sign)].type != "0"):
                print("can't move over other pieces")
                return False
        return True
    

    return False

def valid_move_queen(board,move):

    if(valid_move_rook(board,move)):
        return True
    if(valid_move_bishop(board,move)):
        return True
    

    return False

def valid_move_emperor(board,move):
    
    v1 = move[2]-move[0]
    v2 = move[3]-move[1]

    if(board[move[2]][move[3]].color == board[move[0]][move[1]].color ):
        print("trying to move piece onto own color")
        return False
    
    if(abs(v1) < 2 and abs(v2) <2):
        return True
    
    return False






def make_move(board, move, player):

    print(player.color + " Turn")
    
    if (move[0] == move[2] and move[1] == move[3]):
        print("can't move the piece to the same spot")
        return False
    
    #if the move is out of bounds
    for i in range(4):
        if (move[i] > 7 and move[i] < 0 ):
            print("Move was out of bounds")
            return False
    

    #checks if the color of the piece at the first position is the same as the player
    print(board[move[0]][move[1]].color)
    if(board[move[0]][move[1]].color == player.color):

        moving_piece = board[move[0]][move[1]]

        if(moving_piece.type.lower() == "r"):
            #checking if the move is a valid move
            if (valid_move_rook(board, move)):
                #make move
                execute_move(board,move)
                return True
        
        if(moving_piece.type.lower() == "p"):
            #checking if the move is a valid move
            if(valid_move_pawn(board,move)):
                #make move
                execute_move(board,move)
                return True

        if(moving_piece.type.lower() == "k"):
            #checking if the move is a valid move
            if(valid_move_knight(board,move)):
                #make move
                execute_move(board,move)
                return True
            
        if(moving_piece.type.lower() == "b"):
            #checking if the move is a valid move
            if(valid_move_bishop(board,move)):
                #make move
                execute_move(board,move)
                return True

        if(moving_piece.type.lower() == "q"):
            #checking if the move is a valid move
            if(valid_move_queen(board,move)):
                #make move
                execute_move(board,move)
                return True
            
        if(moving_piece.type.lower() == "e"):
            #checking if the move is a valid move
            if(valid_move_emperor(board,move)):
                #make move
                execute_move(board,move)
                return True




        return False
    print("this is not your piece")
    return False

def start_game():
    board = create_board()
    p1 = Player("b")
    p2 = Player("W")
    print("Players: " + p1.color, p2.color)




    for i in range(8):
        for j in range(8):
            print(board[i][j].type, end = " ")
        print()    

    round_counter = 0
    players = [p1,p2]

    while(True):
            round_counter+= 1

            print("player turn: " + players[round_counter%2].color)
            next_player = False
            
            while(not next_player):
                numbers_input = input("Enter 4 numbers separated by commas: ")

                # Split the input string into a list of strings
                numbers_list = numbers_input.split(',')

                # Convert the list of strings to a list of int
                numbers_array = [int(num) for num in numbers_list]


                next_player = make_move(board, numbers_array,players[round_counter%2])
                if(not next_player):
                    print("that move is not possible")

                for i in range(8):
                    for j in range(8):
                        print(board[i][j].type, end = " ")
                    print()
        
        
    
        


start_game()
    
