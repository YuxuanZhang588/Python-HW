
"""
Solutions to the programming problems from quiz #3.

Author: David Zhang
"""

import turtle

def print_multiplication_table():
    """
    Prints out the multiplication table for 13, up to 13 x 20.
    """    
    # COMPLETE ME!
    for i in range(1, 21):
        product = 13 * i
        print("13 times", i, "=", product)

def steer_turtle():
    """
    Utilizes user-input directions to sketch a figure.
    """
    # The following lines prompt the user to enter a list of step sizes and
    # a list of angles to turn by, storing the results in variables named
    # steps and angles respectively. You should not modify these lines.
    steps = eval(input("Enter the step sizes to take (as a list): "))
    angles = eval(input("Enter the angles to turn by (as a list): "))
    
    # YOUR CODE GOES HERE
    for i in range(len(steps)):
        turtle.forward(steps[i])
        turtle.right(angles[i])
        
    turtle.done()
    
    
def shuffle():
    """
    Performs a perfect shuffle of a user-supplied list.
    """
    # Prompts the user to enter a list, storing the result in deck. You may
    # assume that the list will be of even length.
    deck = eval(input("Enter list: "))
    deck1 = []
    deck2 = []
    new_deck = []
    for i in range(int(len(deck) / 2)):
        deck1.append(deck[i])
    
    for i in range(int(len(deck) / 2), len(deck)):
        deck2.append(deck[i])
    
    for i in range(len(deck1)):
        new_deck.append(deck1[i])
        new_deck.append(deck2[i])
        
    print(new_deck)
    # COMPLETE ME!
    
'''
Note: Uncomment the following function calls as you write your code
'''       

def main():
    print_multiplication_table()
    steer_turtle()
    shuffle()

'''
Note: Do not change/remove the following code!
''' 

if __name__ == "__main__":
    main()   