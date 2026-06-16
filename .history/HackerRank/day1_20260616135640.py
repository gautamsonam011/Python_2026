# Given two strings, str1, and str2, where str1 contains exactly one character more than str2, 
# find the indices of the characters in str1 that can be removed to make str1 equal to str2. 
# Return the array of indices in increasing order. If it is not possible, return the array \[-1\]. 

# **Note:** Use 0-based indexing.

# **Example**

# str1 = "abdgggda"

# str2 = "abdggda"

# Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return \[3, 4, 5\].

str1 = "abdgggda"

str2 = "abdggda"

def getRemovableIndices(str1, str2):
    n, m = len(str1), len(str2)

    if n != m + 1:
        return [-1]

    result = []

    for i in range(n):
        if str1[:i] + str1[i + 1:] == str2:
            result.append(i)

    return result if result else [-1]

print(getRemovableIndices(str1, str2))