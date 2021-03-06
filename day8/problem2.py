def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        signal_list = [line.split('|')[0].split() for line in content]
        outputs = [line.split('|')[1].strip('\n').split() for line in content]

        decoded_strings = []

        for i, signal_patterns in enumerate(signal_list):
            decode = [""] * 10

            decode[1] = next(filter(lambda x: len(x) == 2, signal_patterns))
            decode[4] = next(filter(lambda x: len(x) == 4, signal_patterns))
            decode[7] = next(filter(lambda x: len(x) == 3, signal_patterns))
            decode[8] = next(filter(lambda x: len(x) == 7, signal_patterns))

            # decode all strings of length 5
            signal_len_5 = list(filter(lambda x: len(x) == 5, signal_patterns))

            # if all letters from 1 occur, it's number 3
            decode[3] = next(filter(lambda x:
                                    count_common_char(x, decode[1]) == 2,
                                    signal_len_5))
            signal_len_5.remove(decode[3])

            # if 3 letters from 4 occur in a string, it's number 5
            decode[5] = next(filter(lambda x:
                                    count_common_char(x, decode[4]) == 3,
                                    signal_len_5))
            signal_len_5.remove(decode[5])

            # Remaining is 2
            decode[2] = signal_len_5[0]

            # decode all strings of length 5
            signal_len_6 = list(filter(lambda x: len(x) == 6, signal_patterns))

            # if NOT all letters from 1 occur, it's number 6
            decode[6] = next(filter(lambda x:
                                    count_common_char(x, decode[1]) != 2,
                                    signal_len_6))
            signal_len_6.remove(decode[6])

            # if all letters from 4 occur, it's number 9
            decode[9] = next(filter(lambda x:
                                    count_common_char(x, decode[4]) == 4,
                                    signal_len_6))
            signal_len_6.remove(decode[9])

            # Remaining is 0
            decode[0] = signal_len_6[0]

            decoded_strings.append(decode)

    results = []
    for i, output in enumerate(outputs):
        value = ""
        for digit in output:
            for j, d in enumerate(decoded_strings[i]):
                if sorted(digit) == sorted(d):
                    value += str(j)
                    break
        results.append(value)

    print(sum([int(x) for x in results]))


def count_common_char(string1, string2):
    return sum(min(string1.count(char), string2.count(char)) for char in (set(string1) & set(string2)))


if __name__ == "__main__":
    main()

