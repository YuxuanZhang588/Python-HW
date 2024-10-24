
"""
Solutions to the programming problems from quiz #10.

Author: David Zhang
"""

import math

def radical_sum(num, level):
    """ Returns the value of the radical sum of num, nested to the given level.
    
    We assume that num >= 0 and level >= 0.
    
    Parameters:
        num - the integer whose radical sum we wish to compute.
        level - the number of levels of nesting in the radical sum.
        
    Returns:
        The value of sqrt(num + sqrt(num + sqrt(num + ...))), nested level
        times.
        
    Pseudocode:
        The base case is when the level is zero, it should return 0.0.
        The recursion case is when level is not zero. First reduce the level by
        one because we don't want infinite loops. Then the function should
        return the square root of the number plus radical_sum(num, level)
    """
    import math
    #base case: level = 0
    if level == 0:
        return 0.0
    else:
        level-=1
        return (num+radical_sum(num, level))**(0.5)


def simplify(phrase):
    """Returns a straightforward version of the input phrase.
    
    For example, 'the cat the dog worried' --> 'the dog that worried the cat'
    
    Parameters:
        phrase - a string containing a nested phrase.
        
    Returns:
        A string containing a more straightforward rewrite of the given
        phrase.
        
    Pseudocode:
        The base case is when the phrase only contain one subject, which only
        contains two element: "the" and the subject. So we just need to check
        if the second word in the phrase is the last word or not.
        In order to simplify the sentence, we need to work from the end to the
        begining. We first take the first subject, which is the first two words
        in the phrase, at the end of the simplified phrase. Then we put the last
        element in the original phrase, which is a verb, in front of the first
        subject, and then we put a "that" in front of the verb. We also need to
        create a new phrase which has the words that we already have in the
        simplified phrase deleted. Then we justkeep the loop running by adding
        simplify(newphrase) in front of everything. 
    """
    #base case: when
    if phrase.split()[1]==phrase.split()[-1]:
        return phrase
    
    else:
        that = "that"
        lst = phrase.split()
        sp = ' '
        newphrase = sp.join(lst[2:-1])
        phrase = (simplify(newphrase) + sp + that + sp + lst[-1] +
                  sp + lst[0] + sp + lst[1])
        return phrase
    
def main():
    """ Tester function. """
    print ()
    print ("Testing radical_sum")
    print (radical_sum(2, 2))   # 1.8477...
    print (radical_sum(2, 0))   # 0.0
    print (radical_sum(4, 5))   # 2.5607...   
    print (radical_sum(2, 20))  # 1.9999 .. (or 2.0)

    print ()
    print ("Testing simplify")
    print (simplify("the dog"))
    print (simplify("the roach the pirate killed"))
    print (simplify("the rat the cat the dog worried killed"))
    print (simplify("the rat the cat the dog the boy the girl saw owned " + 
                   "chased bit"))
    print ()
   
    
if __name__ == "__main__":
    main()
