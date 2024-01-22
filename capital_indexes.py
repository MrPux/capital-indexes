# The function takes a single parameter, which is a string. 
# Function returns a list of all indices in the string that have capital letters.

# E.g, paremeter "HeLlO", should return [0, 2, 4]

def capital_indexes(string): 
    indices =  [x for x, index in enumerate([ i.isupper() for i in list(string) ]) if index != False]
    return indices
 
print(capital_indexes("HeLlO")) #It prints [0, 2, 4]

#------------------------------------------------ 

#The following function is a more shorter version that I coded that acccomplishes the same results 
def capital_indices(string):
    indices = [x for x, index in enumerate(list(string)) if index.isupper()]
    return indices
print(capital_indices("HeLlO")) #It prints [1, 2, 4]