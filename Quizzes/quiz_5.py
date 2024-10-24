
"""
Solutions to the programming problems from quiz #5.

Author: David Zhang
"""

def print_latin_square():
    """
    Prints a Latin Square of the specified order.
    """
    order = int(input("Enter the order of the Latin Square: "))
    for i in range(order):
        for j in range (order):
            print((i+j)%order, end=' ')
        print()
        
    
    # COMPLETE ME!
    

def count_visible():
    """
    Computes the number of visible trophies on a shelf, given their heights
    in order.
    """
    heights = eval(input("Enter trophy heights: "))
    count = 0
    previous_number = heights[0]
    for i in range(1,len(heights)):
        if previous_number < heights[i]:
            count += 1
            previous_number = heights[i]
    count += 1
            
    print("Trophies visible:", count)
    
    # COMPLETE ME!
    

def main():
    ''' Wrapper function to call your functions '''
    print_latin_square()
    count_visible()
    
'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 