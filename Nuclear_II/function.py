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


def correct_string(line: str, A_before: int) -> (list,int):
    """""
    
    Turns one line of the string into a list with values for all these 'N', 'Z', 'A', 'El', 'Orig', 'Mass Excess (keV)', 'ME Unc',
       'Binding Energy/A (keV)', 'BE/A Unc', 'Beta-decay Type',
       'Beta-decay Energy (keV)', 'BE Unc', 'N Protons',
       'Atomic Mass (micro-u)', 'AM Unc'
       
    """""
    
    N = int(line[2:9].strip())
    Z = int(line[10:14].strip())
    
    A_test = line[15:19].strip()
    if A_test ==  "":
        A = A_before
    else:
        A = int(A_test)
    
    El = line[20:22].strip()
    Orig = line[23:27].strip()
    mass_excess = line[28:41].strip()  # missing convertion for # is str for now
    mass_excess_unc = line[42:52].strip() # missing convertion for # is str for now
    b_energya = line[53:63].strip() # missing convertion for # is str for now
    b_energya_unc = line[63:72].strip() # missing convertion for # is str for now
    b_type = line[72:75].strip()
    b_energy = line[75:86].strip() # missing convertion for # and * is str for now
    b_energy_unc = line[87:95].strip() # missing convertion for # and * is str for now
    n_protons = int(line[96:99].strip())
    a_mass = line[99:112].strip() # missing convertion for # and * is str for now
    am_unc = line[112:].strip() # missing convertion for # and * is str for now
    
    output_values = [
        N, Z, A, El, Orig, mass_excess, mass_excess_unc, b_energya, b_energya_unc,
        b_type, b_energy, b_energy_unc, n_protons, a_mass, am_unc
    ]
    return output_values, A

# def Qa (Ta,A,Z): #A,Z til datterkerne, samt bruges den udgave hvor bindingsenergien for alpha partiklen
#     return Ta*(binding_E(A,Z)+(2*mp+2*me+2*mn)-28.296)/binding_E(A,Z)

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
    
    return mother_B-daughter_B-heliumm



# f = open('massround.mas20.txt','r')
# out = f.readlines() 
# line = out[33]
# elements = []
# for i in range(len(line)):
#     # line = out[34]
#     # print(line[i])
#     # print(line[i])
#     if line[i]!=' ':
#         start = 1
#         # print(line[i])
#         if line[i+start]== ' ':
#             # print('mellemrum')
#             elements.append(line[i])
#         elif line[i+start]!=' ':
#             # print('2 element')
#             while line[i+start] !=' ':
#                 start+=1
#                 print(line[i+start])
#                 # print('start',start)
#                 if line[i+start] == ' ':
#                     stop = start
#                     elements.append(line[i:i+stop])
#                     i+=stop
#                     print('stop',stop)
#                     break
                
#             # if line[i]:
                
#             # print(stop)
#             elements.append(line[i+stop])

# line = out[34]  # Assuming you have a list named out, and you want to extract a specific line from it
# def correct_line_to_str_array(line):
#     elements = []
#     i = 0
#     while i < len(line):
#         if line[i] != ' ':
#             start = 1
#             if i + start < len(line) and line[i + start] == ' ':
#                 elements.append(line[i])
#             elif i + start < len(line) and line[i + start] != ' ':
#                 while i + start < len(line) and line[i + start] != ' ':
#                     start += 1
#                 stop = start
#                 elements.append(line[i:i + stop])
#                 i += stop
#         i += 1
#     elements[-1]=elements[-1].replace('\n','')
    
#     return elements

# lines = out[34:60]
# elements_test = [correct_line_to_str_array(line) for line in lines]

# for i in range(len(lines)):
#     if len(elements_test[i])==15:
#         A = elements_test[i][3]
#     if (len(elements_test[i])!=15 and elements_test[i][0]!='0'):
#         elements_test[i].insert(0,'0')
#         elements_test[i].insert(3,A)
#     # print(elements_test[i][2]=='Li' or 'H')
#     if elements_test[i][2] == 'Li' or elements_test[i][2] == 'H':
#         elements_test[i].insert(0,'0')
#         elements_test[i].insert(3,A)
#     print(elements_test[i])
    
 

