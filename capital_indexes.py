# The function takes a single parameter, which is a string. 
# Function returns a list of all indices in the string that have capital letters.

# E.g, paremeter "HeLlO", should return [0, 2, 4]

def capital_indexes(string): 
    indices =  [x for x, index in enumerate([ i.isupper() for i in list(string) ]) if index != False]
    return indices
 
print(capital_indexes("HeLlO"))