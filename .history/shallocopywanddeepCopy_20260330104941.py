# deep copy vs shallow copy 

# Shallow Copy:

# Shallow copy it does not create a new array in memory.
# This will create new array by referencing data and make a view.
# Any changes in both of them will reflect in the other one.

# Deep Copy:

# Independent and new copy of the main array. 
# Changes in any of them will not affect the other one. 

# example: deep copy vs shallow copy 

import numpy as np 

array_org = np.array([1, 2, 3, 4, 5])   # original array
shallow_copy = array_org.view()         #shallow copy
deep_copy = array_org.copy()            #deep copy

shallow_copy[0] = 10001
deep_copy[1] = 289

print("Original array", array_org)
print("Shallow copy", shallow_copy)
print("Deep copy", deep_copy)

