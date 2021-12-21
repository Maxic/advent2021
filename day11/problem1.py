def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()
        grid = [list(map(lambda x: int(x), line.strip())) for line in content]

    flash_counter = 0
    for _ in range(100):
        flash_counter, grid = step(flash_counter, grid)

    print(flash_counter)


def step(flash_counter, grid):

    # First, the energy level of each octopus increases by 1.
    grid = [list(map(lambda x: x + 1, row)) for row in grid]

    # Then, any octopus with an energy level greater than 9 flashes.
    # This increases the energy level of all adjacent octopuses by 1,
    # including octopuses that are diagonally adjacent.
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # (An octopus can only flash at most once per step.)
    x, y = 0, 0
    while y < len(grid):
        if grid[y][x] >= 10:
            flash_counter += 1
            grid = flash((y, x), grid)
            x, y = 0, 0
            continue
        x += 1
        if x % len(grid[0]) == 0:
            x = 0
            y += 1

    return flash_counter, grid


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

