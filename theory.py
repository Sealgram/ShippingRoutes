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
        return f"Cargo{self.time, self.type}"

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
#   Constraints
#
####################################

def ship_creation(MAX, time):
    ships = {}
    for t in range(time+1):
        temp = {}
        for x in range(MAX):
            for y in range(MAX):
                prop = Ship(t, x, y)
                temp.update({(x,y):prop})
        ships.update({t:temp})
    return ships

def cargo_creation(time):
    cargos = {}
    for t in range(time+1):
        temp = {}
        prop = Cargo(t, "Cars")
        temp.update({"Cars":prop})
        prop = Cargo(t, "Produce")
        temp.update({"Produce":prop})
        prop = Cargo(t, "Appliances")
        temp.update({"Appliances":prop})
        cargos.update({t:temp})
    return cargos

def expand_ports(time, scene):
    ports = S.port_creation(scene)
    ports_dict = {}
    for t in range(time+1):
        temp = {}
        for p in ports:
            prop = Port(t, p.x, p.y, p.has_cargo_type, p.wants_cargo_type)
            temp.update({(p.x,p.y):prop})    
        ports_dict.update({t:temp})

    return ports_dict

def theory(time, scene, MAX, start_ship):
    ships = ship_creation(MAX, time)

    prop = start_ship
    E.add_constraint(ships[0][prop.x,prop.y])

    cargo = cargo_creation(time)
    water= S.water_creation(scene)
    land = S.land_creation(scene)
    ports = expand_ports(time, scene)

    #all land is true
    #land implies no ship on that square
    for l in land:
        for t in ships.values():
            ship = t[l.x,l.y]
            E.add_constraint(l)
            E.add_constraint(l >> ~ship)
 
    #this constraint states any given port at any time step can either have it's goods or be finished
    for t in ports.values():
        for p in t.values():
            constraint.add_exactly_one(E, p, Port(p.time, p.x, p.y, 0, 0))

    #makes that ports at the last time step MUST be finished
    for p in ports[time].values():
        E.add_constraint(~p)

    #port at time step 0 must be unfinished
    for p in ports[0].values():
        E.add_constraint(p)

    #atleast one ship must touch every single port within it's trip
    #apparently doesn't do anything currently
    for p in ports[0]:
        lst = []
        for t in ships.values():
            lst.append(t[p])
        constraint.add_at_least_one(E, *lst)
 

    #if a finished port is true then the finished port at the next time step must also be true 
    for t in range(time):
        for p in ports[t].values():
            prop = ports[t+1][(p.x,p.y)]
            # print("if not ", p, " then also not ", prop)
            E.add_constraint(~p >> ~prop)
            # constraint.add_implies_all(E, ~p, ~prop)


        
    #ship can't be beyond the boundary 
    for t in ships.values():
        lst = t.keys()
        for key in lst:
            if key.count(0) > 0 or key.count(MAX-1) > 0:
                prop = t[key]
                E.add_constraint(~prop)


    #if a given ship not at the final time step is true
    #then there must be an adjacent ship at the next time step that is true
    for t in range(time):
        for key in ships[t]:
            if key.count(0) == 0 and key.count(MAX-1) == 0:
                ship = ships[t][key]
                adj_up = ships[t+1][ship.x,ship.y+1]
                adj_down = ships[t+1][ship.x,ship.y-1]
                adj_right = ships[t+1][ship.x+1,ship.y]
                adj_left = ships[t+1][ship.x-1,ship.y]
                E.add_constraint(ship >>  adj_up | adj_down | adj_right | adj_left)

    #if a given ship not at time step 0 is true
    #then there must be an adjacent ship at the previous time step is true 
    #I wonder if this is useless considiring adjacency might be completley enforced by the previous constraints 
    #gonna keep it commented out for now
    # for t in range(1, time+1):
    #     for key in ships[t]:
    #         if key.count(0) == 0 and key.count(MAX-1) == 0:
    #             ship = ships[t][key]
    #             adj_up = ships[t-1][ship.x,ship.y+1]
    #             adj_down = ships[t-1][ship.x,ship.y-1]
    #             adj_right = ships[t-1][ship.x+1,ship.y]
    #             adj_left = ships[t-1][ship.x-1,ship.y]
    #             print(adj_up, " ", adj_down, " ", adj_left, " ", adj_right, " are all adjacent to ", ship)
    #             E.add_constraint(ship >>  adj_up | adj_down | adj_right | adj_left)

    #if a port is finished, either the previous port is also finished or a ship has just touched the port
    for t in ports.values():
        for p in t.values():
            if p.time != 0:
                ship = ships[p.time][p.x,p.y]
                prev_p = ports[p.time-1][p.x,p.y]
                # print("if not ", p, " then not ", prev_p, " or ", ship)
                E.add_constraint(~p >> (~prev_p | ship))

    #if a port is unfinished, either the next port is also unfished or a ship has just touched the next port
    for t in ports.values():
        for p in t.values():
            if p.time != time:
                ship = ships[p.time+1][p.x,p.y]
                next_p = ports[p.time+1][p.x,p.y]
                constraint.add_at_most_one(E, next_p, ship)
                # print("if ", p, " then ", next_p, " or ", ship, " but not both")
                E.add_constraint(p >> next_p | ship)

    #swaps cargo
    #if a ship is on a port and the port is finished. Then the ship must have had the proper cargo and now contains the appropriate cargo
    for t in ports.values():
        for p in t.values():
            if p.time != 0:
                ship = ships[p.time][p.x,p.y]
                curr_cargo = cargo[p.time-1][p.wants_cargo_type]
                next_cargo = cargo[p.time][p.has_cargo_type]
                # print("if ", ship, " and not ", p, " implies the current cargo is ", curr_cargo, " and the next cargo is ", next_cargo)
                E.add_constraint((ship & ~p) >> (curr_cargo & next_cargo))



    for t in ports.values():
        for p in t.values():
            if p.time != 0:
                prev_p = ports[p.time-1][p.x,p.y]
                curr_cargo = cargo[p.time-1][p.wants_cargo_type]
                next_cargo = cargo[p.time][p.has_cargo_type]
                # print("if ", prev_p, " and not ", p, " then cargo must have been ", curr_cargo)
                E.add_constraint((~p&prev_p) >> (curr_cargo & next_cargo))
                # print("if ", prev_p, " and not ", p, " then cargo must currently be ", next_cargo)
                # E.add_constraint((~p&prev_p) >> next_cargo)

    #if ship is on a water tile then cargo must currently be the same as last cargo
    for w in water:
        E.add_constraint(w)
        lst = []
        for t in range(1, time+1):
            ship = ships[t][w.x,w.y]
            lst.append(ship)
            for curr_cargo in cargo[t].values():
                prev_cargo = cargo[t-1][curr_cargo.type]
                E.add_constraint((w & ship & prev_cargo) >> (curr_cargo))


    for t in ships.values():
        ships_at_t = t.values()
        # print("at most one of ", ships_at_t)
        constraint.add_exactly_one(E, *ships_at_t)


    for t in cargo.values():
        cargo_at_t = t.values()
        # print("at most one of ", cargo_at_t)
        constraint.add_exactly_one(E, *cargo_at_t)


    T = E.compile()
    return T



def get_variables(sol, word, time):
    var = []
    if sol:
        for i in range(time+1):
            for key in sol:
                if word in str(key):
                    if sol.get(key) and key.time == i:
                        var.append(key)
                        # print(key, sol.get(key))
    return var


def solve(time, scene, MAX, ship):
    a_theory = theory(time, scene, MAX, ship)
    sol = a_theory.solve()
    valids = []
    valids.append(get_variables(sol, "Ship", time))
    valids.append(get_variables(sol, "Cargo", time))
    valids.append(get_variables(sol, "Port", time))
    print("\nSatisfiable: %s" % a_theory.satisfiable())
    print("# Solutions: %d" % count_solutions(a_theory))
    return valids
