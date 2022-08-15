from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices


landmarks_string = ""
for cha, landmark in landmark_choices.items():
    landmarks_string += cha + " - " + landmark + "\n"

#stations_under_construction = []
stations_under_construction = ['Burrard', 'Marine Drive']


# Define greet() function
def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks: \n" + landmarks_string)


# Getting Start- and Endstation

def get_start():
    start_point_letter = input(
        "Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter not in landmark_choices:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()
    else:
        start_point = landmark_choices[start_point_letter]
        return start_point


def get_end():
    end_point_letter = input(
        "Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()


def set_start_and_end(start_point, end_point):
    if start_point:
        change_point = input(
            "What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

        if change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        elif change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd' or 'b'...")
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    routes = []

    for start_station in start_stations:
        for end_station in end_stations:
            if stations_under_construction:
                metro_system = get_active_stations()
            else:
                metro_system = vc_metro
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    return None
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)

    return min(routes, key=len)


def show_landmarks():
    list_show = input(
        "Would you like to see the list of landmarks again? Enter y/n: ")
    if list_show == 'y':
        print(landmarks_string)


def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for station in vc_metro:
            if station == station_under_construction:
                updated_metro[station] = set([])
            else:
                updated_metro[station] -= set(station_under_construction)
    return updated_metro


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    if shortest_route:
        shortest_route_string = '--> '.join(shortest_route)
        print("The shortest metro route from {0} to {1} is : ".format(
            start_point, end_point))
        print(shortest_route_string)
        again = input("Would you like to see another route? Enter y/n: ")
        if again == 'y':
            show_landmarks()
            new_route(start_point, end_point)
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintaince".format(
            start_point, end_point))


def goodbye():
    print("Thanks for using SkyRoute!")


def skyroute():
    greet()
    new_route()
    goodbye()


skyroute()
