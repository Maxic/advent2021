class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [list(map(lambda x: x.split(','), line.strip('\n').split(' -> '))) for line in content]

        lines = []
        grid = [[0 for _ in range(1000)] for _ in range(1000)]

        # use vectors
        for line in line_arr:
            start = line[0]
            end = line[1]
            lines.append([Vector2(int(start[0]), int(start[1])), Vector2(int(end[0]), int(end[1]))])

        for line in lines:
            draw_line(line, grid)

        print_grid(grid)

        overlap_count = 0
        for row in grid:
            for pos in row:
                if pos > 1:
                    overlap_count += 1
        print(overlap_count)


def draw_line(line, grid):
    start = line[0]
    end = line[1]

    # horizontal
    if start.y == end.y:
        if start.x < end.x:
            for i in range(start.x, end.x+1):
                grid[start.y][i] += 1
        else:
            for i in range(end.x, start.x+1):
                grid[start.y][i] += 1
    # vertical
    elif start.x == end.x:
        if start.y < end.y:
            for i in range(start.y, end.y+1):
                grid[i][start.x] += 1
        else:
            for i in range(end.y, start.y+1):
                grid[i][start.x] += 1
    else:
        if start.x > end.x:
            x_arr = range(start.x, end.x-1, -1)
        else:
            x_arr = range(start.x, end.x+1)
        if start.y > end.y:
            y_arr = range(start.y, end.y - 1, -1)
        else:
            y_arr = range(start.y, end.y + 1)

        for i in range(x_arr.__len__()):
            grid[y_arr[i]][x_arr[i]] += 1
    return grid


def print_grid(grid):
    [print(x) for x in grid]


if __name__ == "__main__":
    main()

