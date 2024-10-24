
"""
Solutions to the programming problems from quiz #4.

Programmer: David Zhang

"""

def approximate_pi():
    """
    Computes an approximation to pi using the Leibniz formula.
    """
    num_terms = int(input("How many terms would you like to use? "))
    list1 = []
    list3 = []
    for i in range(1, 2*num_terms-1, 4):
        list1.append(1/i)
        
    for i in range(3, 2*num_terms, 4):
        list3.append(1/i)
    
    answer = 4*(sum(list1) - sum(list3))
    
    print(answer)
    # COMPLETE ME!
    

def draw_staircase():
    """Prints a staircase composed of *'s (asterisks) with user-specified 
    dimensions.

    Here are a couple of examples:

    height = 5, width = 3
    * * *
    . . * * *
    . . . . * * *
    . . . . . . * * *
    . . . . . . . . * * *

    height = 1, width = 1
    *
    
    """
    height = int(input("Enter the height of the staircase: "))
    width = int(input("Enter the width of the staircase: "))
    

    for i in range(height):
        for j in range(i):
            for k in range(width-1):
                print(".", end=' ')
        for l in range(width):
            print("*", end=' ')
        print()


def main():
    ''' Wrapper function to call your functions '''
    approximate_pi()
    draw_staircase()
    
'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 