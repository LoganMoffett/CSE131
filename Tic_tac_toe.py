# 1. Name:
#      Logan Moffett
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was dealing with the JSON files. I have only worked with them once
#      before and not using the format that was given.
# 5. How long did it take for you to complete the assignment?
#      about 2.5 hours.

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# Extra variable to determin who's turn it is
turn = 0
# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                "BLANK", "BLANK", "BLANK",
                "BLANK", "BLANK", "BLANK",
                "BLANK", "BLANK", "BLANK" ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # open the file and save the information
    with open(filename, 'r') as file:
        blank_board = json.load(file)
    # The JSON file has different formats for how it saves spaces so
    # create board to store the info
    board = []
    # Go through the board and ensure that it handles different formats
    for item in blank_board:
        if item == "BLANK":
            board.append(BLANK)
        elif item == " ":
            board.append(BLANK)
        else:
            board.append(item)
    return board

def save_board(filename, board):
    '''Save the current game to a file.'''
    # open the file and dump the info into it.
    with open(filename, 'w') as outfile:
        json.dump(board, outfile)


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # hardcoded board formating
    print(f"{board[0]}  | {board[1]} | {board[2]} ")
    print(f"---+---+---")
    print(f"{board[3]}  | {board[4]} | {board[5]} ")
    print(f"---+---+---")
    print(f"{board[6]}  | {board[7]} | {board[8]} ")

def is_x_turn(turn):
    '''Determine whose turn it is.'''
    # find out whos turn it is. The code will either send a one or a zero.
    if turn == 0:
        return True
    else:
        return False


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

def play_game():
    '''Play the game of Tic-Tac-Toe.'''
    # open up the board
    board = read_board("CSE131/tic_tac_toe.json")

    # Set initial variables
    user_input = ' '
    turn = 0

    # Start the loop
    while game_done(board, message = True) == False:
        display_board(board)

        # If it is x's turn allow them to play
        if is_x_turn(turn):
            user_input = input("X> ")

            # If the input is a number between 1-9 and the corrisponding spot on the board is empty, play
            if user_input.isnumeric() and int(user_input) < 10 and board[int(user_input) - 1] == BLANK:
                board[int(user_input) - 1] = X
                turn = turn + 1

            # If the user wants to quit then run this code
            elif user_input == "q":
                save_board("CSE131/tic_tac_toe.json", board)
                return True

            # anything else is invalid
            else:
                print("invalid move")

        # It is O's turn
        else:
            user_input = input("O> ")

            # Check if the answer is a number between 1-9 and corisponds to a empty space
            if user_input.isnumeric() and int(user_input) < 10 and board[int(user_input) - 1] == BLANK:
                board[int(user_input) - 1] = O
                turn = 0
                print(turn)
            
            # Alows the user to quit
            elif user_input == 'q':
                save_board("CSE131/tic_tac_toe.json", board)
                return True

            # If it is anything else it is an invalid move.
            else:
                print("invalid move")
    display_board(board)
    return False
# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")
display_board(read_board("CSE131/tic_tac_toe.json"))

# Run the game.
clear = False
play = False

clear = input("would you like to clear the board before playing? y/n ")
if clear == 'y':
    save_board("CSE131/tic_tac_toe.json", blank_board["board"])
while play != "n":
    play_game()
    play = input("would you like to play again? y/n ")



