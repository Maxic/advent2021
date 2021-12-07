def main():

    with open("input.txt", "r+") as file:
        content = file.readline()

        positions = [int(x) for x in content.split(',')]

        fuel_per_dist = calc_fuel_arr(max(positions)+1)

        answer = {'pos': 0, 'dist': 10000000000}
        for i in range(min(positions), max(positions)+1):
            distance = calculate_total_movement(i, positions, fuel_per_dist)
            if answer['dist'] > distance:
                answer['pos'] = i
                answer['dist'] = distance

        print(answer['dist'])


def calc_fuel_arr(length):
    fuel_arr = [0]
    for i in range(1, length):
        fuel_arr.append(i+fuel_arr[i-1])
    return fuel_arr


def calculate_total_movement(target_pos, positions, fuel_arr):
    total_distance = 0

    for position in positions:
        total_distance += fuel_arr[abs(target_pos-position)]
    return total_distance


if __name__ == "__main__":
    main()
