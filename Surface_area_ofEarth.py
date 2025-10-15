import numpy as np

def surface_area(pi_approx):
    a = 6378.137
    c = 6356.752314245
    
    e_squared = 1 - (c**2/a**2)
    
    S_obl = 2 * pi_approx * a**2 *(1 + (1 - e_squared) / np.sqrt(e_squared) * np.arctanh(np.sqrt(e_squared))) 
    
    return S_obl


print(surface_area(np.pi))  

    
    
