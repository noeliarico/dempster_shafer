# import the package
import dempster_shafer as ds

# Create a Frame of Discerment for the items a, b, c, d using a list
fod = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])

# Create a Frame of Discerment for the items a, b, c, d using a numpy
import numpy as np
fod = ds.FrameOfDiscernment(np.array(['a', 'b', 'c', 'd']))