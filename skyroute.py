from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
def skyroute():
    greet()

skyroute()

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
    greet()

skyroute()


def set_start_and_end(start_point, end_point):
    pass

def get_start():
    pass

def get_end():
    pass


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    else:
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b'...")
            return set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point


def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()

def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point

def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point


def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_start()

def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
    if end_point_letter in landmark_choices:
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        return get_end()


print(set_start_and_end(None, None))


def new_route(start_point=None, end_point=None):
    pass

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)


def get_route(start_point, end_point):
    pass

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            # Logic to find the route will go here

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            route = bfs(vc_metro, start_station, end_station)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            route = bfs(vc_metro, start_station, end_station)
            if route:
                routes.append(route)

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            route = bfs(vc_metro, start_station, end_station)
            if route:
                routes.append(route)
    
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route

# Example landmarks: "Marine Building" and "Science World"
print(get_route("Marine Building", "Science World"))

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))

def skyroute():
    greet()
    new_route()

skyroute()

def get_route(start_point, end_point):
    # Add indented block here

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    again = input("Would you like to see another route? Enter y/n: ")


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        new_route(start_point, end_point)

def show_landmarks():
    pass  # This will be implemented later

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)


def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")

def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == "y":
        print(landmark_string)

def goodbye():
    print("Thanks for using SkyRoute!")

def skyroute():
    greet()
    new_route()
    goodbye()

skyroute()

stations_under_construction = []

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    
    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    
    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)

def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    
    if shortest_route:
        shortest_route_string = '\n'.join(shortest_route)
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
    
    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)

def get_active_stations():
    updated_metro = vc_metro.copy()

def get_active_stations():
    updated_metro = vc_metro.copy()
    
    for station_under_construction in stations_under_construction:
        # Logic to remove connections will go here

def get_active_stations():
    updated_metro = vc_metro.copy()
    
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            # Logic to remove connections will go here

def get_active_stations():
    updated_metro = vc_metro.copy()
    
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)

def get_active_stations():
    updated_metro = vc_metro.copy()
    
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])

def get_active_stations():
    updated_metro = vc_metro.copy()
    
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])
    
    return updated_metro

# Example usage
stations_under_construction.append("Burrard")
print(get_active_stations())


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                # Logic to handle possible_route will go here
            
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route

def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            
            if stations_under_construction:
                possible_route = dfs(metro_system, start_station, end_station)
                # Logic to handle possible_route will go here
            
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    
    if routes:
        shortest_route = min(routes, key=len)
        return shortest_route

route = bfs(vc_metro, start_station, end_station)

route = bfs(metro_system, start_station, end_station)

skyroute()

# Other code...

skyroute()
