"""
.. module:: fod
    :platform: Unix, Windows
    :synopsis: A useful module indeed.

.. moduleauthor:: Noelia Rico <noeliarico@uniovi.es>


"""

class FrameOfDiscernment:
    """We use this as a public class example class.

    You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.

    .. note::

       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

    """
    
    # all the strings for identifying the elements have length=1       
    __length1 = True
    
    def __init__(self, items):
        """A really simple class.

        Args:
            foo (str): We all know what foo does.

        Kwargs:
            bar (str): Really, same as foo.

        """
        
        self.items = items
        print("Lattice created for {}".format(items))
        
    def get_index(self, subset):
        """Get the index of a subset 

        Given an interger number

        >>> get_index('abdc')
        30

        In the elements of the frame of discernmnet have length one
        
        If the elements of the frame of discernmnet have length one

        """
        
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