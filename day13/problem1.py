from collections import Counter


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip() for line in content]
        empty_line = line_arr.index('')

        dots = []
        instructions = []
        max_x = 0
        max_y = 0

        # Get dots, fold instruction, and grid size
        for i, val in enumerate(line_arr):
            if i < empty_line:
                x, y = list(map(lambda x: int(x), val.split(',')))
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                dots.append((x, y))
            if i > empty_line:
                instructions.append(val)

        # Initialize grid to proper size
        grid = [['.' for i in range(max_x+1)] for j in range(max_y+1)]

        # Fill grid with dots
        for dot in dots:
            x, y = dot
            grid[y][x] = '#'

        dots = do_fold(instructions[0], dots)

        grid = [['.' for i in range(max_x+1)] for j in range(max_y+1)]

        for dot in dots:
            x, y = dot
            grid[y][x] = '#'

        count = 0
        for row in grid:
            bincount = Counter(row)
            count += bincount['#']
        print(count)


def do_fold(instruction, dots):
    new_dots = dots.copy()
    alignment, fold_i = instruction.split('=')
    fold_i = int(fold_i)
    if alignment[-1] == 'y':
        alignment = 'horizontal'
    else:
        alignment = 'vertical'

    if alignment == 'horizontal':
        for i, dot in enumerate(dots):
            x, y = dot
            if y > fold_i:
                displacement = ((y - fold_i)*2)
                new_dots[i] = (x, y-displacement)
    elif alignment == 'vertical':
        for i, dot in enumerate(dots):
            x, y = dot
            if x > fold_i:
                displacement = ((x - fold_i)*2)
                new_dots[i] = (x-displacement, y)
    return new_dots


if __name__ == "__main__":
    main()

