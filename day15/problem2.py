from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()

        matrix = [list(map(lambda x: int(x), line.strip())) for line in content]
        [[8]]
        extended_matrix = [['_' for _ in range(len(matrix[0])*5)] for _ in range(len(matrix)*5)]

        # Extend rows
        for y, row in enumerate(matrix):
            for x, risk in enumerate(row):
                for i in range(5):
                    # extend row
                    extended_matrix[y][x+(len(row)*i)] = risk+i if risk+i < 10 else (risk+i) % 10+1

        # Extend columns
        for y in range(len(matrix)):
            for x, risk in enumerate(extended_matrix[y]):
                for i in range(5):
                    # extend row
                    extended_matrix[y+(len(row)*i)][x] = risk+i if risk+i < 10 else (risk+i) % 10+1

        grid = Grid(matrix=extended_matrix)
        start = grid.node(0, 0)
        end = grid.node(len(extended_matrix) - 1, len(extended_matrix[0]) - 1)

        finder = DijkstraFinder()
        path, runs = finder.find_path(start, end, grid)

        risk = 0
        for pos in path[1:]:
            x, y = pos
            risk += extended_matrix[y][x]
        print(risk)


if __name__ == "__main__":
    main()
