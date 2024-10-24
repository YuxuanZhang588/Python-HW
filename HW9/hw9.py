
"""
Programs for Homework 9

Author: David Zhang  Thatcher Craig

"""
import turtle

def recursive_delete(s,char):
    """ Deletes specific character in a given string.

    Parameters:
        s - a string
        char - some character in the alphabet
    
    Return:
        A string that remains after deleting all occurences of some letter
        from a string.
    
    Pseudocode:
        The base case is once there are no characters left in the string,
        return the modified string.
        What we want is if the first character of the string equals the
        character we want to remove, set s = to the remaining string
        and call the function with the remainder of the string.
        If the first character does not equal the character we want to remove,
        return that character of the string and then call the function again
        with the remainder of the string.
        This means once the function has been called enough times, the string
        will be empty and will return all of the characters of the string that
        are not equal to the character we want to remove.
    """
    #base case
    if s == '':
        return s
    if s[0] == char:
        s = s[1:]
        return recursive_delete(s,char)
    else:
        return s[0]+recursive_delete(s[1:],char) 
    ## Your code here
        
def double_countdown(n):
    ''' Generate a sequence of double countdown.

    Parameters:
        n - the number to begin with in the countdown.
    
    Return:
        A a sequence of double countdown as a string.
        
    Pseudocode:
        By looking at the sequence of double count down
        5 4 3 2 1 0 1 2 3 4 5
        We know we need to build the string from the outside to the inside.
        The base-case is when n is reduced to zero, then the function should
        return zero, which should always be in the center of the string, and we
        just add the number n around the 0.
    '''
    s = ''
    if n == 0:
        s = '0'
        return s
    else:
        s = str(n) + ' ' + double_countdown(n-1) + ' ' + str(n)
        return s

def half_tree(length, level):
    ''' Draws half of the htree.

    Parameters:
        length - the length of the main segment of the htree
        level - the level of the htree
   
    Pseudocode:
        The base case is when level = 0, and then it will return to after the
        first recursive call.
        For each level the turtle will draw a line and turn left.
        Once the level reaches 0 the turtle will then turn around and replicate
        what it just drew on the bottom half of the H tree.
        The turtle will end where at the position where it started from. 
    '''
    if level == 0:
        return
    
    turtle.forward(length)
    turtle.left(90)
    half_tree(length / 2,level - 1)
    turtle.right(180)
    half_tree(length / 2,level - 1)
    turtle.left(90)
    turtle.back(length)
    
def htree(length,level):
    ''' Draws the complete htree.

    Parameters:
        length - the length of the main segment of the htree
        level - the level of the htree
    
    Pseudocode:
        Simply draws the right half of the tree, then turns to the other side,
        and draws the left half of the tree.
    '''
    
    half_tree(length,level)
    turtle.right(180)
    half_tree(length,level)


def single_side(length, level):
    ''' Draws a single side of the koch snowflake.

    Parameters:
        length - the length of each side of the snowflake
        level - the level of the koch snowflake
    
    Pseudocode:
        By looking at the given examples of snowflake in different levels, we
        found the following pattern: 
        1: turtle goes forward by the same amount before it makes a turn
        2: the amount it goes = length / (3 ** level)
        This means we have to somehow divide the length by 3 for level amount of
        times.
        To do this, in the base case, instead of returning nothing, we return
        turtle.forward(length). By doing this, we can get the correct amount of
        distance in the recursive case by using parameters:length/3 and level-1.
        Then for the recursive case, we just need to let the turtle turns into
        correct direction after each time after it moves forward.
    '''
    
    if level == 0:
        return turtle.forward(length)
    
    else:
        single_side(length/3, level-1)
        turtle.left(60)
        single_side(length/3, level-1)
        turtle.right(120)
        single_side(length/3, level-1)
        turtle.left(60)
        single_side(length/3, level-1)
        
def koch_snowflake(length, level):
    ''' Draws the complete pattern of koch snowflake.

    Parameters:
        length - the length of each side of the snowflake
        level - the level of the koch snowflake
    
    Pseudocode:
        Since the complete snowflake is composed of three identical sides, we
        just need to turn the turtle into right direction after we finsh drawing
        a single side.
    '''
    single_side(length,level)
    turtle.right(120)
    single_side(length,level)
    turtle.right(120)
    single_side(length,level)
    turtle.right(120)


'''
Change the code below, as required, to run the program
'''
def main():
    """
    A wrapper function that calls the functions above
    """
    a = "abbbacaba"
    b = "a"
    recursive_delete(a,b)
    double_countdown(8)
    #single_side(90,3)
    koch_snowflake(90, 3)
    
    htree(100, 5)
    turtle.done()

'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 