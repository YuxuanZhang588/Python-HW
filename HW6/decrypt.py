"""
Program that cracks the Caesar cipher.

Author(s): Anh Hoang, David Yuxuan Zhang

Time Spent: 3h
            
"""
#Variables
ENGLISH_FREQ = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15,
                0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.09, 5.99, 6.33, 9.06,
                2.76, 0.98, 2.36, 0.15, 1.97, 0.06]
LC_CODE_POINT_LIM = 122
NUM_ALPHABET = 26
PERCENT = 100
LC_LOWER_BOUNDERY = 97
LC_UPPER_BOUNDERY = 123


def shift(text, amount):
    """    
    Description: 
    Take the encrypted file and shift it by an amount
    
    Parameters:
    text: the text that needs to be decrypted
    amount: the shifting amount (ranging from 1-26)
    
        
    Returns:
    text that has been shifted
    
    Pseudocode:
    First, we have the text in the form of a list (with just characters from
    the alphabet). Use for loop to iterate over every element in the list (every
    alphabetical character in the text). Use the if-else branch to test:
    -if the unicode of the character plus the shift amount exceed 122, which
    is the unicode of the final character z, then we shift the character by
    using the chr() and ord() function, with the unicode of the shifted
    character equal the original one plus the shifted amount minus 26 (we have
    to minus 26 so the unicode can go back to the range 97-122)
    -else we can just combine unicode of the original character
    with the shifted amount to get the shifted characters

    """
    for i in range(len(text)):
        if ord(text[i])+ amount > LC_CODE_POINT_LIM:
            text[i] = chr(ord(text[i]) + amount - NUM_ALPHABET)
        else:
            text[i] = chr(ord(text[i]) + amount)
    return text
    #Turn each character into an integer, then plus the shifting amount to it.
    #Because the integer will exceed the upper limit of the index of characters,
    #we subtract it with 26 to get the correct character.


def score(text):
    """
    Description: 
    Take the shifted text and calculate the score of the text
    to see if it is close to a english-like text
    
    Parameters:
    text: the text that has been shifted
        
    Returns:
    test score of the shifted text
    
    Pseudocode: First, we create the variable count which counts the number
    of each alphabetical characters and freq_list, which stores the frequency
    of each characters. We create a nested for-loop, the outer loop
    iterating over the unicode of the lower-case characters, and the inner loop
    iterating over each character in the text. By using the if statement, we are
    able to count the frequency of each character separately.
    Finally, we store the frequencies of each character into the freq_list.
    We calculate the score by dividing the frequency of each character in the
    shifted text, by the frequency of every character in the english-like text.
    Then we append the results to the list called list_difference. The final
    score is the average of the values in the list.
    
    
    """

    count = 0
    freq_list= []
    for c in range(LC_LOWER_BOUNDERY,LC_UPPER_BOUNDERY):
        for character in text:
            if character == chr(c):
                count += 1
        freq = (count/len(text)) * PERCENT
        freq_list.append(freq)
        count = 0
    #Generate a list of frequencies for the characters in the decoded text.
    difference = 0
    list_difference = []
    for i in range(NUM_ALPHABET):
        difference =  freq_list[i] / ENGLISH_FREQ[i]
        list_difference.append(difference)
        difference = 0
    test_score = sum(list_difference) / NUM_ALPHABET
    return test_score
    #Calculate the diffence ratio by divide the average freqency to the
    #frequency we got, and then calculate the average of the differences.

def crack_cipher(filename):
    """
    Description: 
    Takes a encrypted text, decrypte it by shifting all the letters by
    certain amount. 
    
    Parameters:
    filename: the encrypted file that needs to be decrypted
        
    Returns:
    the decrypted text
    the score of the encrypted file.
    
    Pseudocode:First we open and read the file. Then we create a list called
    text to store the text without punctuations and special characters. 
    We used the for-loop to try to shift the text by amount from 0 to 25.
    We record the score of each of the shifted text. Then we find the text with
    score that is closest to 1, which means the most English-like text. Then we
    create a new string called deciphered_text with the deciphered text and
    all the punctuations from the original text.
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = []
    with open(filename, 'r') as in_file:
        word_list = in_file.read()
        for char in word_list:
            if char in alphabet:
                text.append(char)
    original_text = text[:]
    #Remove the punctuations from the text
    
    scores = []
    for i in range(NUM_ALPHABET):   
        shifted_text = shift(text,i)
        final_score = abs(score(shifted_text)-1)
        scores.append(final_score)
        og_text = original_text[:]
        text = og_text  
    final_thing = min(scores)
    amount = scores.index(final_thing)
    deciphered_text =''  
    for character in word_list:
        if character in alphabet:
            if ord(character)+ amount > LC_CODE_POINT_LIM :
               deciphered_text += chr(ord(character)+amount-NUM_ALPHABET)
            else:
               deciphered_text += chr(ord(character)+amount)
        else:
            deciphered_text += character
   
     #Put the punctuations back into the text.   
    return deciphered_text
    
    

   
    

def main():
    """ Tester function """
    print (crack_cipher("cipher1.txt"))
    print (crack_cipher("cipher2.txt"))


if __name__ == "__main__":
    main()
