# import the package
import dempster_shafer as ds
import numpy as np

fes = np.array(['c', 'bc', 'ad', 'c'])
bpas = np.array([.5, .4, .1])
res = dict(zip(fes, bpas))
print(res)
c = np.unique(fes, return_counts=True)[1]
dup = np.any(c > 1)
print(dup)

# # Create a Frame of Discerment for the items a, b, c, d using a list
# fod1 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])
# print(fod1.get_index('ad'))
# #fod1.print_all()
# fs1 = ds.FocalSet(fod1, 
#     {
#         "abc": 0.4,
#         "abdc": 0.3,
#         "a": 0.3
#     })
# #print(fs1)
# print(fod1.is_subset('abd'))
# print(fod1.is_subset('aed'))

# lat = ds.Lattice(fod1, fs1)
# lat.bel()

# # fod2 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd', 'e', 'f'])
# # fod2.print_all()

# # # Create a Frame of Discerment for the items a, b, c, d using a numpy
# # import numpy as np
# # fod2 = ds.FrameOfDiscernment(np.array(['a', 'b', 'c', 'd']))

