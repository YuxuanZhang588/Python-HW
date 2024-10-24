
"""
Solutions to the programming problems from quiz #7.

Author: David Zhang
"""

def count_cheeseburgers(filename):
    """Returns the number of lines in the file that start with the word
    cheeseburger.

    Parameters:
        filename - the name of the file to be read (a string)

    Returns:
        The number of lines in the specified file that begin with the word
        cheeseburger.
        
    Pseudocode:
        First, I open the file as in_file and read the file as menu. Since I
        need to find out how many lines started with cheeseburger, I split the
        text by lines. Then in each line, I split the line into seperate words.
        Then I use if statement to check if the first word is "cheeseburger".
        If true, count plus one.
    """
    
    with open(filename, 'r') as in_file:
        menu = in_file.read()
        lines = menu.split("\n")
    count = 0
    for line in lines:
        if len(line) != 0:
            word = line.split()
            if word[0] == "cheeseburger":
                count += 1
    
    return count
    

def min_cost_palindrome(s, o_cost, x_cost):
    """Returns the minimum cost of transforming str into a palindrome

    This function accepts a string consisting of only xs, os and ?s and
    reports the minimum cost of transforming this string into a palindrome
    by replacing every occurrence of a ? with either an x or an o. If the
    input string cannot be transformed into a palindrome, then a value of
    -1 is returned.

    Args:
        s - the string whose transformation cost we are computing
        o_cost - the cost of replacing a ? with an o (an int)
        x_cost - the code of replacing a ? with an x (an int)

    Returns:
        The minimum cost of transforming the input string into a palindrome
        given o_cost and x_cost. If it is not possible to transform s into
        a palindrome, then a value of -1 is returned.
        
    Pseudocode:
        First, I use list() function to turn string into a list of characters.
        Then, I use for-loop to compare between the first and the last, the
        second and the second last, the third and the third last... characters
        of the list. There are two cases: The two are the same or not the same.
        If the two are the same and they are not "?"s, then nothing happens. If
        the two are both "?"s, then cost should choose the lower price
        and add it twice. If they are not the same: if both are not "?", then it
        is impossible to turn it into a palindrome. if one of them if "?", then
        cost will add the cost of changing it into the other character.
    """
    
    lst = list(s)
    cost = 0
    end_of_range = int(len(lst) / 2 + 1)
    
    for i in range(1,end_of_range):
        if lst[i-1] != lst[-i]:
            if lst[i-1] != "?" and lst[-i] != "?":
                cost = -1
            elif (lst[i-1] == "?" and lst[-i] != "?"):
                if lst[-i] == "x":
                    cost += x_cost
                else:
                    cost += o_cost
            elif (lst[-i] == "?" and lst[i-1] != "?"):
                if lst[i-1] == "x":
                    cost += x_cost
                else:
                    cost += o_cost
        elif lst[i-1] == "?" and lst[-i] == "?":
            if x_cost < o_cost:
                cost += 2 * x_cost
            else:
                cost += 2 * o_cost
    return cost
    

def main():
    """ Tester function """
    # Testing count_cheeseburgers
    # You might want to add more test cases to file1.txt
    print ()
    print ("Testing count_cheeseburgers")
    print (count_cheeseburgers('file1.txt'))
    
    # Testing min_cost_palindrome
    print ()
    print ("Testing min_cost_palindrome")
    print (min_cost_palindrome("oxo?xox?", 3, 5)) # should print 8
    print (min_cost_palindrome("x??x", 9, 4)) # should print 8
    print (min_cost_palindrome("ooooxxxx", 12, 34)) # should print -1
    print (min_cost_palindrome("oxoxooxxxxooxoxo", 7, 4)) # should print 0
    # Feel free to add more test cases here

    
if __name__ == "__main__":
    main()
