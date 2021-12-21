def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()
        grid = [list(map(lambda x: int(x), line.strip())) for line in content]

    for i in range(1, 1000):
        grid = step(grid)

        if sum([sum(row) for row in grid]) == 0:
            print(i)
            break


def step(grid):

    grid = [list(map(lambda x: x + 1, row)) for row in grid]

    x, y = 0, 0
    while y < len(grid):
        if grid[y][x] >= 10:
            grid = flash((y, x), grid)
            x, y = 0, 0
            continue
        x += 1
        if x % len(grid[0]) == 0:
            x = 0
            y += 1

    return grid


def flash(pos, grid):
    grid[pos[0]][pos[1]] = 0

    for n_pos in get_neighbours(pos, grid):
        if grid[n_pos[0]][n_pos[1]] != 0:
            grid[n_pos[0]][n_pos[1]] += 1
    return grid


def get_neighbours(pos, grid):
    available_neighbours = []
    neighbour_positions = {(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)}
    for neighbour_pos in neighbour_positions:
        y = pos[0] + neighbour_pos[0]
        x = pos[1] + neighbour_pos[1]
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            available_neighbours.append((y, x))
    return available_neighbours


if __name__ == "__main__":
    main()

