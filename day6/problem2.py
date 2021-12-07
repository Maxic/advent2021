def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()[0].strip('\n')

        lanternfish = list(map(lambda x: int(x), content.split(',')))

        day_128_data = {}

        # Calculate the data for 128 days of growth for a fish of all possible ages (0,8)
        for age in range(9):
            fish_data = {}
            population, length = predict_fish([age], 128)
            fish_data['population'] = population
            fish_data['length'] = length
            day_128_data[age] = fish_data

        print(day_128_data[0]['length'])

        day_256_data = {}

        # Calculate the data for 256 days of growth for a fish of all possible ages (0,8)
        for age in range(9):
            population = day_128_data[age]['population']

            total_fish = 0
            for fish in population:
                total_fish += day_128_data[fish]['length']
            day_256_data[age] = total_fish

        # Calculate total number of fish for input
        total_fish = 0
        for fish in lanternfish:
            total_fish += day_256_data[fish]
        print(total_fish)


def predict_fish(current_pop, days):
    lanternfish = current_pop
    new_lanternfish = []

    for _ in range(days):
        for i, fish in enumerate(lanternfish):
            fish -= 1
            if fish < 0:
                fish = 6
                new_lanternfish.append(8)
            lanternfish[i] = fish
        lanternfish = lanternfish + new_lanternfish
        new_lanternfish.clear()

    return lanternfish, lanternfish.__len__()


if __name__ == "__main__":
    main()

