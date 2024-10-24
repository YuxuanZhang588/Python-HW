"""
Creates the game Connect-4.

Author: David Zhang  Thatcher Craig

"""
class Board:
    """Creates a data type that defines the state and behavior of a Connect-4
       game board.
    
    Attributes:
        height: An integer representing the height of the game board.
        width: An integer representing the width of the game board.
        data: A two-dimensional array representing the current state of each
              cell in the game board. The contents of this nested list will be
              characters, strings of length 1. An empty slot should be
              represented by ' ', player 1's pegs should be represented by 'X'
              (the capital 'x'), and player 2's pegs should be represented by
              'O'(the capital o).
              
    """
    def __init__(self, width, height):
        """Constructs a new board object with the value of width and height, and
        initialize the two-dimensional list, data, that represents the board.
        
        Parameters:
            width: the width of the board
            height: the height of the board
        
        Returns:
            None.
        """
        self.data = []
        self.width = width
        self.height = height
        for row in range(self.height):#This creates a two-dimensional list.
            self.data.append([])
            for col in range(self.width):
                self.data[row].append(' ')
                
    def __str__(self):
        """Returns a printable represenation of the board.
        
        Parameters:
            None.
        
        Returns:
            The game board in a string form.
        """
        board = ''#Board should be printed as a string.
        self.data = self.data[::-1]#We first invert the data list because it
                                   #makes it easier to create for-loop.
        for row in range(self.height):
            for col in range(self.width):
                board += "|" + self.data[row][col]#This links the data with the
            board += "|" + "\n"                   #board, and draws the body of
                                                  #the board.
        for col in range(self.width * 2 + 1):#This draws the line of dashes
            board += "-"                     #below the body of the board.
        board += "\n"
        for num in range(self.width):#This draws a row of index number for
            new_num = num % 10       #columns.
            board += " " + str(new_num)
        self.data = self.data[::-1]#We invert the data back to its original
                                   #structure.
        return board
   
    def add_move(self, column, side):
        """Add a peg into the game board for one side.

        Parameters:
            column: the column where the player wants to add a peg
            side: the side of the player
        
        Returns:
            None.
        """
        for row in range(len(self.data[:])):
            if self.data[row][column] == " ":
                self.data[row][column] = side
                break #We don't need to run through every row.
        
    def allows_move(self,column):
        """Tests if the player's move is a legal move.
        
        Parameters:
            column: the column where the player wants to add a peg
            
        Returns:
            It returns True if the player's move is legal. It returns False if
            the player's move it illegal.
        """
        self.data = self.data[::-1]#We first invert the data list because it
                                   #makes it easier to create for-loop.
        if_col_full = []
        if column >= 0 and column <= len(self.data):
            for row in range(len(self.data)):
                if_col_full.append(self.data[row][column])
            if ' ' in if_col_full:
                self.data = self.data[::-1]#We invert the data back to its 
                                           #original structure.
                return True
            else:
                self.data = self.data[::-1]
                return False
        else:
            self.data = self.data[::-1]
            return False
        
    def clear(self):
        """Clears the board that calls it.

        Parameters:
            None.
        
        Returns:
            None.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '
                
    def set_board(self,move_string):
        """Accepts a string of column numbers and places alternating
        pegs in them.
        
        For example, b.set_board("012345") would place alternating
        "X"s and "O"s on the bottom-most row (starting with an "X").
        
        Parameters:
            move_string - a string containing a sequence of moves to play.
            
        Returns:
            None.
        """
        next_side = "X"
        for col_string in move_string:
            col = int(col_string)
            if col >= 0 and col <= self.width:
                self.add_move(col, next_side)
            if next_side == "X": #Alternate between 'X' and 'O'.
                next_side = "O"
            else:
                next_side = "X"
                
    def is_full(self):
        """Tests if the calling Board object is completely filled with pegs.

        Parameters:
            None.
            
        Returns:
            It returns True if the Board object that calls it is filled with
            pegs, returns False if there is still space in the board.
        """
        result = True
        for row in self.data:
            if ' ' in row:
                result = False
        return result
        
    def delete_move(self,column):
        """Removes the top peg from column.

        Parameters:
            column: the column where the player wants to add a peg
        
        Returns:
            None.
        """
        self.data = self.data[::-1]
        for row in range(len(self.data)):
            if self.data[row][column] != ' ':
                self.data[row][column] = ' '
                break 
        self.data = self.data[::-1]
        
    def win_for(self,side):
        """Tests if one side has four pegs in a row.
        
        Parameters:
            side: the side of the player
        
        Returns:
            It returns True if the side has four pegs in a row, and False
            otherwise.
        
        Pseudocode:
            Same as what we did in the minesweeper, we use for-loop to run
            through each cell. We divide it up into four different cases:
            horizontal/vertical straight line, and diagnals with two different
            directions. Then we just check if such cases exist in the data set.
        """
        data = self.data[:]
        win = False
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == side:
                    try:#We uses try/except to avoid IndexError.
                        if data[row][col + 1] == side:
                            if data[row][col + 2] == side:
                                if data[row][col + 3] == side:
                                    win = True #check if any side has four pegs
                                               #in a row in a horizontal
                                               #straight line.
                        elif data[row + 1][col] == side:
                            if data[row + 2][col] == side:
                                if data[row + 3][col] == side:
                                    win = True #check if any side has four pegs
                                               #in a row in a vertical straight
                                               #line.
                        elif data[row + 1][col + 1] == side:
                            if data[row + 2][col + 2] == side:
                                if data[row + 3][col + 3] == side:
                                    win = True #check if any side has four pegs
                                               #in a row in a diagnal line, from
                                               #lower left to upper right.
                        elif data[row + 1][col - 1] == side:
                            if data[row + 2][col - 2] == side:
                                if data[row + 3][col - 3] == side:
                                    win = True #check if any side has four pegs
                                               #in a row in a diagnal line, from
                                               #lower right to upper left.
                    except IndexError:
                        return win
        return win
    
    def host_game(self):
        """Hosts a full game of Connect-4.
        
        Parameters:
            None.
        
        Returns:
            None.
        """
        print('Welcome to Connect-4!')
        side = 'X'
        side_list = ['X', 'O']
        count = 0
        while self.win_for(side) == False or self.is_full() == True:
        #When any side wins the game, or when the board is full, it's gonna exit
        #the while loop.
            print(self.__str__())
            side = side_list[count%2]
            count += 1
            column = int(input("%s's move: " % (side)))
            while self.allows_move(column) == False:
            #Check if it is a legal move. If not, it's gonna let the user to
            #enter another move.
                column = int(input("%s's move: " % (side)))
            self.add_move(column, side)
        print("%s wins -- congratulations!" % (side))
        print(self.__str__())#Print the board for one last time.
        
         
'''
Change the code below, as required, to run the program
'''
def main():
    b = Board(7,6)
    b.host_game()
    """
    A wrapper function that calls the functions above
    """
    
#Testing Board,add_move,allows_move and clear:
    '''
    b = Board(6,7)
    b.add_move(0, 'X')
    b.add_move(0, 'O')
    b.add_move(0,'X')
    b.add_move(0,'O')
    print(b)
    print(b.allows_move(-1))
    print(b.allows_move(0))
    print(b.allows_move(1))
    print(b.allows_move(2))
    b.clear()
    '''  
#Testing is_full:
    '''
    b = Board(2,2)
    print(b.is_full())
    b.add_move(0, 'X')
    print(b.is_full())
    b.add_move(1,'O')
    print(b.is_full())
    b.set_board("0011")
    print(b.is_full())
    print(b)
    '''
#Testing delete_move:
    '''
    b = Board(2, 2)
    b.set_board("0011")
    b.delete_move(1)
    b.delete_move(1)
    b.delete_move(1)
    b.delete_move(0)
    print (b)
    '''
#Testing win_for:
    '''
    b = Board(7, 6)
    b.set_board("00102030")
    print (b.win_for('X'))
    print (b.win_for('O'))
    b = Board(7, 6)
    b.set_board("23344545515")
    print (b)
    print (b.win_for("X"))
    print (b.win_for("O"))
    '''
    
'''
Do NOT change the code below
'''
   
if __name__ == "__main__":
    main()