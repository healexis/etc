#!/usr/bin/python

class Tree( object ):
    def __init__( self, val, left=None, right=None ):
	self.val = val
	self.left = left
	self.right = right

    def __repr__( self ):
        return "( %s, %s, %s )" % ( repr( self.val ), repr( self.left ), repr( self.right ) )

    def __eq__( self, other ):
        return self.val == other.val and self.left == other.left and self.right == other.right

def listToTree( l ):
    if len( l ) == 0:
        return None
    elif len( l ) == 1:
        return Tree( l[ 0 ] )

    middle = len( l )//2
    left = l[ : middle ]
    right = l[ middle + 1 : ]
    return Tree( l[ middle ], left=listToTree( left ), right=listToTree( right ) )

if __name__ == "__main__":
    tests = []
    checks = []
    tests.append( range( 3 ) )
    checks.append( Tree( 1, Tree( 0 ), Tree( 2 ) ) )
    tests.append( range( 10 ) )
    checks.append( Tree( 5, Tree( 2, Tree( 1, Tree( 0 ) ), Tree( 4, Tree( 3 ) ) ), Tree( 8, Tree( 7, Tree( 6 ) ), Tree( 9 ) ) ) )
    tests.append( range( 10, 20, 2 ) )
    checks.append( Tree( 14, Tree( 12, Tree( 10 ) ), Tree( 18, Tree( 16 ) ) ) )

    for ( test, check ) in zip( tests, checks ):
        print "list:", test
        tree = listToTree( test )
        print "tree:", tree
        assert check == tree

