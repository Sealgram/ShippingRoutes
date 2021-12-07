from bauhaus import Encoding, proposition, constraint, print_theory
from bauhaus.utils import count_solutions, likelihood
import pprint
from tabulate import tabulate
import scenarios as S

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

    def __init__(self, time, x, y):
        self.time = time
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Ship{ self.time, self.x, self.y}"


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


@proposition(E)
class Time:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return f"Time{ self.i}"

####################################
#
#   Constraints
#
####################################

def ship_creation(MAX, time):
    ships = [] 
    for t in range(time+1):
        for x in range(MAX):
            for y in range(MAX):
                prop = Ship(t, x, y)
                ships.append(prop)
    return ships

def cargo_creation(time):
    cargos = []
    for t in range(time+1):
        prop = Cargo(t, "Cars")
        cargos.append(prop)
        prop = Cargo(t, "Produce")
        cargos.append(prop)
        prop = Cargo(t, "Appliances")
        cargos.append(prop)
    return cargos

def theory(time, scene, MAX):
    ships = ship_creation(MAX, time)
    ships2 = ship_creation(MAX, time)

    prop = Ship(0, 1, 1)
    for ship in ships:
        if ship.x == prop.x and ship.y == prop.y and ship.time == prop.time:
            print("this ship must be true", ship)
            E.add_constraint(ship)

    cargo = cargo_creation(time)
    water= S.water_creation(scene)
    land = S.land_creation(scene)
    ports = S.port_creation(scene)

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
            print(p, "must be true")
            E.add_constraint(p)

    for p in ports:
        if p.time == 0:
            E.add_constraint(p)


    for p in ports:
        lst = []
        for ship in ships:
            if ship.x == p.x and ship.y == p.y:
                lst.append(ship)
        if len(lst) != 0:
            constraint.add_at_least_one(E, *lst)


    #if a finished port is true then the finished port at the next time step must also be true 
    for p in finished_ports:
        for t in finished_ports:
            if p.x == t.x and p.y == t.y and t.time+1 == p.time:
                constraint.add_implies_all(E, t, p)
        

    #this entire chunk makes sure that any new Ship steps must be adjacent to the one currently implemented 
    #an implication is true if both are false 
    #how does one enforce adjacency 
    for ship in ships:
        adjacent_tup = []
        adjacent_tdown = []
        for temp in ships:
            if (ship.x == temp.x+1 or ship.x == temp.x-1) and ship.y == temp.y and ship.time+1 == temp.time:
                adjacent_tup.append(temp)
            elif ship.x == temp.x and (ship.y == temp.y+1 or ship.y == temp.y-1) and ship.time+1 == temp.time:
                adjacent_tup.append(temp)
            elif ship.x == temp.x and (ship.y == temp.y+1 or ship.y == temp.y-1) and ship.time-1 == temp.time:
                adjacent_tdown.append(temp)
            elif (ship.x == temp.x+1 or ship.x == temp.x-1) and ship.y == temp.y and ship.time-1 == temp.time:
                adjacent_tdown.append(temp)

        #this is pointless as of rn because the only one ship per time is already in place
        #needs to be modfied 
        if len(adjacent_tup) != 0:
            #constraint.add_implies_all(E, *adjacent_tup, ship)
            #constraint.add_at_most_one(E, ship, *adjacent_tup)
            #constraint.add_exactly_one(E, *adjacent_tup)
            if len(adjacent_tup) == 1:
                E.add_constraint(ship >> adjacent_tup[0])
            elif len(adjacent_tup) == 2:
                E.add_constraint(ship >> adjacent_tup[0] | adjacent_tup[1])
            elif len(adjacent_tup) == 3:
                E.add_constraint(ship >> adjacent_tup[0] | adjacent_tup[1] | adjacent_tup[2])
            else:
                #constraint.add_implies_all(E, ship, (~adjacent_tup[0] | ~adjacent_tup[1] | ~adjacent_tup[2] | ~adjacent_tup[3]) & ship)
                E.add_constraint(ship >> adjacent_tup[0] | adjacent_tup[1] | adjacent_tup[2] | adjacent_tup[3])
        if len(adjacent_tdown) != 0:
            #constraint.add_at_most_one(E, *adjacent_tdown)
            if len(adjacent_tdown) == 1:
                E.add_constraint(ship >> adjacent_tdown[0])
            elif len(adjacent_tdown) == 2:
                E.add_constraint(ship >> adjacent_tdown[0] | adjacent_tdown[1])
            elif len(adjacent_tdown) == 3:
                E.add_constraint(ship >> adjacent_tdown[0] | adjacent_tdown[1] | adjacent_tdown[2])
            else:
                E.add_constraint(ship >> adjacent_tdown[0] | adjacent_tdown[1] | adjacent_tdown[2] | adjacent_tdown[3])
            #constraint.add_exactly_one(E, *adjacent_tdown)



        #print("adjacent to ship:", ship)
        #print(adjacent_tup)
        #print(adjacent_tdown)
        #print()


        #any given finished port is either currently being touched by a ship or the port one time step below it is finished 
        #so just make the statement false or smthn 
        for p in finished_ports:
            if ship.x == p.x and ship.y == p.y and ship.time == p.time and p.time != 0:
                for t in finished_ports:
                    if ship.x == t.x and ship.y == t.y and ship.time == t.time+1:
                        #print("did this")
                        #print("added constraint ", t, " or ", ship, " or not ", p)
                        
                        #a finished port implies the previous port is also finished or there is a ship currently at the port
                        constraint.add_at_most_one(E, t, ship)
                        E.add_constraint(p >> t | ship)
                        #constraint.add_exactly_one(E, t, ship, ~p)


                
        

        for p in ports:
            #if there is a ship at a time step above the port, either that ship can be true or the unfinished port can be true, but not both 
            if ship.x == p.x and ship.y == p.y and ship.time == p.time+1:
                    for t in ports:
                        if p.x == t.x and p.y == t.y and p.time+1 == t.time:
                            #an unfinished port implies the next port is also unfinished or there is a ship at the next port
                            constraint.add_at_most_one(E, t, ship)
                            E.add_constraint(p >> t | ship)
                            #constraint.add_exactly_one(E, t, ship, ~p)


        #first cargo function
        #this swaps cargo
        for p in ports:
            if ship.x == p.x and ship.y == p.y and ship.time == p.time:
                for c in cargo:
                    if c.time == ship.time-1 and c.type == p.wants_cargo_type:
                        for c1 in cargo:
                            if c1.time == ship.time and c1.type == p.has_cargo_type:
                                #this is an exchange 
                                #no make sense, if those 2 are true port can't be true because all the conditions are fullfilled
                                E.add_constraint((ship & ~p) >> (c1 & c))

        #ship is consistent, if ship is true then whatever it's tiles condition is it's true
        #therefore if ship is not on a port then we imply that cargo is the same
        #we have many ports to consider at any time step, there can be many ports that are true or false
        #there can only be 1 ship at any time instance
        #ships are the key


    for p in ports:
        for t in ports:
            if p.x == t.x and p.y == t.y and p.time == t.time-1:
                for c in cargo:
                    if c.time == t.time and c.type == t.has_cargo_type:
                        E.add_constraint((p&~t) >> c)

    for p in ports:
        for t in ports:
            if p.x == t.x and p.y == t.y and p.time == t.time-1:
                for c in cargo:
                    if c.time == p.time and c.type == t.wants_cargo_type:
                        E.add_constraint((p&~t) >> c)



    for p in ports:
        for t in ports:
            if p.x == t.x and p.y == t.y and p.time+1 == t.time:
                for c in cargo:
                    if c.time == p.time and c.type == p.wants_cargo_type:
                        for c1 in cargo:
                            if c1.time == t.time and c1.type == p.has_cargo_type:
                                #this is an exchange
                                E.add_constraint((c & ~t) >> c1)
                            if c1.time == t.time and c.type == c1.type:
                                #there's overlap with the other ports meaning that c doesn't actually have to imply
                                #if cargo is a thing, then the next cargo is the same or some ports swapped
                                E.add_constraint((c & t) >> (c1))
                                #E.add_constraint((c1 & ~t) >> c)
                                #E.add_constraint((p & t) >> (c & c1))
    
                                

    #something like  E.add_constraint(c & t >> c1)


    #second cargo function
    #if cargo is of a current type it stays the same unless a port is fullfilled and therefore the cargo is changed
    #for p in ports:
    #for t in ports:
        #if p.x == t.x and p.y == t.y and p.time+1 == t.time:
            #for c in cargo:
                #if c.time == p.time:
                    #for c1 in cargo:
                        #if c1.time == t.time and c.type == c1.type:
                            #E.add_constraint(c >> (c1 | (p&~t)))
                            #if c.type == p.wants_cargo_type:
                                #E.add_constraint((p&~t) >> c)
                            

    #p is a port at a time step
    #t is the same port with time +1 
    #c is cargo at p's time step
    #t is cargo at t's time step
    #we need to say if port is not done and then done at the next step then cargo at the initial step must have been the wants 


    

    #it can't handle 2 ports 
    #probably because p&~t hits all ports so there's conflict 




    for t in range(time+1):
        temp_list = []
        for ship in ships:
            if ship.time == t:
                temp_list.append(ship)                

        print()
        print(temp_list)
        print()
        print(t)
        constraint.add_exactly_one(E, *temp_list)



    for t in range(time+1):
        temp_list = []
        for c in cargo:
            if c.time == t:
                temp_list.append(c)

        constraint.add_exactly_one(E, *temp_list)
                    

            #for p in ports:
            #    if ship.x == p.x and ship.y == p.y and ship.time == p.time:
            #        constraint.add_exactly_one(E, p, ship)
            
    #if port is at max time it must be 0,0 that implies it was either touched before or at that turn
    #set the last ports to be unconditonally true since it's our win condition 
    #IT WORKS
    #need to constrain that if it hasn't been touched by ship it CAN'T BE FULLFILLED



    T = E.compile()
    print("\nSatisfiable: %s" % T.satisfiable())
    return T



def print_variables(sol, word, state, time):
    if sol:
        for i in range(time+1):
            for key in sol:
                if word in str(key):
                    if sol.get(key) and key.time == i:
                        print(key, sol.get(key))


def solve(time, scene, MAX):
    a_theory = theory(time, scene, MAX)
    sol = a_theory.solve()
    print_variables(sol, "Ship", True, time)
    print_variables(sol, "Cargo", True, time)
    print_variables(sol, "Port", True, time)
    print("\nSatisfiable: %s" % a_theory.satisfiable())
    print("# Solutions: %d" % count_solutions(a_theory))

    
if __name__ == "__main__":
    time = 3
    S.scenarios(1, 5, Ship(0, 2, 1))
    theory = theory(time, 1, 5)
    sol = theory.solve()
    print_variables(sol, "Ship", True, time)
    print_variables(sol, "Cargo", True, time)
    print_variables(sol, "Port", True, time)
    print("\nSatisfiable: %s" % theory.satisfiable())
    print("# Solutions: %d" % count_solutions(theory))
