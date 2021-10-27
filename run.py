
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()


####################################
#
#   Propositions
#
####################################

# Proposition to initialize the land nodes

# Proposition to initialize the water nodes

# Proposition to initialize the ship 

# Proposition to initialize what kind of cargo is on the ship

# Proposition to initialize the port nodes

# Proposition to initialize the wildcard nodes
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


####################################
#
#   Constraints
#
####################################

# Port must be on a land node that is adjacent to at least one water node

# The ship cannot touch a land node unless it is a port node

# A water node cannot also be a land node

# If a ship is at a port and has the cargo the port needs, the ship will take on the cargo the port has, drop the cargo the port
# needs, and the port's two cargo types will be set to null

# The ship can only move to one of the four adjacent nodes to the one it is currently on

# There are 9 ports to be randomly placed on the map, and they cannot be within two nodes of each other


####################################

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    T = E.compile()
    return T


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
