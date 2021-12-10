open_b = ['(', '<', '{', '[']
close_b = [')', '>', '}', ']']


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip('\n') for line in content]

        corrupted_chars = []

        for line in line_arr:
            corrupted_chars.append(find_corrupt_char(line))

        syntax_err_score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
            None: 0
        }

        score_arr = [syntax_err_score[x] for x in corrupted_chars]
        print(sum(score_arr))


def find_corrupt_char(line):
    brackets = []
    for char in line:
        if char in open_b:
            brackets.append(char)
        elif char in close_b:
            if brackets[-1] == get_open_bracket(char):
                brackets.pop(-1)
            else:
                return char


def get_open_bracket(closing_bracket):
    return open_b[close_b.index(closing_bracket)]




if __name__ == "__main__":
    main()

