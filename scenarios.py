import pprint
from tabulate import tabulate
import theory as T

####################################
#
#   Making the Map
#
####################################

# Function that creates all of the land on the map for each scenario, taking in the scene it is creating land for as a parameter.
def land_creation(scene):
    if scene == 1:
        l_y0 = []
        l_y1 = []
        l_y2 = []
        l_y3 = []
        l_y4 = []
        l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4]
    if scene == 2:
        l_y0 = []
        l_y1 = []
        l_y2 = [2]
        l_y3 = []
        l_y4 = []
        l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4]
    if scene == 3:
        l_y0 = []
        l_y1 = []
        l_y2 = [2, 4]
        l_y3 = [1]
        l_y4 = [1]
        l_y5 = []
        l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4, l_y5]
    if scene == 4:
        l_y0 = []
        l_y1 = [7]
        l_y2 = [7]
        l_y3 = [4]
        l_y4 = [3, 4, 5]
        l_y5 = [3, 4]
        l_y6 = [1]
        l_y7 = [1, 2]
        l_y8 = []
        l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4, l_y5, l_y6, l_y7, l_y8]
    if scene == 5:
        l_y0 = []
        l_y1 = [1, 2, 7]
        l_y2 = [1, 7]
        l_y3 = [3, 4]
        l_y4 = [3, 4, 5]
        l_y5 = [2, 3, 4, 5]
        l_y6 = [3, 5]
        l_y7 = []
        l_y8 = []
        l_yall = [l_y0, l_y1, l_y2, l_y3, l_y4, l_y5, l_y6, l_y7, l_y8]
    # the specific scenario's land objects will be stored in a list
    land = []
    # initialize all land on map
    for y in range(len(l_yall)):
        for x in range(len(l_yall[y])):
            prop = T.Land(l_yall[y][x], y)
            land.append(prop)
    return land

# Function that creates all of the water on the map for each scenario, taking in the scene it is creating water for as a parameter.
def water_creation(scene):
    if scene == 1:
        w_y0 = []
        w_y1 = [1, 2, 3]
        w_y2 = [1, 2, 3]
        w_y3 = [1, 3]
        w_y4 = []
        w_yall =[w_y0, w_y1, w_y2, w_y3, w_y4]
    if scene == 2:
        w_y0 = []
        w_y1 = [1, 2, 3]
        w_y2 = [1, 3]
        w_y3 = [1, 3]
        w_y4 = []
        w_yall =[w_y0, w_y1, w_y2, w_y3, w_y4]
    if scene == 3:
        w_y0 = []
        w_y1 = [1, 2, 3, 4]
        w_y2 = [1, 3]
        w_y3 = [3, 4]
        w_y4 = [2, 3]
        w_y5 = []
        w_yall =[w_y0, w_y1, w_y2, w_y3, w_y4, w_y5]
    if scene == 4:
        w_y0 = []
        w_y1 = [2, 3, 4, 5, 6]
        w_y2 = [1, 2, 3, 4, 5, 6]
        w_y3 = [1, 2, 3, 5, 6, 7]
        w_y4 = [2, 6, 7]
        w_y5 = [1, 2, 5, 6, 7]
        w_y6 = [2, 3, 4, 5, 6, 7]
        w_y7 = [3, 4, 5, 6]
        w_y8 = []
        w_yall = [w_y0, w_y1, w_y2, w_y3, w_y4, w_y5, w_y6, w_y7, w_y8]
    if scene == 5:
        w_y0 = []
        w_y1 = [3, 4, 5, 6]
        w_y2 = [3, 4, 5, 6]
        w_y3 = [1, 2, 5, 6]
        w_y4 = [1, 2, 6, 7]
        w_y5 = [1, 6, 7]
        w_y6 = [1, 2, 6, 7]
        w_y7 = [1, 2, 3, 4, 5, 6]
        w_y8 = []
        w_yall = [w_y0, w_y1, w_y2, w_y3, w_y4, w_y5, w_y6, w_y7, w_y8]
    # the specific scenarios water objects will be stored in a list
    water = []
    # initialize all water on map
    for y in range(len(w_yall)):
        for x in range(len(w_yall[y])):
            prop = T.Water(w_yall[y][x], y)
            water.append(prop)
    return water

# Function that creates all of the ports on the map for each scenario, taking in the scene it is creating ports for as a parameter.
def port_creation(scene):
    # the specific scenario's port objects will be stored in a list
    ports = []
    if scene == 1:
        prop = T.Port(0, 2, 3, "Cars", "Produce")
        ports.append(prop)
    if scene == 2:
        prop = T.Port(0, 2, 3, "Cars", "Produce")
        ports.append(prop)
    if scene == 3:
        prop = T.Port(0, 2, 3, "Cars", "Produce")
        ports.append(prop)
        prop = T.Port(0, 4, 4, "Appliances", "Cars")
        ports.append(prop)
    if scene == 4:
        prop = T.Port(0, 1, 1, "Cars", "Produce")
        ports.append(prop)
        prop = T.Port(0, 1, 4, "Appliances", "Cars")
        ports.append(prop)
        prop = T.Port(0, 7, 7, "Produce", "Appliances")
        ports.append(prop)
    if scene == 5:
        prop = T.Port(0, 2, 2, "Cars", "Produce")
        ports.append(prop)
        prop = T.Port(0, 7, 3, "Appliances", "Cars")
        ports.append(prop)
        prop = T.Port(0, 4, 6, "Produce", "Appliances")
        ports.append(prop)
        prop = T.Port(0, 7, 7, "Produce", "Appliances")
        ports.append(prop)
    return ports

# function that takes in the scene that is being created as a parameter, as well as the maximum size of the map, and generates a list that represents the entire map
def map_creation(MAX, scene):
    map = [[0 for x in range(MAX)] for y in range(MAX)]
    land = land_creation(scene)
    for i in range(len(land)):
        map[land[i].x][land[i].y] = "L"

    water = water_creation(scene)
    for i in range(len(water)):
        map[water[i].x][water[i].y] = "-"

    ports = port_creation(scene)
    for i in range(len(ports)):
        map[ports[i].x][ports[i].y] = "P"
    return map

# function that prints out a visual representation of the specific scene making use of tabulate
def visual(MAX, scene, ship):
    visual = map_creation(MAX, scene)
    visual[ship.x][ship.y] = "S"
    MAX -= 1
    if scene == 1 or scene == 2:
        table = [[visual[x][1] for x in range(1, MAX)], [visual[x][2] for x in range(1, MAX)],
                [visual[x][3] for x in range(1, MAX)]]
    if scene == 3:
        table = [[visual[x][1] for x in range(1, MAX)], [visual[x][2] for x in range(1, MAX)], 
                [visual[x][3] for x in range(1, MAX)], [visual[x][4] for x in range(1, MAX)]]
    if scene == 4 or scene == 5:
        table = [[visual[x][1] for x in range(1, MAX)], [visual[x][2] for x in range(1, MAX)], 
                [visual[x][3] for x in range(1, MAX)], [visual[x][4] for x in range(1, MAX)], 
                [visual[x][5] for x in range(1, MAX)], [visual[x][6] for x in range(1, MAX)], 
                [visual[x][7] for x in range(1, MAX)]]
    MAX += 1
    print()
    print(tabulate(table, tablefmt="fancy_grid"))

# function that prints out each specific scenario, using the function 'visual'.
def scenarios(scene, MAX, ship):
    if scene == 1:
        # MAX must be 5
        visual(MAX, scene, ship)
    if scene == 2:
        # MAX must be 5
        visual(MAX, scene, ship)
    if scene == 3:
        # MAX must be 6
        visual(MAX, scene, ship)
    if scene == 4:
        # MAX must be 9
        visual(MAX, scene, ship)
    if scene == 5:
        # MAX must be 9
        visual(MAX, scene, ship)


if __name__ == "__main__":
    print("Scenario 1:")
    S.scenarios(1, 5, T.Ship(0, 2, 1))
    print("\nScenario 2:")
    S.scenarios(2, 5, T.Ship(0, 2, 1))
    print("\nScenario 3:")
    S.scenarios(3, 6, T.Ship(0, 2, 1))
    print("\nScenario 4:")
    S.scenarios(4, 9, T.Ship(0, 6, 1))
    print("\nScenario 5:")
    S.scenarios(5, 9, T.Ship(0, 5, 5))