class FocalSet:
    """Class for representing the focal sets associated to a Frame of Discerment
    """

    def __init__(self, fod, bpa):
        """Focal set class

        :param fod: FrameOfDiscernment for which the focal set is defined
        :type fod: FrameOfDiscernment
        :param bpa: dictionary associating subset
        :type bpa: dict
        """
        
        self.fod = fod
        
    def __checkSubsets(self):
        """Check that all the subsets belong to the FrameOfDiscernment
        """
        
    def __str__(self):
        return "Focal set defined for the items {}".format(self.fod.items)