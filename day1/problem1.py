def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        depths = [int(line) for line in content]

        sum = 0

        depth = depths[0]
        for new_depth in depths:
            if new_depth > depth:
                sum += 1
            depth = new_depth

        print(sum)


if __name__ == "__main__":
    main()

