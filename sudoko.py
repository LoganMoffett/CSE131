# 1. Name:
#      Logan
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This code will allow a user to play sudoku without checking any of the rules
# 4. What was the hardest part? Be as specific as possible.
#      Remembering how to use class based programming was the only hard part
#      that I had with this assignement which is why I chose to use it
# 5. How long did it take for you to complete the assignment?
#      1.5 - 2 hours
import json

class sudoku:
    
    def __init__(self):
        """Initialze the class, create 2 conversion tables to go from user input to a manipulatable format and back"""
        self.board_dict = {}
        self.board = {}
        self.conversion_table = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9}
        self.conversion_table_2 = {1: "a", 2: "b", 3: "c",4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i"}

    def get_board(self, file = None):
        """We are going to get the board from the file"""
        # If there is not a file passed in then retrive a file
        if file == None:
            file = self.get_file_path()
        with open(file, "r") as f:
            board = json.load(f)
        # The dict variable is to preserve formatting, while the board is how we are going to manipulate it.
        self.board_dict = board
        self.board = self.board_dict["board"]

    def get_file_path(self):
        """We are going to get the file_path to the board from the user"""
        while True:
            file_path = input("Where is the game located? ")
            # Test to make sure that the file name is a valid file.
            try:
                with open(file_path, "r"):
                    return file_path
            except:
                print("Invalide file path")

    def display_board(self, board = None):
        """We are going to display the board to the user"""
        # Declare counter variables that will be used in display info
        x_counter = 1
        y_counter = 0
        # Print the top, this is done once
        print("   A B C D E F G H I")
        for y in range(0, 9):
            if y_counter % 3 == 0 and y != 0:
                print("   -----+-----+-----")
            y_counter += 1
            for x in range(0, 9):
        # If it is the first spot on the board we print the side bar
                if x == 0:
                    print(y + 1," ",end="")
        # The last spot we want a new line printed
                if x == 8:
                    if self.board[y][x] != 0:
                        print(self.board[y][x])
                    else:
                        print(" ")
        #whenever it is not a spot with a divider, print this
                elif x_counter % 3 != 0:
                    if self.board[y][x] != 0:
                        print(self.board[y][x], "",end="")
                    else:
                        print("  ", end="")
        # This is where we print the dividers for formating
                else:
                    if self.board[y][x] != 0:
                        print(f"{self.board[y][x]}|", end="")
                    else:
                        print(" |", end="")
                x_counter += 1

    def display_instructions(self):
        """Display any instruction for the user"""
        print("Enter S to save and quit")
        print("Enter p to see possbile answers")

    def quit(self, file = None):
        """Save the board to a new file and then close the code"""
        # If a file wasn't passed automatically, then retrive one
        file = input("Where would you like to save the board? ")
        
        # Convert the board into a savable format
        self.board_dict["board"] = self.board

        #Put the board into the save file
        with open(file, 'w') as outfile:
            json.dump(self.board_dict, outfile)

    def get_location(self, user_input = None):
        """Get the location from the user, and return it in an acceptable manor"""
        counter = 0
        while True:
            user_input = input("> ")
            # If the users input has more then 2 characters then the input is invalid
            if len(user_input) > 2:
                print("Enter a single letter and number input, or s or p")
            # If they enter a s then they are saving and quiting
            elif user_input == "s" or user_input == "p":
                return user_input
            elif len(user_input) < 2:
                print("Enter a single letter and number or s or p")
            else:
            #If it isn't a basic input then process it to use it.
                location = self._process_input(user_input)
            # Return the valid input
                return location
    
    def _process_input(self, user_input):
        location = []
        for x in user_input:
            location.append(x.lower())
            
        # If the letter is in the second spot instead of the first, reverse the array
        if location[1].isalpha() == True:
            save_state = user_input
            location[0] = save_state[1]
            location[1] = save_state[0]
        # Check if the input is valid
        if location[0] not in self.conversion_table:
            print("enter a valid letter")
            location = self.get_location()
            location[0] = self.conversion_table_2[location[0]]

        # Convert the first letter into a usable number
        location[0] = self.conversion_table[location[0].lower()]

        # Check to see if the location is already full
        if self.board[int(location[1]) - 1][int(location[0]) - 1] != 0:
            print("Location is full")
            location = self.get_location()

        # Return the valid input
        return location

    
    def get_value(self, location, value = None):
        """gets the value from the user"""
        while True:
            # Check to see if the first input is a number or not, if it is a number
            # Convert to a Letter.
            if value == None:
                if isinstance(location[0], int) == True:
                    location[0] = self.conversion_table_2[location[0]]
                # Turn the array into a string for formating
                location = "".join(location)
                value = input(f"What value goes into {location}? ")
                if value.isalpha():
                    print("Enter a number between 1-9")
                    value = self.get_value(location)
                try:
                    value = int(value)
                except:
                    print("Enter a whole number between 1-9")
                    value = self.get_value(location)
                if int(value) > 9:
                    print("Enter a number between 1-9")
                    value = self.get_value(location)
                if int(value) <= 0:
                    print("Enter a number between 1-9") 
                    value = self.get_value(location)
            return int(value)

    def edit_board(self, location, value):
        # Check to see if the location is a string or int, if it is a string convert to int
        if isinstance(location[0], str) == True:
            location[0] = self.conversion_table[location[0]]
        # If the place is empty then replace it with the user input
        if self.board[int(location[1]) - 1][int(location[0]) - 1] == 0:
            self.board[int(location[1]) - 1][int(location[0]) - 1] = value
        # Display an error message if it is not empty
        else:
            print("square if full, please try another square")

    def take_turn(self, location = None, value = None, loop = None):
        """We are going to take the turn for the user
        this starts with processing the input and then editing the board"""
        #I made input = None at the start for easy troublshooting and to use with other programs
        if location == None:
            location = self.get_location()
        # Get a input from the use

        if location == "s":
            self.quit()
        elif location == "p":
            self.possible_moves()
        else:
            value = self.get_value(location)
            # display the board and edit the board
            if self.is_valid_move(location, value) == True:
                    self.edit_board(location, value)
            else:
                print("invalide move")
            self.display_board()

            # Loop through a turn till the game ends
        while loop == None:
            location = self.get_location()
            if location == "s":
                self.quit()
                return
            value = self.get_value(location)
            if self.is_valid_move(location, value) == True:
                self.edit_board(location, value)
                self.display_board()
            else:
                print("invalide move")
                self.display_board()
        
    def possible_moves(self, location = None):
        possible_moves = []
        if location == None:
            user_input = input("What are the coordinates you want to check? ")
            location = self.get_location(user_input)
        for x in range(1, 10):
            if self.is_valid_move(location, x) == True:
                possible_moves.append(x)
        for x in possible_moves:
            print(x, " ", end="")
        print("")


    def is_valid_move(self, location, value):
        value = int(value)
        if isinstance(location[0], str) == True:
            location[0] = self.conversion_table[location[0]]
        location[0] = int(location[0])
        location[1] = int(location[1])
        if self._check_row(location, value) == False:
            return False
        if self._check_column(location, value) == False:
            return False
        if self._check_square(location, value) == False:
            return False
        return True

    def _check_row(self, location, value):
        for x in range(0, 9):
            if x != location[0]:
                if value == int(self.board[int(location[1]) - 1][int(x)]):
                    return False
        return True 
    
    def _check_column(self, location, value):
        for y in range(0, 9):
            if y != location[1]:
                if value == self.board[y][location[0] - 1]:
                    return False
        return True

    def _check_square(self, location, value):
        range_conversion = {0: 0, 1: 0, 2: 0, 3: 3, 4: 3, 5: 3, 6: 6, 7: 6, 8: 6}
        x_range = range_conversion[location[0] - 1]
        y_range = range_conversion[location[1] - 1]
        for y in range(0, 3):
            for x in range(0, 3):
                if x + x_range != location[0] and y + y_range != location[1]:
                    if self.board[x + x_range][y + y_range] == value:
                        return False
        return True

    def play_game(self):
        """Initiate the game"""
        # Get the board from the user to use
        self.get_board()
        # Display the board
        self.display_board()
        # Take turn will continuasly loop through a full turn until the user indicates to stop
        self.take_turn()
        # Once the game ends display the board for the user to see what it looks like at the end
        self.display_board()

    def __main__(self):
        """Start game play """
        self.play_game()

game = sudoku()
game.__main__()