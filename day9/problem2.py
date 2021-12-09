from collections import Counter


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        grid = [list(line.strip('\n')) for line in content]

        low_points = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                val = int(val)
                n = int(grid[y-1][x]) if y-1 >= 0 else 100
                s = int(grid[y+1][x]) if y+1 < grid.__len__() else 100
                e = int(grid[y][x-1]) if x-1 >= 0 else 100
                w = int(grid[y][x+1]) if x+1 < row.__len__() else 100

                if val < n and val < s and val < e and val < w:
                    low_points.append((y, x))

        for i, low_point in enumerate(low_points):
            basin_index = 'b' + str(i)
            fill_basin(low_point, basin_index, grid)

        basins = Counter(sum(grid, []))
        basins['9'] = 0
        basins_sorted = sorted(basins.values(), reverse=True)
        print(basins_sorted[0]*basins_sorted[1]*basins_sorted[2])


def fill_basin(low_point, basin_i, grid):
    unmarked_basin = [low_point]
    row = grid[0]

    while len(unmarked_basin) != 0:
        point = unmarked_basin.pop(0)
        y = point[0]
        x = point[1]

        # first mark self as basin index
        grid[y][x] = basin_i

        n = (y - 1, x) if y - 1 >= 0 and grid[y-1][x] != '9' and grid[y-1][x] != basin_i else None
        s = (y + 1, x) if y + 1 < grid.__len__() and grid[y + 1][x] != '9' and grid[y + 1][x] != basin_i else None
        e = (y, x - 1) if x - 1 >= 0 and grid[y][x-1] != '9' and grid[y][x-1] != basin_i else None
        w = (y, x + 1) if x + 1 < row.__len__() and grid[y][x+1] != '9' and grid[y][x+1] != basin_i else None
        if n: unmarked_basin.append(n)
        if s: unmarked_basin.append(s)
        if e: unmarked_basin.append(e)
        if w: unmarked_basin.append(w)


if __name__ == "__main__":
    main()

