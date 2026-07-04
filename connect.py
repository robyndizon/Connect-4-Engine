class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

        # Add code here to put the numbers underneath
        s += ' '  # first space for alignment with the board
        for col in range(self.width):
            s += str(col % 10) + ' '  # display single digits for column numbers
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox): 
        """
        to search for the first available (empty) spot in the chosen col starting from 
        the bottom most row and going up due to the checkers falling to the lowest
        available row in a col
        """
        # height reps number of rows on board and i of last row is -1 of height
        # stop condition and loop will stop when row reached -1 (never)
        # step size and loop decrements row by 1 on each iteration
        for row in range(self.height - 1, -1, -1): 
            if self.data[row][col] == ' ':
                self.data[row][col] = ox 
                break
            
    def clear(self): 
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '  # set each cell to empty space
        
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        if c < 0 or c >= self.width:
            return False
        
        # check if the topmost row in the column is empty
        if self.data[0][c] != ' ':
            return False
        
        # if both checks pass, the move is allowed
        return True

    def isFull(self):
        # any column that allowsMove is true, the board not full
        for col in range(self.width):
            # if any col allows move, not full
            if self.allowsMove(col):
                return False
        # if no col allows more, board full
        return True
    
    def delMove(self, c): 
        if c < 0 or c >= self.width:
            return              # does nothing bc invalid col
        # finding topmost checker in the col and remove it 
        for row in range(self.height):
            # found space not empty 
            if self.data[row][c] != ' ':
                # remove checker
                self.data[row][c] = ' '
                # only remove top most checker
                break 
    
    def winsFor(self, ox):
        # player ox wins the game by getting 4 checkers in a row
        h = self.height
        w = self.width
        d = self.data 

        # check all positions on the board 
        for row in range(h):
            for col in range(w):
                # horizontal right
                if col <= w - 4 and d[row][col] == ox and d[row][col + 1] == ox and d[row][col+2] == ox and d[row][col+ 3] == ox: 
                    return True
                
                # vertical down
                if row <= h - 4 and d[row][col] == ox and d[row+1][col] == ox and d[row+2][col] == ox and d[row+3][col] == ox:
                    return True 
                
                # diagonal down right
                if row <= h - 4 and col <= w - 4 and d[row][col] == ox and d[row+1][col+1] == ox and d[row+2][col+2] == ox and d[row+3][col+3] == ox:
                    return True 
                
                # diagonal down left 
                if row <= h - 4 and col >= 3 and d[row][col] == ox and d[row+1][col-1] == ox and d[row+2][col-2] == ox and d[row+3][col-3] == ox:
                    return True                

        return False
    
    def hostGame(self):
        # hosts game, alternates between X and O 
        print ("Welcome to Connect Four!")

        # loops to handle the turns til game over
        while True: 
            # print board before each move 
            print(self)

            # player X turn 
            while True:
                user_column = input("X's choice: ")
                # check if the input is a valid integer and within the allowed range
                if user_column.isdigit():   # built in func that checks if user input in "0123456789"
                    # if true, converts to a int
                    user_column = int(user_column)
                    if self.allowsMove(user_column):
                        self.addMove(user_column, 'X')    # if valid move then lets that X be added
                        break  # and exits loop
                    else:
                        print("Column " + user_column + " is not a valid move. Try again.")
                else:
                    print(user_column + " is not a valid column number. Please enter a number between 0 and" + (self.width - 1) )

            # check if X has won
            if self.winsFor('X'):
                print(self)
                print("X wins, congratulations!")
                break  # End the game

            # check if the board is full and tie
            if self.isFull():
                print(self)
                print("The board is full, it's a tie!")
                break  # End the game

            # player O turn
            while True:
                print(self)
                user_column = input("O's choice: ")

                # check if the input is a valid integer and within the allowed range
                if user_column.isdigit(): # built in func that checks if user input in "0123456789"
                    user_column = int(user_column)
                    # if true, converts to a int
                    if self.allowsMove(user_column):
                        self.addMove(user_column, 'O')    # if valid move then lets that O be added
                        break  # and exits loop
                    else:
                        print("Column " + user_column + " is not a valid move. Try again.")
                else:
                    print(user_column + " is not a valid column number. Please enter a number between 0 and " + (self.width - 1))

            # check if 'O' has won
            if self.winsFor('O'):
                print(self)
                print("O wins, congratulations!")
                break  # end the game

            # check if the board is full and tie
            if self.isFull():
                print(self)
                print("The board is full, it's a tie!")
                break  # end the game

        

# This is the end of the Board class

b = Board(7,6)

b.hostGame()


"""
classes and objects
override methods in custon class definitions
define and call custom methods for a class 
use self in oop 
use nested for loops
choose between types of loops
"""
