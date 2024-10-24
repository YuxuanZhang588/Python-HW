
"""
Measures centraility and find the most central individual of a given membership
dataset
Author: Anh Hoang, David Yuxuan Zhang
Time spent: 3 hours

"""

def find_most_central(text):
     
    """ Take the text and find the most central person in the dataset
    
    Parameters:
     text - the membership dataset
    
    Returns:
     Name of the most central person
      (in case of error, print 'error' and return an empty string)
    
    Pseudocode:
     The function opens the file as infile, then it turns the context in the
     list into a dictionary, with names for keys and numbers for values.
    
    """
    matrix_element = {} #A dictionary, keys are the names of the participants
                   #names of the orgnizations are not in the dictionary.
    lst_participant = []
    values = []
    try:
        with open (text, 'r') as infile:
            for line in infile:
                words= line.split(',')
                if words[0] != 'Name':
                    for num in words[1:]:
                        try:
                            values.append(int(num))
                        except:
                            values.append(0)
                    matrix_element[words[0]] = values
                    values = []
            result_matrix = matrix_multiplication(matrix_element)
            name_central = measuring_centrality(result_matrix, matrix_element)
            return name_central
                    
    except FileNotFoundError or IOError:
        print('Error')
        return ''
    
    #Matrix Multiplication
def matrix_multiplication(original_matrix):
    
     
    """ Transfrom the matrix into a nested list and calculate matrix
    matrix multiplication
    
    Parameters:
     original_matrix - a dictionary transfromed from the membership dataset
    
    Returns:
     the result of the multiplication in the form of a nested list
    
    Pseudocode:
     The function turns all values in the dictionary into a nested list, where
     each list in the nested list represent a row in the matrix. Then we used
     nested for-loop, to multiply each number with its corresponding number.
     Each time after we finished multiplying a row of numbers, we store the sum
     of the values into M_lines, and append that list of number into the
     resulting matrix M. This way, we don't need to reverse the matrix.
    
    """
    products = [] #A list for the products of the two numbers.
    matrix_lines = [] #A list for each row in the resulting matrix
    resulting_matrix = [] #A nested list represent the resulting matrix
    lst = list(original_matrix.values())

    for i in range(len(lst)):
        for e in range(len(lst)):
        #The coordinate for the first multiplier
            for k in range(len(lst[0])):
                products.append(lst[i][k]*lst[e][k])
            matrix_lines.append(sum(products))
            products = []
        resulting_matrix.append(matrix_lines)
        matrix_lines = []
    
    return resulting_matrix
    #Measuring Centrality
def measuring_centrality(matrix, original_matrix):
    
    """ Use the result of the multiplication to measure centrality    
    
    Parameters:
     matrix - result of the multiplication
     original matrix - a dictionary transfromed from the membership dataset
    
    Returns:
     name of the most central person
    
    Pseudocode:
     The function calculates the sum of each row of the resulting matrix. Then
     the function finds the largest sum, and returns the name corresponding to
     the row that has the largest sum.
    
    """
    
    
    lst_sums = []
    for lines in matrix:
        lst_sums.append(sum(lines))
    index_max = lst_sums.index(max(lst_sums))
    lst_names = list(original_matrix.keys())
    name = lst_names[index_max]
    
    return name
    
'''
Change the code below, as required, to run the program
'''
def main():
    """
    A wrapper function that calls the functions above
    """
    
    print(find_most_central('revolutionaries.txt'))


'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 