from collections import Counter


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

    # initialize some variables
    visited = []
    route = []
    routes = []
    origin = 'start'
    final_destination = 'end'

    # Now we can recursively traverse the paths
    find_paths(origin, final_destination, visited, route, paths, routes)

    print(len(routes))


def find_paths(origin, final_destination, visited, route, paths, routes):
    route.append(origin)
    visited.append(origin)
    origin_end = None
    if len(origin.split(',')) > 1:
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
    visited.remove(origin)


def visited_before(destinations, visited_destinations):
    possible_destinations = []
    visited_destinations = visited_destinations.copy()

    # check if single small caves has already been visited twice
    double_visit = False
    count = Counter(visited_destinations)

    # Check for double occurrences of the same node
    if sum(count.values()) > count.values().__len__():
        double_visit = True

    else:
        for visited_dest in visited_destinations:
            if len(visited_dest.split(',')) > 1:
                visited_destinations.append(visited_dest.split(',')[1])
                count = Counter(visited_destinations)
                if sum(count.values()) > len(set(visited_destinations)):
                    double_visit = True
                    break

    for destination in destinations:
        if destination.__contains__(','):
            destination_visited = destination.split(',')[1]
        else:
            destination_visited = destination
        visited = False

        for v in visited_destinations:
            if v.__contains__(','):
                v = v.split(',')[1]
            if destination_visited == v:
                if double_visit or destination_visited == "start":
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
