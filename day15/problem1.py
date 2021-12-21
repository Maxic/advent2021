from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

        matrix = [list(map(lambda x: int(x), line.strip())) for line in content]
        grid = Grid(matrix=matrix )
        start = grid.node(0, 0)
        end = grid.node(len(matrix)-1, len(matrix[0])-1)

        finder = AStarFinder()
        path, runs = finder.find_path(start, end, grid)

        risk = 0
        for pos in path[1:]:
            x, y = pos
            risk += matrix[y][x]

        print(grid.grid_str(path=path, start=start, end=end))
        print(risk)

        # routes = []
        # find_paths([], [], (0, 0), 0, routes, grid)
        # print(min([sum(route) for route in routes]))


# def find_paths(route, visited, pos, risk, routes, grid):
#     route.append(pos)
#     visited.append(pos)
#
#     x, y = pos
#     if x != len(grid[0]) - 1 and y != len(grid) - 1:
#         paths = possible_paths(grid, pos, visited)
#         for path, risk in paths:
#             find_paths(route, visited, path, risk, routes, grid)
#     else:
#         routes.append(route.copy())
#
#     route.pop()
#     visited.pop()
#
#
# def possible_paths(grid, pos, visited):
#     possible_path_arr = []
#
#     for neighbour in get_neighbours(pos, grid):
#         if neighbour not in visited:
#             y, x = neighbour
#             risk = int(grid[y][x])
#             possible_path_arr.append((neighbour, risk))
#     return possible_path_arr
#
#
# def get_neighbours(pos, grid):
#     available_neighbours = []
#     neighbour_positions = {(0, 1), (-1, 0), (1, 0), (0, -1)}
#
#     for neighbour_pos in neighbour_positions:
#         y, x = pos
#         n_y, n_x = neighbour_pos
#         y += n_y
#         x += n_x
#         if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
#             available_neighbours.append((y, x))
#     return available_neighbours
#

if __name__ == "__main__":
    main()
