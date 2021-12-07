def main():

    with open("input.txt", "r+") as file:
        content = file.readline()

        positions = [int(x) for x in content.split(',')]

        answer = {'pos': 0, 'dist': 10000000000}
        for i in range(min(positions), max(positions)+1):
            distance = calculate_total_movement(i, positions)
            if answer['dist'] > distance:
                answer['pos'] = i
                answer['dist'] = distance

        print(answer['dist'])


def calculate_total_movement(target_pos, positions):
    total_distance = 0

    for position in positions:
        total_distance += abs(target_pos-position)
    return total_distance


if __name__ == "__main__":
    main()

