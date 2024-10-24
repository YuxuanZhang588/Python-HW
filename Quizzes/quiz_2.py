
"""
Solutions to the programming problems from quiz #2.

Author: David Zhang
"""

import math

def verify_ramanujan_theorem():
    """
    Verifies the validity of one of Ramanujan's theorems involving radicals.
    """
    left = (5**(1/4)+1)/(5**(1/4)-1)
    right = (1/2)*(3+5**(1/4)+math.sqrt(5)+125**(1/4))
    print("The value of the left-hand side of Ramanujan's theorem: %.15f" % left)
    print("The value of the right-hand side of Ramanujan's theorem: %.15f" % right)
    
    
    # COMPLETE ME!
    

def print_surfin_bird():
    """
    Prints out the lyrics to the song Surfin' Bird by The Trashmen.
    """
    print("A-well-a, everybody's heard about the bird")
    for i in range(8):
        print("A-well-a, bird, bird, bird, b-bird's the word")     
    print("Surfin' bird")
    for i in range(6):
        print("Papa-ooma-mow-mow, papa-ooma-mow-mow")
        print("Ooma-mow-mow, papa-ooma-mow-mow")
    # COMPLETE ME!
    
    
def compute_laundry_time():
    """
    Computes and prints out the minimum number of minutes required to 
    do a user-specified number of loads of laundry.
    
    Assumptions: There is only 1 washer and 1 dryer. Washing takes 25 minutes,
    drying takes 25 minutes, and folding takes 10 minutes.
    """
    # The following line prompts the user to enter a value for the number of
    # loads that need laundering, and stores the input as an integer in the 
    # variable named num_loads. You should not modify this line. Just use the 
    # variable num_loads in your solution below.
    num_loads = int(input("Enter the number of loads: "))
    num_minutes = 60+(num_loads-1)*25
    print('Minimum time required in minutes:', num_minutes)
    
    #COMPLETE ME!
    
'''
Note: Uncomment the following function calls as you write your code
'''

def main():
    verify_ramanujan_theorem()
    print_surfin_bird()
    compute_laundry_time()   


'''
Note: Do not change/remove the following code!
''' 
if __name__ == "__main__":
    main()
    