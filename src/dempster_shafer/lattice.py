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
        
        
    def __repr__(self):
        return "Lattice for the items".format(self.items)
    
    def __str__(self):
        return "Lattice for the items".format(self.items)