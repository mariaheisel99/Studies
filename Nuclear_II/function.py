import numpy as np
mn = 939.56542052
mp = 938.27208816
me = 0.51099895000


def binding_E(A,Z):
    """binding energy of nuclei from formel 5.2 in nuclei book

    Args:
        A (float): Atomic number
        Z (float): proton number

    Returns:
        float: _returns the binding energy in MeV_
    """
    bv, bs,bc, bsymm, bp = 15.2, 15.8, 0.686, 44.7, 5.0
    N = A-Z
    energy = bv*A-bs*A**(2/3)-bsymm*((N-Z)**2/(2*A))-bc*Z**2/A**(1/3)+bp*(((-1)**N)+((-1)**Z))*(1/np.sqrt(A))
    
    return energy


def Q_alpha(A,Z):
    """Alpha emission Q-balue

    Args:
        A (float): Atomic number
        Z (float): proton number

    Returns:
        float: Q-value for alpha emission i MeV, using 28.296MeV as experimental binding energy of 4He
    """
    mother_B = binding_E(A,Z)
    daughter_B = binding_E(A-4,Z-2)
    heliumm = 28.296
    
    return daughter_B+heliumm-mother_B


def correct_line_to_str_array(line):
    """
    Converts a string line into an array of individual elements.

    This function takes a string line as input and splits it into individual elements based on spaces. 
    It handles cases where multiple spaces separate elements and removes any trailing newline character.

    Args:
        line (str): A string representing a line of data.

    Returns:
        list: A list of individual elements extracted from the input line.
    """
    
    elements = []
    i = 0
    while i < len(line):
        if line[i] != ' ':
            start = 1
            if i + start < len(line) and line[i + start] == ' ':
                elements.append((line[i]))
            elif i + start < len(line) and line[i + start] != ' ':
                while i + start < len(line) and line[i + start] != ' ':
                    start += 1
                stop = start
                elements.append((line[i:i + stop]))
                i += stop
        i += 1
    elements[-1]=elements[-1].replace('\n','')
    
    return elements

def correct_missing_values_in_str(lines):
    """
    Corrects missing values and inconsistencies in the list of lines.

    This function processes a list of lines, each representing data, and corrects missing values and inconsistencies
    based on predefined rules. It utilizes the correct_line_to_str_array function to split each line into individual
    elements.

    Args:
        lines (list): A list of strings representing lines of data.

    Returns:
        list: A list of lists containing corrected elements for each line.
    """
    elements_test = [correct_line_to_str_array(line) for line in lines]

    for i in range(len(lines)):
        if len(elements_test[i])==15:
            A = elements_test[i][3]
        if (len(elements_test[i])!=15 and elements_test[i][0]!='0'):
            elements_test[i].insert(0,'0')
            A=elements_test[i-1][3]
            elements_test[i].insert(3,A)
            # print(elements_test[i][2]=='Li' or 'H')
        if elements_test[i][2] == 'Li' or elements_test[i][2] == 'H':
            elements_test[i].insert(0,'0')
            elements_test[i].insert(3,A)
    

        if len(elements_test[i])<16:
            if elements_test[i][5][0]!='-a':
                elements_test[i].insert(5,' ')
                
            elif elements_test[i][5][0]!='x':
                elements_test[i].insert(5,' ')
                
            elif elements_test[i][5][0]!='-n':
                elements_test[i].insert(5,' ')
            

        if elements_test[i][10]=='*':
            elements_test[i].insert(11,'NaN')
            elements_test[i].insert(12,'NaN')
        
        # first = float(elements_test[i][-3])
        # second = float(elements_test[i][-2])
        # elements_test[i].insert(14,first*1e7+second)
        # # print(elements_test[i])
        # print((elements_test[i]))
        
        
    return elements_test
