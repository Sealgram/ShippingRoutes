
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

@proposition(E)
class Land:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Land{ self.x, self.y}"


# #x land locations for yth row

# l_y0 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# l_y1 = [0,9,10,11,12,13,21]
# l_y2 = [0,2,3,4,5,10,11,12,21]
# l_y3 = [0,2,3,4,12,15,16,17,18,21]
# l_y4 = [0,2,3,4,5,8,9,10,15,16,17,18,21]
# l_y5 = [0,4,5,10,18,21]
# l_y6 = [0,13,14,15,16,21]
# l_y7 = [0,13,14,15,21]
# l_y8 = [0,3,4,8,9,13,14,15,16,21]
# l_y9 = [0,7,8,9,10,14,15,16,17,21]
# l_y10 = [0,8,9,16,20,21]
# l_y11 = [0,19,20,21]
# l_y12 = [0,3,4,5,6,7,8,18,19,20,21]
# l_y13 = [0,2,3,4,5,6,7,8,9,19,20,21]
# l_y14 = [0,3,4,5,6,7,8,14,15,20,21]
# l_y15 = [0,2,3,13,14,15,16,17,21]
# l_y16 = [0,2,3,10,11,12,13,14,15,16,17,21]
# l_y17 = [0,3,4,10,11,12,13,14,15,16,21]
# l_y18 = [0,4,10,11,12,13,14,15,21]
# l_y19 = [0,21]
# l_y20 = [0,21]
# l_y21 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

# l_yall = [
#     l_y0,l_y1,l_y2,l_y3,l_y4,l_y5,l_y6,l_y7,l_y8,l_y9,
#     l_y10,l_y11,l_y12,l_y13,l_y14,l_y15,l_y16,l_y17,l_y18,l_y19,
#     l_y20,l_y21
# ]

# land = []

# # initialize all land on map 
# for y in range(len(l_yall)):
#     for x in range(len(l_yall[y])):
#         prop = Land(l_yall[y][x], y)
#         land.append(prop)

# pprint.pprint(land)

# Proposition to initialize the water nodes

@proposition(E)
class Water:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Water{ self.x, self.y}"

# #x water locations for yth row
# w_y0 = []
# w_y1 = [1,2,3,4,5,6,7,8,14,15,16,17,18,19,20]
# w_y2 = [1,6,7,8,9,13,14,15,16,17,18,19,20]
# w_y3 = [1,5,6,7,8,9,10,11,13,14,19,20]
# w_y4 = [1,6,7,11,12,13,14,19,20]
# w_y5 = [1,2,3,6,7,8,9,11,12,13,14,15,16,17,19,20]
# w_y6 = [1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20]
# w_y7 = [1,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20]
# w_y8 = [1,2,5,6,7,10,11,12,17,18,19,20]
# w_y9 = [1,2,3,4,5,6,11,12,13,18,19,20]
# w_y10 = [1,2,3,4,5,6,7,10,11,12,13,14,15,17,18,19]
# w_y11 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# w_y12 = [1,2,9,10,11,12,13,14,15,16,17]
# w_y13 = [1,10,11,12,13,14,15,16,17,18]
# w_y14 = [1,2,9,10,11,12,13,16,17,18,19]
# w_y15 = [1,4,5,6,7,8,9,10,11,12,18,19,20]
# w_y16 = [1,4,5,6,7,8,9,18,19,20]
# w_y17 = [1,2,5,6,7,8,9,17,18,19,20]
# w_y18 = [1,2,3,5,6,7,8,9,16,17,18,19,20]
# w_y19 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# w_y20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# w_y21 = []

# w_yall = [
#     w_y0,w_y1,w_y2,w_y3,w_y4,w_y5,w_y6,w_y7,w_y8,w_y9,
#     w_y10,w_y11,w_y12,w_y13,w_y14,w_y15,w_y16,w_y17,w_y18,w_y19,
#     w_y20,w_y21
# ]

# water = []

# # initialize all water on map 
# for y in range(len(w_yall)):
#     for x in range(len(w_yall[y])):
#         prop = Water(w_yall[y][x], y)
#         water.append(prop)
   
# pprint.pprint(water)

# Proposition to initialize the ship 

@proposition(E)
class Ship:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ship{ self.x, self.y}"

#need to initialize all ship on map
ship = Ship(2, 4)

pprint.pprint(ship)

# Proposition to initialize what kind of cargo is on the ship
@proposition(E)
class Cargo:
    
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f"Cargo_{self.type}"



cargo=Cargo("Cars")

pprint.pprint(cargo)

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



# ports = []
# #need to initialize all ports on map
# for x in range(10):
#     prop = Port(x, 0, cargo[1],cargo[2])
#     ports.append(prop)
    
# pprint.pprint(ports)


# Proposition to initialize the wildcard nodes
# @proposition(E)
# class BasicPropositions:

#     def __init__(self, data):
#         self.data = data

#     def __repr__(self):
#         return f"A.{self.data}"

def land_creation():
    l_y0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    l_y1 = [0, 9, 10, 11, 12, 13, 21]
    l_y2 = [0, 2, 3, 4, 5, 10, 11, 12, 21]
    l_y3 = [0, 2, 3, 4, 12, 15, 16, 17, 18, 21]
    l_y4 = [0, 2, 3, 4, 5, 8, 9, 10, 15, 16, 17, 18, 21]
    l_y5 = [0, 4, 5, 10, 18, 21]
    l_y6 = [0, 13, 14, 15, 16, 21]
    l_y7 = [0, 13, 14, 15, 21]
    l_y8 = [0, 3, 4, 8, 9, 13, 14, 15, 16, 21]
    l_y9 = [0, 7, 8, 9, 10, 14, 15, 16, 17, 21]
    l_y10 = [0, 8, 9, 16, 20, 21]
    l_y11 = [0, 19, 20, 21]
    l_y12 = [0, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21]
    l_y13 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 19, 20, 21]
    l_y14 = [0, 3, 4, 5, 6, 7, 8, 14, 15, 20, 21]
    l_y15 = [0, 2, 3, 13, 14, 15, 16, 17, 21]
    l_y16 = [0, 2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 21]
    l_y17 = [0, 3, 4, 10, 11, 12, 13, 14, 15, 16, 21]
    l_y18 = [0, 4, 10, 11, 12, 13, 14, 15, 21]
    l_y19 = [0, 21]
    l_y20 = [0, 21]
    l_y21 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

    l_yall = [
        l_y0, l_y1, l_y2, l_y3, l_y4, l_y5, l_y6, l_y7, l_y8, l_y9,
        l_y10, l_y11, l_y12, l_y13, l_y14, l_y15, l_y16, l_y17, l_y18, l_y19,
        l_y20, l_y21
    ]

    land = []

    # initialize all land on map
    for y in range(len(l_yall)):
        for x in range(len(l_yall[y])):
            prop = Land(l_yall[y][x], y)
            land.append(prop)

    return land

land=land_creation()

def water_creation():
    # x water locations for yth row
    w_y0 = []
    w_y1 = [1, 2, 3, 4, 5, 6, 7, 8, 14, 15, 16, 17, 18, 19, 20]
    w_y2 = [1, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20]
    w_y3 = [1, 5, 6, 7, 8, 9, 10, 11, 13, 14, 19, 20]
    w_y4 = [1, 6, 7, 11, 12, 13, 14, 19, 20]
    w_y5 = [1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20]
    w_y6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19, 20]
    w_y7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20]
    w_y8 = [1, 2, 5, 6, 7, 10, 11, 12, 17, 18, 19, 20]
    w_y9 = [1, 2, 3, 4, 5, 6, 11, 12, 13, 18, 19, 20]
    w_y10 = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 18, 19]
    w_y11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    w_y12 = [1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    w_y13 = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    w_y14 = [1, 2, 9, 10, 11, 12, 13, 16, 17, 18, 19]
    w_y15 = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 20]
    w_y16 = [1, 4, 5, 6, 7, 8, 9, 18, 19, 20]
    w_y17 = [1, 2, 5, 6, 7, 8, 9, 17, 18, 19, 20]
    w_y18 = [1, 2, 3, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20]
    w_y19 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    w_y20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    w_y21 = []

    w_yall = [
        w_y0, w_y1, w_y2, w_y3, w_y4, w_y5, w_y6, w_y7, w_y8, w_y9,
        w_y10, w_y11, w_y12, w_y13, w_y14, w_y15, w_y16, w_y17, w_y18, w_y19,
        w_y20, w_y21
    ]

    water = []

    # initialize all water on map
    for y in range(len(w_yall)):
        for x in range(len(w_yall[y])):
            prop = Water(w_yall[y][x], y)
            water.append(prop)

    return water

water=water_creation()

def port_creation():
    ports = []

    for c1 in range(0, 3):
        if c1 == 0:
            prop = Port(2, 4, "Appliances", "Cars")
            ports.append(prop)
            prop = Port(13, 6, "Appliances", "Produce")
            ports.append(prop)
        if c1 == 1:
            prop = Port(10, 18, "Cars", "Appliances")
            ports.append(prop)
            prop = Port(18, 12, "Cars", "Produce")
            ports.append(prop)
        if c1 == 2:
            prop = Port(12, 3, "Produce", "Appliances")
            ports.append(prop)
            prop = Port(5, 14, "Produce", "Cars")
            ports.append(prop)

    # pprint.pprint(ports)
    return ports

port=port_creation()

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
    for i in range(len(ports)):
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
             [visual[x][4] for x in range(MAX)], [visual[x][5] for x in range(MAX)], [visual[x][6] for x in range(MAX)],
             [visual[x][7] for x in range(MAX)], [visual[x][8] for x in range(MAX)],
             [visual[x][9] for x in range(MAX)], [visual[x][10] for x in range(MAX)],
             [visual[x][11] for x in range(MAX)], [visual[x][12] for x in range(MAX)],
             [visual[x][13] for x in range(MAX)],
             [visual[x][14] for x in range(MAX)], [visual[x][15] for x in range(MAX)],
             [visual[x][16] for x in range(MAX)], [visual[x][17] for x in range(MAX)],
             [visual[x][18] for x in range(MAX)],
             [visual[x][19] for x in range(MAX)], [visual[x][20] for x in range(MAX)],
             [visual[x][21] for x in range(MAX)]]

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

####################################
#
#   Constraints
#
####################################



#no 2 things can be on the same tile, must add exception to land and ports and ships and ports, easy fix via if statement checking what is contained within the list
for x in range(MAX):
    for y in range(MAX):
        constraint.add_exactly_one(E, things_on_tile(x,y))

#if Ship(x, y) is not implied then Ship(x, y) is false in the left side, do we have to imply that a Ship is at said location
#for i in port:
    #if i.x == ship.x and i.y == ship.y and i.wants_cargo_type == cargo.type:
        #E.add_constraint(Ship(ship.x, ship.y) >> Port(ship.x, ship.y, 0, 0) & Cargo(i.has_cargo_type))

for i in port:
    if i.x == ship.x and i.y == ship.y and i.wants_cargo_type == cargo.type:
        E.add_constraint(Ship(ship.x, ship.y) & Port(ship.x, ship.y, i.has_cargo_type, i.wants_cargo_type) & Cargo(i.wants_cargo_type) >> Port(ship.x, ship.y, 0, 0) & Cargo(i.has_cargo_type))

#a port must be on edge of land
for i in port:
    E.add_constraint(Port(i.x, i.y, i.has_cargo_type, i.wants_cargo_type) & (Water(i.x-1, i.y) | Water(i.x+1, i.y) | Water(i.x, i.y-1) | Water(i.x, i.y+1)) >> Land(i.x, i.y))

#ship can't touch land unless ship is on port
for x in range(MAX):
    for y in range(MAX):
        for i in port:
            constraint.add_at_most_one(E, (Land(x, y) & ~Ship(x, y)) | (Land(x, y) & Ship(x,y) & Port(x, y, i.has_cargo_type, i.wants_cargo_type)))

#alternate solution for ship can't touch land unless ship is on port
#possibly works if we loop the solutions but I doubt it, first solution covers the entire map
for i in port:
    constraint.add_at_most_one(E, (Land(ship.x, ship.y) & ~Ship(ship.x, ship.y)) | (Land(ship.x, ship.y) & Ship(ship.x,ship.y) & Port(ship.x, ship.y, i.has_cargo_type, i.wants_cargo_type)))

#port can not have and want the same the cargo type
#might not need the second variable as the for loop should cover all cargo types
for i in port:
    E.add_constraint(~Port(i.x, i.y, i.wants_cargo_type, i.wants_cargo_type) & ~Port(i.x, i.y, i.has_cargo_type, i.has_cargo_type))

#alternate solution for: port can not have and want the same the cargo type
cargo_types=["Appliances", "Cars, Produce"]
for x in range(MAX):
    for y in range(MAX):
        for i in cargo_types:
            E.add_constraint(~Port(x, y, i, i))



#other constraints determine that 2 ports can not be on the same location




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
