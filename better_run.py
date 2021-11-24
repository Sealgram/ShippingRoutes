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

# Proposition to initialize the time variable
@proposition(E)
class Time:

    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return f"Time{ self.i}"

# Proposition to initialize the land nodes 
@proposition(E)
class Land:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Land{ self.x, self.y}"

# Proposition to initialize the water nodes
@proposition(E)
class Water:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Water{ self.x, self.y}"

# Proposition to initialize the ship
@proposition(E)
class Ship:

    def __init__(self, time, x, y, has_cargo_type):
        self.time = time
        self.x = x
        self.y = y
        self.has_cargo_type = has_cargo_type

    def __repr__(self):
        return f"Ship{ self.time, self.x, self.y, self.has_cargo_type}"

# Proposition to initialize what kind of cargo is on the ship
@proposition(E)
class Cargo:
    
    def __init__(self, time, type):
        self.time = time
        self.type = type

    def __repr__(self):
        return f"Cargo_{self.time, self.type}"

# Proposition to initialize the port nodes
@proposition(E)
class Port:
    
    def __init__(self, time, x, y, has_cargo_type, wants_cargo_type):
        self.time = time
        self.x = x
        self.y = y
        self.has_cargo_type = has_cargo_type
        self.wants_cargo_type = wants_cargo_type

    def __repr__(self):
        return f"Port{self.time, self.x, self.y, self.has_cargo_type, self.wants_cargo_type}"

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
    w_y3 = [3]
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
    prop = Port(0, 2, 3, "Appliances", "Cars")
    ports.append(prop)
    prop = Port(0, 1, 3, "Produce", "Appliances")
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

LEFT = -1
RIGHT = 1
UP = 2
DOWN = -2

#increment should always start at 0
def generate_paths(increment, time, visited):

    if increment == time:
        print("for time step " + str(time) + " these are the avalible moves")
        print(visited)
        return visited
    elif increment == 0:
        visited = ([LEFT], [RIGHT], [UP], [DOWN])
        return generate_paths(increment+1, time, visited)
    else:
        new_list = []
        for i in visited:
            left = i.copy()
            left.append(LEFT)
            right = i.copy()
            right.append(RIGHT)
            up = i.copy()
            up.append(UP)
            down = i.copy()
            down.append(DOWN)

            new_list.append(left)
            new_list.append(up)
            new_list.append(right)
            new_list.append(down)

        visited = new_list
        return generate_paths(increment+1, time, visited)
        

ship = Ship(0, 1, 1, "Cars")
ship_locations = []

def is_valid_test(final_list, time):
    #time variable is used to determine which lists are valid lengths 
    #(if u can find a better way than passing a var do it)

    water = water_creation()
    locations = final_list[0]
    visited = final_list[1]

    
    valid_paths = []
    for i in locations:
        temp_ports = port_creation()
        temp_list = []
        for ship in i:
            for w in water:
                if ship.x == w.x and ship.y == w.y:
                    temp_list.append([ship, "water"])
            for p in temp_ports:
                if ship.x == p.x and ship.y == p.y and ship.has_cargo_type == p.wants_cargo_type:
                    ship.has_cargo_type = p.has_cargo_type
                    p.has_cargo_type = 0
                    p.wants_cargo_type = 0
                    temp_list.append([ship, "port, swapped cargo"])
                elif ship.x == p.x and ship.y == p.y:
                    temp_list.append([ship, "port, did not swap cargo"])
                    print("ship has: ", ship.has_cargo_type)
                    print("port wants: ", p.wants_cargo_type)

        if len(temp_list) == time + 1:
            valid_paths.append(i)
    pprint.pprint(valid_paths)

    return valid_paths



def parse(visited):

    ship_copy = Ship(ship.time, ship.x, ship.y, ship.has_cargo_type)

    ship_list = []
    
    for i in visited:
        time = ship.time
        ship_copy.x = ship.x
        ship_copy.y = ship.y 
        temp_list = []
        temp_list.append(ship)
        for j in i:
            ship_copy.time = time + 1
            if j == -1:
                ship_copy.x = ship_copy.x-1
            elif j == 1:
                ship_copy.x = ship_copy.x+1
            elif j == 2:
                ship_copy.y = ship_copy.y+1
            elif j == -2:
                ship_copy.y = ship_copy.y-1
            ship_temp = Ship(ship_copy.time, ship_copy.x, ship_copy.y, ship.has_cargo_type)
            
            temp_list.append(ship_temp)
            time += 1
        ship.time
        ship_list.append(temp_list)
    # pprint.pprint(ship_list)
    return ship_list
            

ports = port_creation()

def is_valid(locations, time):
    #time variable is used to determine which lists are valid lengths 
    #(if u can find a better way than passing a var do it)

    water = water_creation()

    valid_paths = []

    for i in locations:
        
        temp_ports = port_creation()
        temp_list = []

        for s in i:
            if (s.time != 0):
                s.has_cargo_type = ship_has
            else:
                ship_has = s.has_cargo_type

            for w in water:
                if s.x == w.x and s.y == w.y:
                    temp_list.append([s, "water"])
            for p in temp_ports:
                if s.x == p.x and s.y == p.y and s.has_cargo_type == p.wants_cargo_type:
                    s.has_cargo_type = p.has_cargo_type
                    ship_has = p.has_cargo_type
                    p.has_cargo_type = 0
                    p.wants_cargo_type = 0
                    temp_list.append([s, "port, swapped cargo"])
                    # print("did this at: (", ship.x, ",", ship.y, ")")
                elif s.x == p.x and s.y == p.y:

                    temp_list.append([s, "port, did not swap cargo"])
                    # print("ship has: ", ship.has_cargo_type)
                    # print("port wants: ", p.wants_cargo_type)

        if len(temp_list) == time + 1:
            valid_paths.append(temp_list)
    pprint.pprint(valid_paths)

    return valid_paths

def win_path(locations):
    
    win_paths = []

    for i in locations:
        counter = 0
        for j in i:
            # for k in j:
            if j[1] == 'port, swapped cargo':
                counter += 1
        if counter == len(ports):
            win_paths.append(i)
    
    print("WINNERS")
    pprint.pprint(win_paths)




#increment should always start at 0
def create_trimmed_paths(increment, time, visited):

    if increment == time:
        print("for time step " + str(time) + " these are the avalible moves")
        print(visited)
        return visited
    elif increment == 0:
        visited = ([LEFT], [RIGHT], [UP], [DOWN])
        visited = is_valid_test(parse_test(visited), increment+1)
        return create_trimmed_paths(increment+1, time, visited)
    else:
        new_list = []
        for i in visited:
            left = i.copy()
            left.append(LEFT)
            right = i.copy()
            right.append(RIGHT)
            up = i.copy()
            up.append(UP)
            down = i.copy()
            down.append(DOWN)

            new_list.append(left)
            new_list.append(up)
            new_list.append(right)
            new_list.append(down)

        visited = new_list
        visited = is_valid_test(parse_test(visited), increment+1)
        return create_trimmed_paths(increment+1, time, visited)

def parse_test(visited):

    ship_copy = Ship(ship.time, ship.x, ship.y, ship.has_cargo_type)

    ship_list = []
    unparsed_list = []

    for i in visited:
        time = ship.time
        ship_copy.x = ship.x
        ship_copy.y = ship.y 
        temp_list = []
        temp_list.append(ship)
        for j in i:
            ship_copy.time = time + 1
            if j == -1:
                ship_copy.x = ship_copy.x-1
            elif j == 1:
                ship_copy.x = ship_copy.x+1
            elif j == 2:
                ship_copy.y = ship_copy.y+1
            elif j == -2:
                ship_copy.y = ship_copy.y-1
            ship_temp = Ship(ship_copy.time, ship_copy.x, ship_copy.y, ship.has_cargo_type)
            
            temp_list.append(ship_temp)
            time += 1
        ship.time
        ship_list.append(temp_list)
        unparsed_list.append(i)
    # pprint.pprint(ship_list)
    final_list = [ship_list, unparsed_list]
    return final_list


#locations is ship_list 
#it contains all the ship coordinates for a given time step
#for time 0 it will have the ship move one to the left, one to the right, one up, and one down
#the list of valid moves doesn't actually matter we just need the unparsed moves to be sent back after being trimmed 
#set locations to be of the format [[ship_moves], [uparsed_moves]]
#use a range for loop and a nested for loop 
#for ship in i[x]
def is_valid_test(locations, time):
    #time variable is used to determine which lists are valid lengths 
    #(if u can find a better way than passing a var do it)

    water = water_creation()

    valid_paths = []
    for x in range(len(locations[0])):
        temp_ports = port_creation()
        temp_list = []
        for ship in locations[0][x]:
            for w in water:
                if ship.x == w.x and ship.y == w.y:
                    temp_list.append([ship, "water"])
            for p in temp_ports:
                if ship.x == p.x and ship.y == p.y and ship.has_cargo_type == p.wants_cargo_type:
                    ship.has_cargo_type = p.has_cargo_type
                    p.has_cargo_type = 0
                    p.wants_cargo_type = 0
                    temp_list.append([ship, "port, swapped cargo"])
                elif ship.x == p.x and ship.y == p.y:
                    temp_list.append([ship, "port, did not swap cargo"])

        if len(temp_list) == time + 1:
            valid_paths.append(locations[1][x])

    return valid_paths

####################################
#
#   Constraints
#
####################################

water = water_creation()
for i in water:
    constraint.add_exactly_one(E, i)

land = land_creation()
for i in land:
    constraint.add_exactly_one(E, i)

for i in ports:
    E.add_exactly_one(Port(5, i.x, i.y, 0, 0))


    
if __name__ == "__main__":
    time = 5

    cargo=Cargo(0,"Cars")
    # ship = Ship(0, 2, 1)
    visual()
    visited = ([LEFT], [RIGHT], [UP], [DOWN])
    test = create_trimmed_paths(0,time,visited)
    parsed = parse(test)
    pprint.pprint(parsed)
    paths = is_valid(parsed, time)
    win_path(paths)

    # T = E.compile()
    # sol = T.solve()
    # print(sol)

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