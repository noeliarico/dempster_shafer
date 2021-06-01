# import the package
import dempster_shafer as ds
import numpy as np

fes = np.array(['c', 'bc', 'ad'])
bpas = np.array([.5, .4, .1])

# Create a Frame of Discerment for the items a, b, c, d using a list
fod1 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])
print(fod1.get_index('c'))
print(fod1.get_index('bc'))
print(fod1.get_index('ad'))
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

fes_num = np.array([2, 6, 9])
fs2 = ds.FocalSet(fod1, bpas, fes_num)
print(fs2)

lat = ds.Lattice(fod1, fs2)
lat.bel()

# # fod2 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd', 'e', 'f'])
# # fod2.print_all()

# # # Create a Frame of Discerment for the items a, b, c, d using a numpy
# # import numpy as np
# # fod2 = ds.FrameOfDiscernment(np.array(['a', 'b', 'c', 'd']))

