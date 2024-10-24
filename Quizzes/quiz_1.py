
"""
Solutions to the programming problems from quiz #1.

Author: David Zhang
"""

def lorentz_factor():
    """
    Determines the Lorentz factor for an object given its speed as a fraction
    of the speed of light.
    """
    # The following line prompts the user to enter a value for the velocity of
    # the moving object, and stores the input as a float in the variable
    # named speed. You do not have to understand how it works (for now)
    # and you should not modify this line. Just use the variable speed in 
    # your solution below.
    speed = float(input("Enter object velocity (as a fraction of c): "))
    r = 1 / ((1 - speed ** 2) ** 0.5)
    print('Lorentz factor: %.11f' % r)
    # COMPLETE ME!
    # I saw the examples that the outputs are all rounded to the 11th. So I wrote '%.11f' %r.

def fight_song():
    """
    Prints out the lyrics to an admittedly uninspiring Wildcats fight song.
    """
    verse1()
    print()
    verse2()
    print()
    verse2()
    print()
    verse1()
    
def verse1():
    print('Go, team go!')
    print('We can do it.')

def verse2():
    print('Go, team go!')
    print('We can do it.')
    print("We're the 'cats,")
    print("We'll leave it at that.")
    print('Go, team go!')
    print('We can do it.')
    
'''
Do NOT change the code below
'''
def main():
    lorentz_factor()
    fight_song()
    
if __name__ == "__main__":
    main()
