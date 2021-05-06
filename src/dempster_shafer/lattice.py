import numpy as np

def the_lattice():
    print("This is the lattice")
    
class Lattice:
    
    def __init__(self, items):
        self.items = items
        print("Lattice created for {}".format(items))
        
    def get_index(self, subset):
        
        if not type(subset) is str:
            raise ValueError("ValueError: subset must be an string")
        
        # check if all the elements of the subset are 
        binary_repr = ''
        for i in range(len(self.items)):
            if subset.find(self.items[i]) == -1:
                binary_repr+='0'
            else:
                binary_repr+='1'
                
        return(int(binary_repr, base=2))
        
        # TODO: check the values are unique
        # TODO: check that all the values are in the set of items
        # TODO: What happens is items have length greater than one?
        
    def get_subset(self, index):
            
        # convert number into string of the binary representation
        binary = bin(index) 
        binary = binary[2:] # remove first two characters which are 0b
        binary = binary.zfill(len(self.items)) # pad with zeros
        binary = list(binary) # each element to a position of an array
        binary = [int(x) for x in binary] # as integers
        binary = list(np.extract(binary, self.items))
        binary = ''.join(binary)
        return(binary)
        
    def __repr__(self):
        return "Lattice for the items".format(self.items)
    
    def __str__(self):
        return "Lattice for the items".format(self.items)