.. dempster_shafer documentation master file, created by
   sphinx-quickstart on Mon May 10 15:04:58 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dempster_shafer's package documentation
===========================================

The aim of this package is to provide a tool for performing Dempster-Shafer
operations in large set of items by means of a native GPU implementation

.. toctree::
   :maxdepth: 2
   :caption: Contents:

items - elements in omega

The Dempster-Shafer theory of evidence provides an expressive framework for reasoning with uncertainty.  

It includes probability theory as a special case and is able to express imprecise probabilities. 

Given a \textit{frame of discernment} :math:`\Omega`, which is a set containing :math:`n` elements, 
basic probabilities are allocated to its subsets, instead of being allocated to single elements (on the contrary to what happens in the case of probability theory). 
The derived measures of Plausibility and Belief, which determine the probability interval assigned to a subset, 
are calculated from the relationships between that subset and the basic assignment of probabilities on all subsets. 

For any application of this theory, the need to deal with the power set :math:`2^\Omega`, i.e., the collection of all potential subsets of a discourse universe, poses significant problems in terms of scalability, being this a problem for the DST computation and consequently its use in real contexts. 



Belief function represents the degree of belief to which the evidence supports 
and plausibility refers to the degree of belief to which a set is feasible.

A function :math:`m:2^{\Omega}\longrightarrow [0, 1]` over :math:`\Omega` is called a *basic probability assignment* iff
:math:`m(\emptyset)=0 \;\;\; \textrm{and} \:\; \sum_{S \in 2^\Omega} m(S)=1`

Any :math:`S \in 2^\Omega$ is a \textit{focal element} iff $m(S)>0`. 

A *focal set* is the collection of focal elements :math:`F(\Omega)=\{S \subseteq \Omega | m(S)>0\} \subseteq 2^\Omega`.


The *Belief* of :math:`A \subseteq \Omega` induced by the basic probability assignment function :math:`m` is defined as

:math:`Bel(A)=\sum_{S\subseteq A} m(S)`

The *Plausibility* of :math:`A \subseteq \Omega` induced by the basic probability assignment function *m* is defined as

:math:`Pl(A)=\sum_{S \cap A \neq \emptyset} m(S)`


Let :math:`m_1` and :math:`m_2$` be two basic probability assignments, the *joint basic probability assignment*, i.e. the Dempster's combination rule (DCR), is computed as
:math:`m_{1,2}(A) = \frac{1}{1-Z} \sum\limits_{B \cap C = A} m_1(B) \cdot m_2(C)`
where
:math:`Z = \sum\limits_{B \cap C = \emptyset} m_1(B) \cdot m_2(C)`
is a measure of *conflict* between the two basic probability assignment sets. In addition, it is assumed :math:`m_{1,2}(\emptyset) = 0`.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Documentation for the Code
**************************

.. automodule:: dempster_shafer


Frame Of Discernment
====================

.. autoclass:: FrameOfDiscernment
   :members: __init__, is_subset, get_index, get_subset, print_all

Focal Set
=========

The set of focal sets must be associated with a Frame of Discernment.

The initialization can be done either using the literal names of the items or 
the indexes of the subset.

For example, given the focal set of items {a,b,c,d} which was initiallize as:

>>> fod = ds.FrameOfDiscernment(["a", "b", "c", "d"])

To create the focal set of elements {C, BC, AD} with basic probability assignments of 0.5, 0.4 and 0.1
it is necessary to execute:::

   fs1 = ds.FocalSet(fod, )

Another option is to use a dictionary::

   fs1 = ds.FocalSet(fod, 
      {
         "c": 0.5,
         "bc": 0.4,
         "ad": 0.1
      })

This can be also done using indexes for the dictionary::



.. autoclass:: FocalSet
   :members: __init__, __checkSubsets, 


Lattice
=======

The lattice objects allow operations over a frame of discernment. Each Lattice
must have associated the frame of discernment for which the computations are done.

In order to compute the belief and plausibility, it is necessary to associate 
a focal set to the lattice.

An example of workflow could be::

   import numpy as np
   import dempster_shafer as ds
   
   # Create a frame of discernment
   fod = ds.FrameOfDiscernment(['a', 'b', 'c', 'd'])

   # Focal elements and their associated basic probability assignment
   elems = np.array(['c', 'bc', 'ad'])
   bpas = np.array([.5, .4, .1])
   # Initialize the focal set
   fs = ds.FocalSet(fod, bpas, elemes)

   # Lattice to perform operations
   lat = ds.Lattice(fod, fs)

.. autoclass:: Lattice
   :members: __init__, bel, pl