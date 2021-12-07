class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [list(map(lambda x: x.split(','), line.strip('\n').split(' -> '))) for line in content]

        non_diagonal_lines = []
        grid = [[0 for _ in range(1000)] for _ in range(1000)]

        # remove diagonal lines
        for line in line_arr:
            start = line[0]
            end = line[1]

            if start[0] == end[0] or start[1] == end[1]:
                non_diagonal_lines.append([Vector2(int(start[0]), int(start[1])), Vector2(int(end[0]), int(end[1]))])

        for line in non_diagonal_lines:
            draw_line(line, grid)

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
    if start.x == end.x:
        if start.y < end.y:
            for i in range(start.y, end.y+1):
                grid[i][start.x] += 1
        else:
            for i in range(end.y, start.y+1):
                grid[i][start.x] += 1

    return grid


def print_grid(grid):
    [print(x) for x in grid]


if __name__ == "__main__":
    main()

