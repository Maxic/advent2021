def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        counter = 0
        line_arr = [line.split('|')[1].strip('\n').split() for line in content]
        for line in line_arr:
            for digit in line:
                if digit.__len__() in [2, 3, 4, 7]:
                    counter += 1

        print(counter)


if __name__ == "__main__":
    main()

