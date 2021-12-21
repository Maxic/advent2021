from collections import Counter


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip() for line in content]
        empty_line = line_arr.index('')

        dots = []
        instructions = []

        # Get dots, fold instruction
        for i, val in enumerate(line_arr):
            if i < empty_line:
                x, y = list(map(lambda x: int(x), val.split(',')))
                dots.append((x, y))
            if i > empty_line:
                instructions.append(val)

        for instruction in instructions:
            dots = do_fold(instruction, dots)

        # Get grid size
        max_x = 0
        max_y = 0
        for dot in dots:
            x, y = dot
            if x > max_x: max_x = x
            if y > max_y: max_y = y

        grid = [['.' for _ in range(max_x+1)] for j in range(max_y+1)]
        for dot in dots:
            x, y = dot
            grid[y][x] = '#'

        [print(row) for row in grid]


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

