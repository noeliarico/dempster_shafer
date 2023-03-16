# import the package
import dempster_shafer as ds
import numpy as np

################################################################################
# FRAME OF DISCERNMENT #########################################################
################################################################################

# Create a FrameOfDiscerment for the items a, b, c, d using a list
fod1 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])
# Create a FrameOfDiscernment with names larger than one charancter
fod2 = ds.FrameOfDiscernment(['item1', 'item2', 'item3'])

# Check if a string represents a subset of a FrameOfDiscerment
print("Is 'bda' subset of fod1?: {}".format(fod1.is_subset("bda")))
print("Is 'ecd' subset of fod1?: {}".format(fod1.is_subset("ecd")))

# Get the indexes of some subsets
print("The index of 'c' is: {}".format(fod1.get_index('c')))
print("The index of 'bc' is: {}".format(fod1.get_index('bc')))
print("The index of 'ad' is: {}".format(fod1.get_index('ad')))

################################################################################
# FOCAL SET ####################################################################
################################################################################

fes = np.array(['c', 'bc', 'ad'])
bpas = np.array([.5, .4, .1])



# fod1.print_all()
# fs1 = ds.FocalSet(fod1, 
#     {
#         "abc": 0.4,
#         "abdc": 0.3,
#         "a": 0.3
#     })
# #print(fs1)
# print(fod1.is_subset('abd'))
# print(fod1.is_subset('aed'))

fs1 = ds.FocalSet(fod1, bpas, fes)
print(fs1)

fes, bpas = fs1.as_arrays()
print(fes)
print(bpas)

fes_num = np.array([2, 6, 9])
fs2 = ds.FocalSet(fod1, bpas, fes_num)
print(fs2)

lat = ds.Lattice(fod1, fs2)
#print(lat.bel())
lat.b = np.array([0.,0.,0.5,0.5,0.,0.,0.9, 0.9, 0. , 0.1, 0.5, 0.6, 0.,0.1, 0.9, 1. ])
print(lat.pl())

# # fod2 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd', 'e', 'f'])
# # fod2.print_all()

# # # Create a Frame of Discerment for the items a, b, c, d using a numpy
# # import numpy as np
# # fod2 = ds.FrameOfDiscernment(np.array(['a', 'b', 'c', 'd']))

