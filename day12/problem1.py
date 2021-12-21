import random


class Path:
    def __init__(self, town, destination):
        self.origin = town
        self.destinations = {destination}

    def add_destination(self, destination):
        self.destinations.add(destination)


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        paths = {}
        line_arr = [line.strip() for line in content]
        for line in line_arr:
            towns = line.split('-')
            if not towns[0] in paths:
                paths[towns[0]] = Path(town=towns[0], destination=towns[1])
            else:
                paths[towns[0]].add_destination(towns[1])
            if not towns[1] in paths:
                paths[towns[1]] = Path(town=towns[1], destination=towns[0])
            else:
                paths[towns[1]].add_destination(towns[0])

    routes = set()
    i = 0
    route = 'start'
    visited = []
    destination = 'start'

    while i < 100000000:
        origin = destination
        if origin.islower():
            visited.append(origin)

        path = paths[origin]
        destinations = list(path.destinations)
        destinations = list(filter(lambda x: x not in visited, destinations))

        if not destinations:
            route = 'start'
            destination = 'start'
            visited = []
            i += 1
            continue

        destination = random.choice(destinations)

        route += ', ' + destination

        if destination == 'end':
            routes.add(route)
            route = 'start'
            destination = 'start'
            visited = []
        i += 1
        if i % 1000000 == 0:
            print(len(routes))

    print(len(routes))


if __name__ == "__main__":
    main()

"""

#### ----- HOW I SHOULD HAVE DONE THIS ---- ####

class Path:
    def __init__(self, town, destination):
        self.origin = town
        self.destinations = {destination}

    def add_destination(self, destination):
        self.destinations.add(destination)


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

        paths = {}
        line_arr = [line.strip() for line in content]

    # First create all paths given in the input
    for line in line_arr:
        towns = line.split('-')
        paths = create_path(towns[0], towns[1], paths)
        paths = create_path(towns[1], towns[0], paths)

    # Then we dissolve the big caves in combined paths to smaller caves, so we can mark them as visited
    for k,v in paths.items():
        big_caves = list(filter(lambda x: x.isupper(), v.destinations))
        for cave in big_caves:
            v.destinations.remove(cave)
            for c in paths[cave].destinations:
                v.destinations.add(c)

    # Now we can easily and recursively traverse the paths

    visited = []
    route = []
    routes = []
    origin = 'start'
    final_destination = 'end'

    find_paths(origin, final_destination, visited, route, paths, routes)

    print(len(routes))

def find_paths(origin, final_destination, visited, route, paths, routes):
    route.append(origin)
    visited.append(origin)
    origin_end = None
    if len(origin.split(',')) > 1:
        visited.append(origin.split(',')[1])
        origin_end = origin.split(',')[1]

    if origin.endswith(final_destination):
        routes.append(route.copy())
    else:
        if origin_end:
            destinations = visited_before(paths[origin_end].destinations, visited)
        else:
            destinations = visited_before(paths[origin].destinations, visited)
        for d in destinations:
            find_paths(d, final_destination, visited, route, paths, routes)
    route.pop()
    if origin_end:
        visited.remove(origin_end)
    visited.remove(origin)


def visited_before(destinations, visited_destinations):
    possible_destinations = []

    for destination in destinations:
        visited = False
        for v in visited_destinations:
            if destination.endswith(v):
                visited = True
                break
        if not visited:
            possible_destinations.append(destination)
    return possible_destinations


def create_path(origin, destination, paths):
    if origin not in paths:
        if origin.isupper():
            paths[origin] = Path(town=origin, destination=origin + ',' + destination)
        else:
            paths[origin] = Path(town=origin, destination=destination)
    else:
        if origin.isupper():
            paths[origin].add_destination(origin + ',' + destination)
        else:
            paths[origin].add_destination(destination)
    return paths


if __name__ == "__main__":
    main()

"""