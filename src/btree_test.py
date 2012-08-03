'''
Created on Aug 2, 2012

@author: valeriy
'''
class Node:
    def __init__( self, data = None ):
        self.left = None
        self.right = None
        self.data = data

class BTree:
    def __init__( self, root = None ):
        """Constructor. Returns a tree if <root> is provided, 
        otherwise - initializes new tree
        
        @param root: Root node of a tree (@type root: Node)
        """
        if root:
            self.root = root
        else:
            self.root = Node()

    def insert( self, data ):
        """
        Insert <data> into a BTree
        @param data: data to be inserted
        """
        if not self.root.data:
            self.root.data = data
        else:
            if data < self.root.data:
                if not self.root.left:
                    self.root.left = Node( data )
                else:
                    tree = BTree( self.root.left )
                    tree.insert( data )
            elif data > self.root.data:
                if not self.root.right:
                    self.root.right = Node( data )
                else:
                    tree = BTree( self.root.right )
                    tree.insert( data )


    def preOrder( self, node ):
        """
        Print <node.data>, then traverse left and right sub-trees
        @param node: tree node (@type node: Node)
        """
        if node:
            if node.data:
                print node.data,
                self.preOrder( node.left )
                self.preOrder( node.right )


def createTree( data = [] ):
    if not isinstance( data, list ):
        raise RuntimeError, "<data> must be of list type"

    tree = BTree()
    for item in data:
        tree.insert( item )

    return tree

def test():
    """
    >>> tree = createTree()
    >>> tree.preOrder(tree.root)
    >>> data = [5, 2, 7, -1, 9, 124, -56, 35]
    >>> tree = createTree(data)
    >>> tree.preOrder(tree.root)
    5 2 -1 -56 7 9 124 35
    >>> data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    >>> tree = createTree(data)
    >>> tree.preOrder(tree.root)
    one four five two three six seven
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
