def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        content = [line.strip('\n') for line in content]

        depth = 0
        pos = 0

        for line in content:
            instruction = {'dir': line.split(' ')[0], 'amount': int(line.split(' ')[1])}

            if instruction['dir'] == 'forward':
                pos += instruction['amount']
            if instruction['dir'] == 'down':
                depth += instruction['amount']
            if instruction['dir'] == 'up':
                depth -= instruction['amount']

        print(depth*pos)


if __name__ == "__main__":
    main()

