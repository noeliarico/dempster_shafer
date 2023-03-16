import dempster_shafer as ds
import numpy as np

################################################################################
# Creation of frame of discernment with items of length = 1
################################################################################

# Using a lists and numpy arrays ###############################################

print("Creating frame of discernment for elements n, r, p")
fod1 = ds.FrameOfDiscernment(['n', 'r', 'p'])
fod1

print("Creating frame of discernment for elements a, b, c, d")
fod2 = ds.FrameOfDiscernment(["a", "b", "c", "d"])
fod2

fs1 = ds.FocalSet(fod2, np.array([.4, .3, .3]), np.array(["abc", "abdc", "a"]))
print(fs1)



# As Dictionary
fs1 = ds.FocalSet(fod, 
    {
        "abc": 0.4,
        "abdc": 0.3,
        "a": 0.3
    })
print(fs1)

fs2 = ds.FocalSet(fod, 
    {
        2: 0.4,
        3: 0.3,
        4: 0.3
    })
print(fs2)



################################################################################
# Creation of frame of discernment with items of length > 1
################################################################################

