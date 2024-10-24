
"""
Solutions to the programming problems from quiz #8.

Author: David Zhang
"""

def scrabble_score_file(filename):
    """Returns the average Scrabble score of the words in a given file

    This function opens the supplied file and computes the average
    Scrabble score of every word in the file. A "word" is defined to
    be a non-empty sequence of characters that contains no spaces.
    When scoring words, only lower-case letters of the alphabet are
    scored; all other characters receive a score of 0. If the given
    file does not exist or cannot be opened, then a value of -1.0 is
    returned.

    Args:
        filename - a string containing the name of the file to be scored

    Returns:
        The average Scrabble score of all the words in the file
        
    Pseudocode:
        First, I open the file as in_file and read it as text, which turns the
        context into a string. Then I use for-loop to iterate through each
        letters in the string, and see if it is a lower-case letter. If so, add
        the score the total score of the file. Next, I split the string into
        seperate words using xx.split(), which gives me the number of words by
        using len(xx). Now we have the total score and the number of words.
        Average score = tatal score / number of words.
    """
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, 
                   "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                   "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                   "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                   "y": 4, "z": 10}
    try:
        with open(filename, "r") as in_file:
            text = in_file.read()
        
        total_score = 0
        for i in text:
            if i in TILE_SCORES:
                total_score += TILE_SCORES[i]

        words = text.split()
        num_words = len(words)
        average_score = total_score/num_words
        return average_score
    
    except FileNotFoundError:
        return -1.0
    
    
    
    # COMPLETE ME!
    

def compute_mode(scores):
    """ Returns the mode(s) of the supplied data.
    
    In case the mode is not unique, then the list of modes returned is in
    ascending order.
    
    Parameters:
        scores - a list of integers denoting the data whose mode we wish to
                 compute.
                 
    Returns:
        A list of integers denoting the mode(s) of the data (sorted in 
        ascending order).
        
    Pseudocode:
        I created a dictionary for the freqency of each score. I use for-loop to
        run through the given list of scores. If the score does exist in the
        dictionary, its frequncy increase by 1. If not, we add that score to the
        key, and assign it with value 1 since it appeared once. Next, I turned
        both the keys and the values of the dictionary into lists. I find the
        maximum frequency by using max(list). Then I iterate through the whole
        frequency list to find the score that has the maximum frequency, and I
        append that score to the mode list. 
    """
    mode_list = []
    scores_dict = {}
    for score in scores:
        if score not in scores_dict:
            scores_dict[score] = 1
        else:
            scores_dict[score] += 1
    list_freq = list(scores_dict.values())
    list_scores = list(scores_dict.keys())
    max_freq = max(list_freq)
    
    for i in range(len(list_freq)):
        if list_freq[i] == max_freq:
            mode_list.append(list_scores[i])
    mode_list.sort()
    return mode_list
    
    # COMPLETE ME!


def main():
    """ Tester function """
    # Testing scrabble_score_file
    print
    print ("Testing scrabble_score_file")
    print (scrabble_score_file("hello.txt")) # should print 4.0
    print (scrabble_score_file("one-word.txt")) # should print 5.0
    print (scrabble_score_file("non-existent-file")) # should print -1.0 
    print (scrabble_score_file("moby-dick.txt")) # should print 7.4415...
    
    # Testing compute_mode
    print ()
    print ("Testing compute_mode")
    print (compute_mode([65, 70, 88, 70]))
    print (compute_mode([88, 70, 65, 70, 88]))
    print (compute_mode([92, 56, 14, 73, 22, 38, 93, 45, 55]))
    # Feel free to add more test cases here

    
if __name__ == "__main__":
    main()
