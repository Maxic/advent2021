def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line for line in content]
        print(line_arr)


if __name__ == "__main__":
    main()

