def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        depths = [int(line) for line in content]

        sum = 0

        three_depth = depths[0] + depths[1] + depths[2]
        for i in range(depths.__len__()-2):
            new_three_depth = depths[i] + depths[i+1] + depths[i+2]

            if new_three_depth > three_depth:
                sum += 1
            three_depth = new_three_depth

        print(sum)


if __name__ == "__main__":
    main()

