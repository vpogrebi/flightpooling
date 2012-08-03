'''
Created on Aug 2, 2012

@author: valeriy
'''
import math

def compute( data = None ):
    """
    Compute average and standard deviation of the list
    
    @param data: LIST
    
    "doctest":
    >>> compute() == {'avg': None, 'std': None}
    True
    >>> compute([]) == {'avg': None, 'std': None}
    True
    >>> compute([1, 2, 3]) == {'avg': 2, 'std': 1}
    True
    """
    res = {'avg': None, 'std': None};
    if isinstance( data, list ):
        size = len( data )
        if size > 0:
            mean = sum( data ) / size

            variance = sum( ( ( num - mean ) ** 2 for num in data ) ) / ( size - 1 )
            std = math.sqrt( variance )

            res['avg'] = mean
            res['std'] = std

    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
