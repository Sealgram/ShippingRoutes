from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import pprint
from tabulate import tabulate

MAX = 5

# Encoding that will store all of your constraints
E = Encoding()

####################################
#
#   Propositions
#
####################################

# Proposition to initialize the land nodes 

@proposition(E)
class Land:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Land{ self.x, self.y}"


@proposition(E)
class Water:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Water{ self.x, self.y}"


@proposition(E)
class Ship:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ship{ self.x, self.y}"

# Proposition to initialize what kind of cargo is on the ship
@proposition(E)
class Cargo:
    
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f"Cargo_{self.type}"

# Proposition to initialize the port nodes
@proposition(E)
class Port:
    
    def __init__(self, x, y, has_cargo_type, wants_cargo_type):
        self.x = x
        self.y = y
        self.has_cargo_type = has_cargo_type
        self.wants_cargo_type = wants_cargo_type

    def __repr__(self):
        return f"Port{self.x, self.y, self.has_cargo_type, self.wants_cargo_type}"

@proposition(E)
class Previous:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Previous{self.x, self.y}"

####################################
#
#   Making the Map
#
####################################

def land_creation():
    l_y0 = [0, 1, 2, 3, 4]
    l_y1 = [0, 4]
    l_y2 = [0, 4]
    l_y3 = [0, 4]
    l_y4 = [0, 1, 2, 3, 4]
    l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4]
    land = []
     # initialize all land on map

    for y in range(len(l_yall)):
        for x in range(len(l_yall[y])):
            prop = Land(l_yall[y][x], y)
            land.append(prop)
    return land

def water_creation():
    w_y0 = []
    w_y1 = [1, 2, 3]
    w_y2 = [1, 2, 3]
    w_y3 = [1, 3]
    w_y4 = []
    w_yall =[w_y0, w_y1, w_y2, w_y3, w_y4]
    water = []
    # initialize all water on map
    for y in range(len(w_yall)):
        for x in range(len(w_yall[y])):
            prop = Water(w_yall[y][x], y)
            water.append(prop)
    return water

def port_creation():
    ports = []
    prop = Port(2, 3, "Appliances", "Cars")
    ports.append(prop)
    # pprint.pprint(ports)
    return ports

def map_creation():
    map = [[0 for x in range(MAX)] for y in range(MAX)]
    land = land_creation()
    for i in range(len(land)):
        # print("at loop " + str(i))
        # print("putting land at x:" + str(land[i].x) + " y:" + str(land[i].y) + " with object " + str(land[i]))
        map[land[i].x][land[i].y] = "L"

    water = water_creation()
    for i in range(len(water)):
        # print("at loop " + str(i))
        # print("putting land at x:" + str(water[i].x) + " y:" + str(water[i].y) + " with object " + str(water[i]))
        map[water[i].x][water[i].y] = "-"

    ports = port_creation()
    for i in range(1):
        # print("at loop " + str(i))
        # print("putting water at x:" + str(ports[i].x) + " y:" + str(ports[i].y) + " with object " + str(ports[i]))
        map[ports[i].x][ports[i].y] = "P"

    # for x in range(MAX):
    #     print()
    #     for y in range(MAX):
    #         print(map[x][y], end='')

    return map

def visual():
    visual = map_creation()
    visual[ship.x][ship.y] = "S"

    table = [[visual[x][0] for x in range(MAX)], [visual[x][1] for x in range(MAX)],
             [visual[x][2] for x in range(MAX)], [visual[x][3] for x in range(MAX)],
             [visual[x][4] for x in range(MAX)]]

    print()
    print(tabulate(table, tablefmt="fancy_grid"))

def things_on_tile(x, y):
    things=[]

    land = land_creation()
    for i in range(len(land)):
        if land[i].x == x and land[i].y == y:
            things.append(land[i])

    water = water_creation()
    for i in range(len(water)):
        if water[i].x == x and water[i].y == y:
            things.append(water[i])

    ports = port_creation()
    for i in range(len(ports)):
        if ports[i].x == x and ports[i].y == y:
            things.append(ports[i])

    if ship.x == x and ship.y == y:
        things.append(ship)

    return things

    
if __name__ == "__main__":

    cargo=Cargo("Cars")
    ship = Ship(2, 1)
    visual()


    # T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    # T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    # print("\nSatisfiable: %s" % T.satisfiable())
    # print("# Solutions: %d" % count_solutions(T))
    # print("   Solution: %s" % T.solve())
    # E.pprint(T, T.solve())
    # print(E.introspect())
    # print("\nVariable likelihoods:")
    
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
