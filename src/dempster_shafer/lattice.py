import numpy as np
from numba import cuda
from numba import jit
import math
from .fod import FrameOfDiscernment
from .fs import FocalSet
    
class Lattice:
    
    def __init__(self, fod, fs = None):
        """Lattice
        
        The lattice has a frame of discernment associated

        :param fod: Frame of discernment associated with the lattice
        :type fod: FrameOfDiscernment
        
        :param fod: Focal set associated with the lattice
        :type fod: FocalSet
        
        """
        
        # Associate frame of discernment
        if isinstance(fod, (FrameOfDiscernment)):
            self.fod = fod
        else:
            raise TypeError("fod must be a FrameOfDiscernment")
        
        # Associate focal set
        if isinstance(fs, (FocalSet)):
            # The focal set must refer to the same fod that the lattice
            if fs.fod is fod: 
                self.fs = fs
            else:
                raise ValueError('The focal set and this lattice must be associated with the same frame of discernment' )  
        else:
            self.fs = None
            
        # This is an array to store the belief
        self.b = None
    
    def add_focal_set(self, fs):
        """Associate a focal set with the latice

        :param fs: Focal set to associate with the lattice
        :type fs: FocalSet
        :raises ValueError: The focal set and this lattice must be associated with the same frame of discernment.
        :raises TypeError: fs must be a FocalSet object.
        """
        if isinstance(fs, (FocalSet)):
            # The focal set must refer to the same fod that the lattice
            if fs.fod is self.fod: 
                self.fs = fs
            else:
                raise ValueError('The focal set and this lattice must be associated with the same frame of discernment.' )  
        else:
            raise TypeError('fs must be a FocalSet object.')  
            
    def bel(self, element='all'):
        """Compute the belief using the set of focal elements associated with 
        the lattice.

        :param element: 'all' to return the belief of all the subsets or a list 
            with the indexes of the subset to get the belief. Defaults to 'all'
        :type element: str, optional
        :raises ValueError: A focal set must be added to the lattice before computing the belief.
        :raises ValueError: No GPU available.
        :return: Array with the belief of all the elements of the matrix
        :rtype: np.array
        """
        
        # A focal set is required
        if not isinstance(self.fs, (FocalSet)):
            raise ValueError("A focal set must be added to the lattice before computing the belief.")
        
        if cuda.is_available():
            if isinstance(self.b, (np.ndarray)):
                return self.b
            else:
                # Initialize the array to store the belief of each subset
                print(self.fod.n)
                self.b = np.zeros(2**self.fod.n)
                print(self.b.size)
                
                # Define the dimensions of the parallelization
                threadsperblock = 128 # TODO which one is the best to use?
                blockspergrid = math.ceil(self.b.size / threadsperblock)
                
                # Get the focal set as two diffent arrays
                elements, bpas = self.fs.as_arrays()
                
                # Copy to the GPU
                d_elements = cuda.to_device(elements)
                d_bpa = cuda.to_device(bpas)     
                d_b = cuda.to_device(self.b) # TODO is it better to initialize in gpu ? 
                
                self.__bel[blockspergrid, threadsperblock](d_elements, d_bpa, d_b)
                
                # # Get the results back
                d_b.copy_to_host(self.b)
                # TODO should I clean somehow the GPU?
                
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
        
        
    @cuda.jit
    def __bel(fs, bpa, be): #, pl):
    
        # iset = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
        iset = cuda.grid(1)
        nfocal = fs.shape[0]
        nnodes = be.shape[0]
        
        if iset < nnodes:
            be[iset] = 0 # gpu does not initialize to zeros so this is necessary
            # pl[iset] = 0 # gpu does not initialize to zeros so this is necessary  
            for k in range(nfocal):
                el = fs[k]
                if (iset & el) == el: # belief
                    be[iset] += bpa[k]
                # if (iset & el) > 0: # plausibility
                #    pl[iset] += bpa[k]
    
    
    def pl(self, element='all'):
        """Compute the plausability using the set of focal elements associated
        with the lattice.

        :return: [description]
        :rtype: [type]
        """
        
        # A list of indexes is given
        if isinstance(element, (list, np.ndarray)): 
            if isinstance(self.b, (np.ndarray)):
            # sing the property Pl(A) = 1 - ~Bel(A)
                p = 1 - np.flip(self.b)
                return p[element]
            else:
                self.bel()
                self.pl() # call recursively and go into isinstance
            
        # The plausibility of all the elemnts is required
        elif isinstance(element, (str)) and element=='all':
            if isinstance(self.b, (np.ndarray)):
            # sing the property Pl(A) = 1 - ~Bel(A)
                return 1 - np.flip(self.b)
            else:
                self.bel()
                self.pl() # call recursively and go into isinstance

        # Invalid format for the parameter element  
        else:
            raise ValueError("Intance must be a list of indexes or a 'all'")

            
        return(0)
    
    def combine(self, fs):
        """Combine the basic probability assigments of two focal sets

        :param fs: New focal set, with the focal elements and their corresponding
            basic probability assigments resulting from the combination of
            the two focals sets given to this function
        :type fs: FocalSet
        """
        
        if not isinstance(fs, (FocalSet)):
            raise ValueError("fs must be a FocalSet object.")
        elif self.fs.fod != fs.fod: 
            raise ValueError("The focal sets must refer to the same frame of discernment.")
        else:
            fs1, bpa1 = self.fs.fod.as_arrays()
            fs2, bpa2 = fs.fod.as_arrays()
            self.__combine(fs1, fs2, bpa1, bpa2)
            
            k = np.zeros(1, dtype=np.float32)

            # To store the results
            fs_out = np.zeros((fs1.size,fs2.size))
            bpa_out = np.zeros((fs1.size,fs2.size))
            bpa_final = np.zeros(2**self.fod.n)

            # Move the set of focal elements and bpa to the GPU
            d_fs1 = cuda.to_device(fs1)
            d_fs2 = cuda.to_device(fs2)
            d_bpa1 = cuda.to_device(bpa1)
            d_bpa2 = cuda.to_device(bpa2)
            d_k = cuda.to_device(k)
            d_fs_out = cuda.to_device(fs_out)
            d_bpa_out = cuda.to_device(bpa_out)
            d_bpa_final = cuda.to_device(bpa_final)

            # Is it better to move it or to allocate it in memory?
            # Allocate memory to store the results of belief and plausibility
            # d_fs_out = cuda.device_array((fs1.size,fs2.size), dtype=np.float32)

            threadsperblock = (16, 16)
            blockspergrid_x = math.ceil(fs_out.shape[0] / threadsperblock[0])
            blockspergrid_y = math.ceil(fs_out.shape[1] / threadsperblock[1])
            blockspergrid = (blockspergrid_x, blockspergrid_y)
            self.__combine1[blockspergrid, threadsperblock](d_fs1, d_fs2, d_bpa1, d_bpa2, d_fs_out, d_bpa_out, d_bpa_final, d_k)
            # cuda.synchronize()

            # Copy back to the gpu
            fs_out = d_fs_out.copy_to_host()
            bpa_out = d_bpa_out.copy_to_host()
            k = d_k.copy_to_host()
            
            
            bpa_final = d_bpa_final.copy_to_host()

            # final result needs to be divided
            print("Results after division")
            print(np.divide(bpa_final, 1-k))
            
            # Create a focal set
            comb_fs = FocalSet(self.fod, bpa_final, fs_out)

        
    @cuda.jit
    def __combine(fs1, fs2, bpa1, bpa2, fs_out, bpa_out, bpa_final, k): 

    # fs1 and fs2 are two sets of focal elements
    # bpa1 and bpa2 their corresponding basic probability assignments
    # fs_out is a matrix of dimension fs1.size x fs2.size to store the intersections
    # bpa_out is a matrix of the same dimension than fs_out that stores the mass of each focal element
        i, j = cuda.grid(2)

        if i < fs_out.shape[0] and j < fs_out.shape[1]:
            fs_out[i,j] = fs1[i] & fs2[j] # intersection of the focal elements
            bpa_out[i,j] = bpa1[i] * bpa2[j]
            if fs_out[i,j] == 0:
                cuda.atomic.add(bpa_final, 0, bpa_out[i,j])

        # at this point each element of the matrix has a focal element obtained from 
        # the intersection of two different focal elements of the two sets

        # synchornize the threads
        cuda.syncthreads()

        # summatory of the bpas of the focal elements which intersection result in the empty set
        # can this be done or results in oncurrency problem?
        if (i < fs_out.shape[0] and j < fs_out.shape[1]):
            if fs_out[i,j] != 0:
                cuda.atomic.add(bpa_final, fs_out[i,j], bpa_out[i,j]/(1-bpa_final[0]))

    def __str__(self):
        return "Lattice for the frame of discerment".format(self.lattice.items)