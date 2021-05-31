class FocalSet:
    """Class for representing the focal sets associated to a Frame of Discerment
    """

    def __init__(self, fod, bpa, fe = None):
        """Focal set class

        :param fod: FrameOfDiscernment for which the focal set is defined
        :type fod: FrameOfDiscernment
        :param bpa: dictionary associating subset
        :type bpa: dict, np.array
        """     
        
        if fod == None:
            raise ValueError("The focal set must be associated with a frame of discernment.")
        if len(fod) != len(bpa):
            raise ValueError("There must be exactly one bpa value to each focal element")
        self.fod = fod
        self.bpa = bpa
        #TODO if bpa does not add to 1
        self.fod = fod
        
    def __checkSubsets(self):
        """Check that all the subsets belong to the FrameOfDiscernment.
        
        This method should not be used by the user. It is used internally
        when the Focal set is initiallized and ensures that every element
        of the focal set is a subset of the items in the frame of discernment.
        """
        
    def __str__(self):
        return "Items {} \n Focal set {} \n BPAa {} \n".format(self.fod.items, self.fs. self.bpa)