# Dempster shafer theory

Python package that contains functions related to the Dempster-Shafer theory. Find all the information about this package in:

https://pypi.org/project/dempster-shafer/

# Quick start

```
!pip install dempster_shafer
import dempster_shafer as ds

# Create a Frame of Discerment for the items a, b, c, d using a list
fod1 = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])

# Create focal set for the frame of discernment
fs1 = ds.FocalSet(fod1, 
    {
        "abc": 0.4,
        "abdc": 0.3,
        "a": 0.3
    })

# Create lattice
lat = ds.Lattice(fod1, fs1)
# Compute the plausibility
lat.pl()
# Compute the belief
lat.bel()

```


