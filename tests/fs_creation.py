import dempster_shafer as ds
import numpy as np

################################################################################
# Frame of discernments to use with the focal sets
################################################################################

print("Creating frame of discernment for elements a, b, c, d")
fod1 = ds.FrameOfDiscernment(["a", "b", "c", "d"])
fod1

# Using arrays or lists ########################################################

# List with strings
fs = ds.FocalSet(fod1, [.5, .4, .1], ["b", "bc", "ad"])
print(fs) # Example of the papers

# Array with strings
fs = ds.FocalSet(fod1, np.array([.4, .1, .15, .15, .2]), 
                        np.array(["abc", "abdc", "a", "bdc", "dca"]))
print(fs)


# Using dictionaries ###########################################################

fs = ds.FocalSet(fod1, # with strings
    {
        "abc": 0.4,
        "abdc": 0.3,
        "a": 0.3
    })
print(fs)

fs = ds.FocalSet(fod1, # with integers
    {
        2: 0.4,
        3: 0.3,
        4: 0.3
    })
print(fs)



################################################################################
# Creation of focal set from arrays
################################################################################


################################################################################
# Creation of focal set from dictionary
################################################################################

