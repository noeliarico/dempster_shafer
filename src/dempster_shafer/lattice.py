import numpy as np
    
class Lattice:
    
    def __init__(self, fod, fs = None):
        """Lattice
        
        The lattice has a frame of discernment associated

        :param lattice: [description]
        :type lattice: [type]
        """
        self.fod = fod
        
        # TODO check that ds is associated with the same fod object
        self.fs = fs
        
        print("Lattice created for the frame of discerment {}".format(fod.items))
        
    def bel(self, element='all'):
        """Compute the belief using the set of focal elements associated with 
        the lattice.

        :return: The belief
        :rtype: np.array
        """
        
        if self.fs == None:
            raise ValueError("A focal set must be added to the latice before computing the belief.")
        
        if self.b != None:
            return self.b
        else:
            # compute the belief
            return self.b
        
        # TODO check if element if a string or a index
        # if it is a index (int) then it is necessary to check that the value
        # is lower then the number of subsets for n elements (2**n)
        # and retrieve the value for the array
        # if the element is a string...
        # if it is all, as default, return all the beliefs
        # if it is positive, return the ones that have a value greater than 0
        # if it is any other value, ensure that it is a subset
    
    def pl(self, element='all'):
        """Compute the plausability using the set of focal elements associated
        with the lattice.

        :return: [description]
        :rtype: [type]
        """
        
        if self.b != None:
            # sing the property Pl(A) = 1 - ~Bel(A)
            return np.flip(self.b)
        else:
            self.bel()
            
        return(0)
    
    def __str__(self):
        return "Lattice for the frame of discerment".format(self.lattice.items)