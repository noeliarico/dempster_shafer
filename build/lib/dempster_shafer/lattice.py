import numpy as np
from numba import cuda
from numba import jit
    
class Lattice:
    
    def __init__(self, fod, fs = None):
        """Lattice
        
        The lattice has a frame of discernment associated

        :param lattice: [description]
        :type lattice: [type]
        """
        self.fod = fod
        
        # TODO check that ds is associated with the same fod object
        if fs != None:
            if fs.fod != fod:
                raise ValueError('The focal set and this lattice must be associated to the same the frame of discernment' )
            else:
                self.fs = fs
        else:
            self.fs = None
        # print("Lattice created for the frame of discerment {}".format(fod.items))
        
    def calculation(self):
        k = self.k
        return self.complicated([1,2,3],k)

    @staticmethod
    @jit(nopython=True)                             
    def complicated(x,k):                                  
        for a in x:
            b = a**2 + a**3 + k
            
    def bel(self, element='all'):
        """Compute the belief using the set of focal elements associated with 
        the lattice.

        :return: The belief
        :rtype: np.array
        """
        
        if self.fs == None:
            raise ValueError("A focal set must be added to the lattice before computing the belief.")
        
        if cuda.is_available():
            if self.b != None:
                return self.b
            else:
                # compute the belief
                return self.b
        else:
            raise ValueError("No GPU available.")
        
        # TODO check if element if a string or a index
        # if it is a index (int) then it is necessary to check that the value
        # is lower then the number of subsets for n elements (2**n)
        # and retrieve the value for the array
        # if the element is a string...
        # if it is all, as default, return all the beliefs
        # if it is positive, return the ones that have a value greater than 0
        # if it is any other value, ensure that it is a subset
        
        
#         @cuda.jit
# def alg1GPU(fs, bpa, be, pl):
  
#   iset = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
#   nfocal = fs.shape[0]
#   nnodes = be.shape[0]

#   if iset < nnodes:
#     be[iset] = 0 # gpu does not initialize to zeros so this is necessary
#     pl[iset] = 0 # gpu does not initialize to zeros so this is necessary

#     for k in range(nfocal):
#       el = fs[k]
#       if (iset & el) == el: # belief
#         be[iset] += bpa[k]
#       if (iset & el) > 0: # plausibility
#         pl[iset] += bpa[k]
    
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