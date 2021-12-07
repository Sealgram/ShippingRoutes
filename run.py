import scenarios as S 
import theory as T 

def start_ship(scene):
    ship = T.Ship(0, 0, 0)
    if scene == 1:
        ship = T.Ship(0, 2, 1)
    if scene == 2:
        ship = T.Ship(0, 2, 1)
    if scene == 3:
        ship = T.Ship(0, 2, 1)
    if scene == 4:
        ship = T.Ship(0, 6, 1)
    if scene == 5:
        ship = T.Ship(0, 5, 5)
    return ship


def print_scenarios(pv):
    if pv == 1 or pv == 6:
        print("Scenario 1:")
        S.scenarios(1, 5, start_ship(1))
    if pv == 2 or pv == 6:
        print("\nScenario 2:")
        S.scenarios(2, 5, start_ship(2))
    if pv == 3 or pv == 6:
        print("\nScenario 3:")
        S.scenarios(3, 6, start_ship(2))
    if pv == 4 or pv == 6:
        print("\nScenario 4:")
        S.scenarios(4, 9, start_ship(4))
    if pv == 5 or pv == 6:
        print("\nScenario 5:")
        S.scenarios(4, 9, start_ship(5))


if __name__ == "__main__":
    print("CISC 204 Modelling Project: Shipping Routes\nAnton Gudonis\nDallin Whitford\nAidan Wolf\nLiam Seagram\n\n")
    print("Here are the five scenarios that we can test:\n")
    print_scenarios(6)
    scene = 0
    time = 0
    print("\n\nNow, we will begin testing the model.\n\n")
    while True:
        try:
            scene = int(input("\nEnter the number of the scene you would like to use: "))
            if scene > 0 and scene < 6:
                break
            else:
                print("\nInvalid input. Enter an integer between 1 and 5.")
        except:
            print("\nNot an integer. Enter an integer between 1 and 5.")

    while True:
        try:
            time = int(input("\nEnter the time you would like the program to solve within: "))
            if time > 2 and time < 51:
                break
            else:
                print("\nInvalid input. Enter an integer between 2 and 51.")
        except:
            print("\nNot an integer. Enter an integer between 2 and 51.")

    MAX = 0
    if scene == 1 or scene == 2:
        MAX = 5
    if scene == 3:
        MAX = 6
    if scene == 4 or scene == 5:
        MAX = 9

    print(f"\nScenario {scene} will be attempted to be solved with time {time}.\n")
    print_scenarios(scene)
    print()
    T.solve(time, scene, MAX)
