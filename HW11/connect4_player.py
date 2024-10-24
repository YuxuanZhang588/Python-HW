
"""
Implementation of a Connect-4 Player class.

Author: David Zhang  Thatcher Craig

Time spent: 7 hours
"""
#from connect4 import Board
import random
GOOD = 100
BAD = 0
TIE = 50
FULL = -1
class Player:
    """A type for representing the behavior of a Connect4 player 

    Attributes:
        side - a single character string that is either 'X' or 'O', denoting the
              side this Player will be taking.
        ply - a non_negative integer representing how many moves into the future
             this Player will look in order to evaluate the "goodness" of a move
        is_random - a boolean value denoting how this Player will handle
                   situations when there exist multiple moves that are equally
                   good. If set to True, then this Player will break ties
                   randomly; if False, then the Player will choose the left-most
                   column among the tied columns.
    """
    
    def __init__(self, side, ply, is_random):
        """This constructor is used to initialize the parameters listed below. 
       
        Parameters:
            side - a character that represents which side this player will be
            taking
            ply - an integer representing how many moves this player will be
            looking into the future
            is_random - a boolean value determining how player will decide to
            break ties
           
        Returns:
            String of each characteristic of Player. The side,
            the ply and how the computer decides to break ties
        """
        self.side = side
        self.ply = ply
        self.is_random = is_random
        
    def __str__(self):
        """Returns a string of the values assigned to each attribute: The side,
        the ply, and the randomness of the computer
       
        Parameters:
            None
           
        Returns:
            String of each characteristic of Player. The side,
            the ply and how the computer decides to break ties
        """
        if self.is_random == True:
            return ("Player for %s, ply = %d, breaks ties randomly"
                    % (self.side, self.ply))
        else:
            return ("Player for %s, ply = %d, breaks ties deterministically"
                    % (self.side, self.ply))
        
    def opponent(self):
        """Determines what checker the human is using and returns the opposite
        checker. This code is used to determine what checker the computer will
        be using for the rest of the game.
       
        Parameters:
            None
           
        Returns:
            A string of character O
            A string of character X
        """
        if self.side == 'X':
            return 'O'
        else:
            return 'X'
        
    def evaluate_board(self,b):
        """Evaluates the current board and returns a score for the current
        situation.
        
        It goes through and uses win_for function from the connect4 code
        to determine whether or not there is already a win on the board for a
        side. If there is no win for either the computer or yourself then it
        will return a score of 50 meaning neither side has won
       
        Parameters:
            b - the current board
           
        Returns:
            GOOD - A score of 100 (good score)
            BAD - A score of 0 (bad score)
            TIE - A score of 50 (neither a good score or bad score)
        """
        if b.win_for(self.side):
            return GOOD
        elif b. win_for(Player.opponent(self)):
            return BAD
        else:
            return TIE
        
    def score_columns(self,b):
        """Returns a list of scores, where the cth score represents the
        "goodness" of making the next move in the cth column.
        
        This function uses recursive method to look into the future by a
        specified amount of steps, which is determined by self.ply. And this
        "goodness" if quantified by determining what happens in the game after
        self.ply moves. In specific, if a move is beneficial to self.side, then
        it gets a score of 100. A 0 means this move is beneficial to the
        opponent. So the score for self_goodness should be the score of opponent
        goodness subtracted from 100.
        
        Parameters:
            b - the current board
            
        Returns:
            self_goodness - a list of scores of making the next move in the
                            corresponding columns.
        """
        
        current_side = 'X'
        self_goodness = [TIE] * b.width 
        opponent = Player.opponent(self)
        for i in range(len(self_goodness)):
            #1st base-case, when any side wins the game or the board is full.
            if b.win_for(self.side) or b.win_for(opponent) or b.is_full():
                self_goodness[i] = Player.evaluate_board(self,b)
            #2nd base_case, when the column is full.
            elif b.allows_move(i) == False:
                self_goodness[i] = FULL
            #3rd base_case, when self.ply is zero.
            elif self.ply == 0:
                self_goodness[i] = TIE
            #Recursive method.
            else:
                b.add_move(i,self.side)
                opponent_goodness = []
                opponent_goodness = ((Player(opponent, self.ply-1,
                                             self.is_random)).score_columns(b))
                self_goodness[i] = GOOD - max(opponent_goodness)
                #Turns opponent's score into self_score.
                #It pick the biggest score opponent can get, and subtract that
                #from 100.
                b.delete_move(i)
        return self_goodness
    
    def best_move(self,scores):
        """Returns the number of the best move column.
        
        This function takes a non-empty list of integers from score_columns
        function, and returns the index of the maximum number in the list. If
        there are several maximum numbers in the list, when self.is_random is
        True, it randomly choose one from these numbers; when self.is_random is
        False, it choose the left-most number.
        
        Parameters:
            scores - a list of scores returned from the score_column function.
            
        Returns:
            If self.is_random is True, it returns the index of a randomly chosen
            number among the maximum numbers in the list. If self.is_random is
            False, it returns the index of the left most maximum number.
        """
        indexes = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                indexes.append(i)
        if self.is_random == True:
            return random.choice(indexes)
        else:
            return indexes[0]
    
    def next_move(self,b):
        """Returns an integer denoting the column number that Player object
           choose to move to.
           
        Parameters:
            b - the current board
            
        Returns:
            An integer representing the move Player choose to make.
        """
        return self.best_move(self.score_columns(b))
                
          
def main():
    """Test functions"""
    b = Board(7,6)
    b.set_board('1211244445')
    print(b)
    
    print(Player('X', 2, True).next_move(b))
    

    

if __name__ == "__main__":
    main()

        