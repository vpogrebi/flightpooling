'''
Created on Aug 2, 2012

@author: valeriy
'''
import random

def preservedList( f ):
    """Decorator that can be used to wrap any procedure that modifies original data (LIST).
    Requirement: procedure must take single argument - a LIST. 
    This decorator executes given procedure, but preserves original data LIST 
    """
    def wrapper( data ):
        """
        Quicksort using data comprehensions and randomized pivot
        
        @param data: Input data (@type data: LIST)
        
        "doctest": 
        >>> qsort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
        [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
        >>> qsort(["bob","alice","barry","zoe","charlotte","fred","marvin"])
        ['alice', 'barry', 'bob', 'charlotte', 'fred', 'marvin', 'zoe']
        """
        return f( data[:] )

    return wrapper

@preservedList
def qsort( data ):
    "Quicksort using data comprehensions and randomized pivot"
    if isinstance( data, list ):
        if data == []:
            return []
        else:
            pivot = data.pop( random.randrange( len( data ) ) )
            lesser = qsort( [ l for l in data if l < pivot ] )
            greater = qsort( [ l for l in data if l >= pivot ] )
            return lesser + [pivot] + greater

if __name__ == "__main__":
    import doctest
    doctest.testmod()
