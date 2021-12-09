def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        grid = [line.strip('\n') for line in content]

        low_points = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                val = int(val)
                n = int(grid[y-1][x]) if y-1 >= 0 else 100
                s = int(grid[y+1][x]) if y+1 < grid.__len__() else 100
                e = int(grid[y][x-1]) if x-1 >= 0 else 100
                w = int(grid[y][x+1]) if x+1 < row.__len__() else 100

                if val < n and val < s and val < e and val < w:
                    low_points.append(val+1)

        print(sum(low_points))


if __name__ == "__main__":
    main()

