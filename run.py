import theory as T
import scenarios as S

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


def print_scenarios():
    print("Scenario 1:")
    S.scenarios(1, 5, start_ship(1))
    print("\nScenario 2:")
    S.scenarios(2, 5, start_ship(2))
    print("\nScenario 3:")
    S.scenarios(3, 6, start_ship(3))
    print("\nScenario 4:")
    S.scenarios(4, 9, start_ship(4))
    print("\nScenario 5:")
    S.scenarios(4, 9, start_ship(5))


if __name__ == "__main__":
    print("\nGroup 26 Modelling Project: Shipping Routes\n")
    print("\nAnton Gudonis\nDallin Whitford\nAidan Wolf\nLiam Seagram\n\n")
    print("Here are the five scenarios that we are working with:\n")
    print_scenarios()
    scene = 0
    time = 0
    while True:
        try:
            scene = int(input("\nEnter the scenario that you would like to test on: "))
            if scene > 0 and scene < 6:
                break
            else:
                print("\nNot a valid scene. Enter an integer between 1 and 5.")
        except:
            print("\nNot an integer. Enter an integer between 1 and 5.")
    while True:
        try:
            time = int(input("\nEnter the time step for which you would like to test the scenario: "))
            if time > 2 and time < 50:
                break
            else:
                print("\nNot a valid time. Enter an integer between 1 and 50.")
        except:
            print("\nNot an integer. Enter an integer between 1 and 50.")
    
    MAX = 0
    if scene == 1 or scene == 2:
        MAX = 5
    elif scene == 3:
        MAX = 6
    elif scene == 4 or scene == 5:
        MAX = 9
    
    print(f"Attempting to solve the model with scenario {scene} and time {time}.\n")
    T.solve(time, scene, MAX)
    print()