import numpy as np
from numba import cuda
    
class Prueba:
    
    def __init__(self,n):
        self.n = n
        self.an_array = np.zeros(self.n)
        self.numbers = np.array([4,2,6,5])
        
    @cuda.jit
    def __add1(an_array):
        # Thread id in a 1D block
        pos = cuda.grid(1)
        if pos < an_array.size:  # Check array boundaries
            an_array[pos] += 1
            
    def add1(self):
        threadsperblock = 16
        blockspergrid = 16
        d_an_array = cuda.to_device(self.an_array)
        self.__add1[blockspergrid, threadsperblock](d_an_array)
        d_an_array.copy_to_host(self.an_array)
        return 0
        
    