"""
.. module:: fod
    :platform: Unix, Windows
    :synopsis: A useful module indeed.

.. moduleauthor:: Noelia Rico <noeliarico@uniovi.es>


"""

import numpy as np

class FrameOfDiscernment:
    """Frame of discernment for a set of items.
    
    This class allows to create a set of items to be used later with the 
    classes FocalSet and Lattice.
    
    """
    
    # if True, all the strings for identifying the elements have length=1       
    __length1 = True
    
    def __init__(self, items):
        """Crate a FrameOfDiscernment object for the set of items that is given 
        as paramenter.

        :param items: List containing the strings with the names of the items
            represented in the frame of discernment.
        :type items: list, np.array
        """
        
        self.items = items
        
    def get_index(self, subset):
        """Get the index of a subset 

        Given an interger number as parameter, return the subset of the frame 
        of discernment associated with that integer.
        
        If the elements of the frame of discernmnet have length one...

        >>> fod = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])
        >>> get_index('ad')
        9
        
        If at least one of the elements of the frame of discernmnet have 
        length greater one...
        
        >>> fod = ds.FrameOfDiscernment(['item1', 'item2', 'item3'])
        >>> get_index('item1;item2')
        
        """
        
        if not type(subset) is str:
            raise ValueError("ValueError: subset must be an string")
        
        # check if all the elements of the subset are item of the FoD
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
        """Returns the subset corresponding to an index  given as paramenter

        :param index: Index of the subset that is going to be retrieved
        :type index: int
        :return: Subset corresponding to the index given as parameter
        :rtype: string
        """
            
        # convert number into string of the binary representation
        binary = bin(index) 
        binary = binary[2:] # remove first two characters which are 0b
        binary = binary.zfill(len(self.items)) # pad with zeros
        binary = list(binary) # each element to a position of an array
        binary = [int(x) for x in binary] # as integers
        binary = list(np.extract(binary, self.items)) # take the names
        binary = ''.join(binary) # create the string representation
        return(binary)
    
        # TODO for longer elements
    
    def is_subset(self, subset):
        """Check if subset is subset of the elements in the frame of discernment

        :param subset: [description]
        :type subset: [type]
        """
        
        if self.__length1:
            # check for all the items if they exist
            for i in range(len(self.items)):
                # find each element as a subset of the set of items
                # function find returns -1 when the number 
                if subset.find(self.items[i]) == -1:
                    return False
            return True
        
        # at least one of the strings representing the items is longer 
        # than one and therefore a separator is needed
        else:
            return True
            
        
    def print_all(self):
        """Print all the subsets of the frame of discernment as well as their
        associated integer index. 
        """
        for i in range(2**len(self.items)):
            print("{} \t - \t {}".format(i, self.get_subset(i)))
    
        
    def __str__(self):
        return "Frame of discernment for the set of items".format(self.items)