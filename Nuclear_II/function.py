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



f = open('massround.mas20.txt','r')
out = f.readlines() 

for line in out:
    line