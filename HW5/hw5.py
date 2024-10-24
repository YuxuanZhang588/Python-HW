
"""
This program contains two functions
1. collatz()
2. simulate_walk()

Author: Thatcher Craig  David Zhang
Hours spent: 2 hours

"""

def collatz():
    """
    This function prompts the user to enter an integer
    number n and generate the hailstone sequence associated
    with n.
    
    Returns: None
    """
    n = int(input("Please enter an integer (> 1): "))
    num_steps = 0
    while n > 1:
        if n%2 == 1:
            n = 3*n+1
            num_steps += 1
        else:
            n = n/2
            num_steps += 1
    print("Number of hailstone steps:", num_steps)
        

def simulate_walk(start, low, high):
    """
    A drunk man is wondering around trying to find the
    exist in a long corridor. This function simulates the
    process of this man wondering around the corridor.
    
    Parameters:
        first_param - the starting position of the drunk man
        secon_param - the lower bond of the corridor
        thrid_param - the upper bond of the corridor
    
    Returns
        It returns the number of steps it takes for the
        drunk man to exist the corridor.
    """
    import random
    pos = start
    steps = 0
    
    while pos > low and pos < high:
        
        print("|", end=' ')
        for i in range(pos-low):
            print(".", end=' ')
        print("S", end=' ')
        for i in range(high-pos):
            print(".", end=' ')
        print("|")
        
        left_right = random.randint(0,1)
        if left_right == 1:
            pos += 1
            steps += 1
            
        else:
            pos -= 1
            steps += 1
            
    print("|", end=' ')
    for i in range(pos-low):
        print(".", end=' ')
    print("S", end=' ')
    for i in range(high-pos):
        print(".", end=' ')
    print("|")
    
    return steps

    
    
def main():
    """
    A wrapper function that calls the functions above
    """
    
    collatz()
    steps = simulate_walk(int(input('start: ')),
                          int(input('low: ')),int(input('high: ')))
    
    

'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 
