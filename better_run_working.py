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


# @proposition(E)
# class Ship:

#     def __init__(self, time, x, y):
#         self.time = time
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Ship{ self.time, self.x, self.y}"

@proposition(E)
class Ship:

    def __init__(self, time, x, y, has_cargo_type):
        self.time = time
        self.x = x
        self.y = y
        self.has_cargo_type = has_cargo_type

    def __repr__(self):
        return f"Ship{ self.time, self.x, self.y, self.has_cargo_type}"

    def swap_cargo(self, cargo):
        self.has_cargo_type=cargo

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

    def swap_cargo(self):
        self.has_cargo_type=0
        self.wants_cargo_type=0


@proposition(E)
class Time:

    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return f"Time{ self.i}"

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
    w_y3 = [2, 3]
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

# def generate_paths():
#     left = (ship.x-1, ship.y)
#     right = (ship.x+1, ship.y)
#     up = (ship.x, ship.y-1)
#     down = (ship.x, ship.y+1)
#     #idk

LEFT = -1
RIGHT = 1
UP = 2
DOWN = -2

#increment should always start at 0
def generate_paths(increment, time, visited):
    print("")
    print("Generate Paths")
    print("")
    ship_copy
    if increment == time:
        print("for time step " + str(time) + " these are the avalible moves")
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
    print("")
    print("is valid test")
    print("")
    ship_copy
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

        if len(temp_list) == time + 1:
            valid_paths.append(i)

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
            

# def is_valid(locations, time):
#     #time variable is used to determine which lists are valid lengths 
#     #(if u can find a better way than passing a var do it)

#     water = water_creation()

#     valid_paths = []
#     # print(locations)
#     for i in locations:
#         temp_list = []
#         for ship in i:
#             for w in water:
#                 if ship.x == w.x and ship.y == w.y:
#                     temp_list.append(ship)
#         if len(temp_list) == time + 1:
#             valid_paths.append(temp_list)
#     pprint.pprint(valid_paths)
#     return valid_paths

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
                    # temp_list.append([s, "water"])
                    temp_list.append(s)
            for p in temp_ports:
                if s.x == p.x and s.y == p.y and s.has_cargo_type == p.wants_cargo_type:
                    s.has_cargo_type = p.has_cargo_type
                    ship_has = p.has_cargo_type
                    p.has_cargo_type = 0
                    p.wants_cargo_type = 0
                    # temp_list.append([s, "port, swapped cargo"])
                    temp_list.append(s)
                    # print("did this at: (", ship.x, ",", ship.y, ")")
                elif s.x == p.x and s.y == p.y:

                    # temp_list.append([s, "port, did not swap cargo"])
                    temp_list.append(s)
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
            print(ship)
            for w in water:
                if ship.x == w.x and ship.y == w.y:
                    temp_list.append([ship, "water"])
            for p in temp_ports:
                if ship.x == p.x and ship.y == p.y:
                    temp_list.append([ship, "port"])
                elif ship.x == p.x and ship.y == p.y:
                    temp_list.append([ship, "port"])
            
        if len(temp_list) == time + 1:
            valid_paths.append(locations[1][x])
        
    return valid_paths

# water = water_creation()
# for i in water:
#     constraint.add_exactly_one(E, i)

# land = land_creation()
# for i in land:
#     constraint.add_exactly_one(E, i)

# for i in ports:
#     # E.add_constraint(Port(5, i.x, i.y, 0, 0))
#     constraint.add_exactly_one(E, i)



def theory(locations):

    time = len(locations[0])-1

    water= water_creation()
    land = land_creation()
    #should make 2 port lists, one fullfilled one not 
    #but how to link the 2?
    ports = port_creation()
    finished_ports = []

    temp_ports = []
    temp_ports2 = []
    for i in ports:
        finished_ports.append(Port(i.time, i.x, i.y, 0, 0))
        for t in range(time):
            prop = Port(t+1, i.x, i.y, i.has_cargo_type, i.wants_cargo_type)
            temp_ports.append(prop)
            temp_ports2.append(Port(t+1, i.x, i.y, 0, 0))
    for i in temp_ports:
        ports.append(i)
    for i in temp_ports2:
        finished_ports.append(i)

    #this constraint states any given port at any time step can either have it's goods or be finished
    for i in range(len(ports)):
        constraint.add_exactly_one(E, ports[i], finished_ports[i])

    #makes that ports at the last time step MUST be true
    for p in finished_ports:
        if p.time == time:
            E.add_constraint(p)

    for p in ports:
        if p.time == 0:
            E.add_constraint(p)


    for q in range(time+1):
        temp_list = []
        for r in range(len(locations)):
            temp_list.append(locations[r][q])
                
        print()
        print(temp_list)
        print()
        print(q)
        constraint.add_at_most_one(E, *temp_list)

    #this entire chunk makes sure that any new Ship steps must be adjacent to the one currently implemented 
    for x in locations:
        for ship in x:
            adjacent_tup = []
            adjacent_tdown = []
            if ship.time == 0:
                E.add_constraint(ship)
            for temp in x:
                if (ship.x == temp.x+1 or ship.x == temp.x-1) and ship.y == temp.y and ship.time == temp.time-1:
                    adjacent_tup.append(temp)
                elif ship.x == temp.x and (ship.y == temp.y+1 or ship.y == temp.y-1) and ship.time == temp.time-1:
                    adjacent_tup.append(temp)
                elif ship.x == temp.x and (ship.y == temp.y+1 or ship.y == temp.y-1) and ship.time == temp.time+1:
                    adjacent_tdown.append(temp)
                elif (ship.x == temp.x+1 or ship.x == temp.x-1) and ship.y == temp.y and ship.time == temp.time+1:
                    adjacent_tdown.append(temp)

            if len(adjacent_tup) != 0:
                constraint.add_at_most_one(E, *adjacent_tup)
            if len(adjacent_tdown) != 0:
                constraint.add_at_most_one(E, *adjacent_tdown)
            
            for p in finished_ports:
                if ship.x == p.x and ship.y == p.y and ship.time == p.time and p.time != 0:
                    for t in finished_ports:
                        if ship.x == t.x and ship.y == t.y and ship.time == t.time+1 and t.time != 0:
                            #constraint.add_at_least_one(E, t, ship)
                            constraint.add_at_most_one(E, t, ship)
                    #constraint.add_at_least_one(E, Port(p.time-1, p.x, p.y, 0, 0), ship)
                    
            
            #can't use same ship twice, duhhhhhhh
            #the if statements never trigger

            for p in ports:
                #if there is a ship at a time step above the port, either that ship can be true or the unfinished port can be true, but not both 
                if ship.x == p.x and ship.y == p.y and ship.time == p.time+1:
                     for t in ports:
                        if ship.x == t.x and ship.y == t.y and ship.time == t.time:
                            #constraint.add_at_least_one(E, t, ship)
                            constraint.add_at_most_one(E, t, ship)
                    #constraint.add_at_least_one(E, Port(p.time+1, p.x, p.y, p.has_cargo_type, p.wants_cargo_type), ship)


                #else statement is here in case we want the player to move the ship's starting location
                #in that sceneario techniically the ship can start at a port and therefore must have a p.time == 0 clause
                else:
                    pass
                    

            #for p in ports:
            #    if ship.x == p.x and ship.y == p.y and ship.time == p.time:
            #        constraint.add_exactly_one(E, p, ship)
            
    #if port is at max time it must be 0,0 that implies it was either touched before or at that turn
    #set the last ports to be unconditonally true since it's our win condition 
    #IT WORKS
    #need to constrain that if it hasn't been touched by ship it CAN'T BE FULLFILLED



    T = E.compile()
    sol = T.solve()
    print()
    E.pprint(T, sol)
    print()
    print("\nSatisfiable: %s" % T.satisfiable())
    pprint.pprint(sol)

    print_variables(sol, "Ship", True)
    print_variables(sol, "Port", True)
    #print(key)
    #print(sol.values())

        #for ship in x:
            #constraint.add_at_most_k(E, 2, Ship)
            #constraint.add_at_least_one(E, Ship)
            #constraint.add_at_most_one(E, ship)

    return T


#visited is all the possible paths within the current time step 
#for time 0 it will be left, right, up, down. etc



def print_variables(sol, word, state):

    print()
    for key in sol:
        if word in str(key):
            if sol.get(key):
                print(key, sol.get(key))
    print()

# def is_valid(locations, time):
#     #time variable is used to determine which lists are valid lengths 
#     #(if u can find a better way than passing a var do it)

#     water = water_creation()

#     # print(ports.wants_cargo_type)

#     valid_paths = []
#     for i in locations:
#         temp_list = []
#         for ship in i:
#             for w in water:
#                 if ship.x == w.x and ship.y == w.y:
#                     temp_list.append([ship, "water"])
            
#             for p in ports:
#                 if ship.x == p.x and ship.y == p.y and ship.has_cargo_type == p.wants_cargo_type and len(temp_list) == time + 1:
#                     ship.has_cargo_type = p.has_cargo_type
#                     p.has_cargo_type = 0
#                     p.wants_cargo_type = 0
#                     temp_list.append([ship, "port, swapped cargo"])
#                     print("ship has: ", ship.has_cargo_type)
#                     print("port wants: ", p.wants_cargo_type)
#                     print(p)
#                 elif ship.x == p.x and ship.y == p.y:
#                     temp_list.append([ship, "port, did not swap cargo"])
#                     print("ship has: ", ship.has_cargo_type)
#                     print("port wants: ", p.wants_cargo_type)
#                     print(p)

#         if len(temp_list) == time + 1:
#             valid_paths.append(temp_list)
#     pprint.pprint(valid_paths)

#     return valid_paths

# def example_theory():

#     # Add the board constraints
#     # add_board_configuration(board_num)

#     T = E.compile()
#     return T

    
if __name__ == "__main__":

    # time = 6

    # cargo=Cargo(0,"Cars")
    # # ship = Ship(0, 2, 1)
    # visual()
    # visited = ([LEFT], [RIGHT], [UP], [DOWN])
    # # test = generate_paths(0,time,visited)
    # # #print(test)
    # # #parsed = parse(test)
    # # # pprint.pprint(parsed)
    # # #paths = is_valid(parsed, time)
    # # #win_path(paths)
    # # test2 = create_trimmed_paths(0, time, visited)
    # # #print(test2)



    time = 1

    cargo=Cargo(0,"Cars")
    # ship = Ship(0, 2, 1)
    visual()
    visited = ([LEFT], [RIGHT], [UP], [DOWN])
    test = create_trimmed_paths(0,time,visited)
    parsed = parse(test)
    pprint.pprint(parsed)
    paths = is_valid(parsed, time)
    # print(paths)
    
    # win_path(paths)

    # test = generate_paths(0,time,visited)
    # # print(test)
    # parsed = parse(test)
    # # pprint.pprint(parsed)
    # paths = is_valid(parsed, time)
    # win_path(paths)


    # T = E.compile()
    theory = theory(paths)
    sol = theory.solve()
    E.pprint(theory, sol)
    # pprint.pprint(sol)

    # Don't compile until you're finished adding all your constraints!
    # T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % theory.satisfiable())
    print("# Solutions: %d" % count_solutions(theory))
    # print("   Solution: %s" % T.solve())
    
    # E.pprint(T, T.solve())
    # print(E.introspect())
    # print("\nVariable likelihoods:")
    
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()