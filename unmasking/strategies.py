from unmasking.interfaces import UnmaskingStrategy

import numpy


class FeatureRemoval(UnmaskingStrategy):
    """
    Classic feature removal as suggested by Koppel et al.
    """

    def __init__(self, num_eliminate: int):
        """
        :param num_eliminate: number of features to eliminate per iteration.
        """
        super().__init__()
        self._num_eliminate = num_eliminate

    def transform(self, data: numpy.ndarray, coef: numpy.ndarray) -> numpy.ndarray:
        coef = numpy.absolute(coef)
        
        for i in range(0, self._num_eliminate):
            if data.shape[1] == 0:
                return data
            
            index = numpy.argmax(coef)
            coef  = numpy.delete(coef, index)
            data  = numpy.delete(data, index, 1)
        
        return data