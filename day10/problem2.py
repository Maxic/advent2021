open_b = ['(', '<', '{', '[']
close_b = [')', '>', '}', ']']


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip('\n') for line in content]

        corrupted_chars = []

        for line in line_arr:
            corrupted_chars.append(find_corrupt_char(line))

        incomplete_lines = []
        for i in range(len(line_arr)):
            if corrupted_chars[i] == None:
                incomplete_lines.append(line_arr[i])


        completion_strings = []
        for line in incomplete_lines:
            completion_string = find_open_brackets(line)
            completion_string.reverse()
            completion_strings.append(completion_string)

        print(score(completion_strings))


def score(completion_strings):
    completion_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    scores = []
    for completion_string in completion_strings:
        score = 0
        for char in completion_string:
            score *= 5
            score += completion_score[char]
        scores.append(score)
    scores = sorted(scores)
    middle = float(len(scores)) / 2
    return scores[int(middle - .5)]


def find_open_brackets(line):
    brackets = []
    for char in line:
        if char in open_b:
            brackets.append(char)
        elif char in close_b:
            if brackets[-1] == get_open_bracket(char):
                brackets.pop(-1)
    closing_brackets = []
    for b in brackets:
        closing_brackets.append(get_closing_bracket(b))
    return closing_brackets


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


def get_closing_bracket(open_bracket):
    return close_b[open_b.index(open_bracket)]


if __name__ == "__main__":
    main()

