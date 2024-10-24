"""
Solutions to the programming problems from quiz #6.

Programmer: David Zhang

"""

def simon_says(instructions):
    """
    Returns the instructions that would be obeyed in a game of Simon Says.
    
    Parameters:
        instructions - a list of strings, where each element is an instruction
                       issued by Simon.
                       
    Returns:
        A list of strings, containing the instructions that were obeyed.
        
    Pseudocode:
        I split the phrase by the space between each word. Then I use for-loop
        to check if the first two elements are "Simon" and "says"
        If true, I append the rest of the sentence into my list.
        
    """
    obey = []
    for phrase in instructions:
        word = phrase.split(" ")
        if word[0] == "Simon":
            if word[1] == "says":
                word2 = phrase.split("Simon says ")
                obey.append(word2[1])
           
    return obey
        
        
        
    # COMPLETE ME!

def min_tiles_to_change(room):
    """
    Returns the minimal number of tiles that need to be changed to make the
    given room as colorful as possible.
    
    The goal is to achieve a tile configuration where no two adjacent tiles are
    the same color.
    
    Parameters:
        room - a string containing the colors of the tiles in the room. The i^th
               character of room (one of 'R', 'G', 'B', or 'Y') is the color of
               the i^th tile.
               
    Returns:
        The minimum number of tiles that need to be changed so that no two
        neighboring tiles are the same color.
        
    Pseudocode:
        I found that the minimum number of tiles needs to change is related
        to the number of consecutive same colored tiles. For example, if there
        are five red tiles placed together: "RRRRR", then the minimum number of
        tiles need to be changed is int(5/2). Based on this, I use for-loop to
        count the number of tiles that have the same number placed together and
        add these number in a list. Then I divide them by two and round them down.
        Then I add them together, which gives me the nimimum number of tiles that
        needs to be changed.
        
    """
    
        
    # COMPLETE ME!
    lst = list(room)
    same = []
    count = 0
    num_change = 0
    lst_num = []
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            count+=1
        else:
            count+=1
            lst_num.append(count)
            count=0
    count += 1
    lst_num.append(count)
    for i in lst_num:
        num_change += int(i/2)
    return num_change

def main():
    """ Tester function. """
    # Test cases for Simon Says
    print ("\nTesting Simon Says")
    obeyed = simon_says(["Simon says smile", "Clap your hands",
                         "Simon says jump", "Nod your head"])
    print ("Test case 1:", obeyed)

    obeyed = simon_says(["simon says wave", "Simon say jump",
                         "Simon says twist and shout"])
    print ("Test case 2:", obeyed)
    
    obeyed = simon_says(["simon says wave", "simon says jump", 
                         "simon says clap"])
    print ("Test case 3:", obeyed)
    
    obeyed = simon_says(["Jump", "Simon says wave"])
    print ("Test case 4:", obeyed)
    print ()
    
    # Test cases for Colorful Tiles
    print ("Testing Colorful Tiles")
    tiles = min_tiles_to_change("RRRRRR")
    print ("Test case 1:", tiles)
    
    tiles = min_tiles_to_change("BBBYYYYYY")
    print ("Test case 2:", tiles)
    
    tiles = min_tiles_to_change("BRYGYBGRYR")
    print ("Test case 3:", tiles)
    print ()
    
    
if __name__ == "__main__":
    main()
