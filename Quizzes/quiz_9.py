
"""
Solutions to the programming problems from quiz #9.

Author: David Zhang
"""

def pretty_print(board):
    """ Prints a Minesweeper board in a human-friendly format.
    
    If the input board is None, then no output is produced.
    
    Parameters:
        board - a list of strings representing the board to be printed.
        
    Returns:
        None.
        
    """
    #print board
    if (board == []) or (board == None):
        print ('Empty board or No board to print')
    else:
        print ('pretty_print:')
        for i in range(len(board)):        # go through every row in board
            string = ''                    # initialize a row string
            for j in range(len(board[0])): # go through every cell in row
                string += board[i][j]      # concatenate cells, they are strings
            print (string)                 # print a row
    
def solve_board(board):
    """ Solves the given Minesweeper board.
    
    Solving a board involves replacing all occurrences of . in the original
    board description with a single digit between 0-8 indicating how many of
    that cell's neighbors contain mines.
    
    Parameters:
        board - a list of strings describing a Minesweeper board. Each string
                is made up of .s and *s, with the former indicating empty
                cells and the latter indicating mines.
                
    Returns:
        A list of strings, where each . in one of the original strings has 
        been replaced with a digit between 0-8, denoting the number of
        adjacent cells that contain a mine.
        
    Pseudocode:
        The function uses nested for-loop to run through the board, with outer
        loop representing height, and inner-loop width. Then the function uses
        if statement to find out special situations when the cell is on the
        boundaries. The function also uses try, except to aviod IndexErrors,
        in this case when j+1 or i+1 exceed the list boundaries.
    """
    

    height = len(board)
    width = len(board[0])
    count = 0
    solved_line = ''
    solved = []
    for i in range(height):
        for j in range(width):
            if board[i][j] != "*":
                if i-1 >= 0:
                    try:
                        if j-1 >= 0:
                            if board[i-1][j-1] == "*":
                                count+=1
                    except:
                        count+=0
                    try:
                        if board[i-1][j] == "*":
                            count+=1
                    except:
                        count+=0
                    try:
                        if board[i-1][j+1] == "*":
                            count+=1
                    except:
                        count+=0
                try:
                    if j-1 >= 0:
                        if board[i][j-1] == "*":
                            count+=1
                except:
                    count+=0
                try:
                    if board[i][j+1] == "*":
                        count+=1
                except:
                    count+=0
                try:
                    if j-1 >= 0:
                        if board[i+1][j-1] == "*":
                            count+=1
                except:
                    count+=0
                try:
                    if board[i+1][j] == "*":
                        count+=1
                except:
                    count+=0
                try:
                    if board[i+1][j+1] == "*":
                        count+=1
                except:
                    count+=0
                solved_line+=(str(count))
                count = 0
            else:
                solved_line+=("*")
        
        solved.append(solved_line)
        solved_line = ''
    return solved
        

def main():
    """ Tester function. """
    
    print ()
    print ("Testing pretty_print()")
    print ()
    pretty_print(["*111",
                  "2*22",
                  "33*3",
                  "444*",
                  "5555"])
    
    print ()
    print ("Testing solve_board()")
    print ()
    print ("Board 1")
    pretty_print(["..",
                  ".*",
                  ".."])
    print ()
    solved = solve_board(["..",
                          ".*",
                          ".."])
    print ('solved_board')
    pretty_print(solved)
    
    print ()
    print ("Board 2")
    pretty_print(["*.*.*",
                  "..*..",
                  "*****",
                  ".....",
                  "..**."])
    print ()
    solved = solve_board(["*.*.*",
                          "..*..",
                          "*****",
                          ".....",
                          "..**."])
    print ('solved_board')
    pretty_print(solved)
    
    print ()
    print ("End Test")
    

   
    
if __name__ == "__main__":
    main()
