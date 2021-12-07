lanternfish_spawn = []


class Lanternfish():
    def __init__(self, age):
        self.age_in_days = age

    def age(self):
        self.age_in_days -= 1
        if self.age_in_days < 0:
            self.age_in_days = 6
            lanternfish_spawn.append(Lanternfish(8))


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()[0].strip('\n')

        lanternfishes = list(map(lambda x: Lanternfish(int(x)), content.split(',')))

        for i in range(80):
            for lanternfish in lanternfishes:
                lanternfish.age()

            lanternfishes = lanternfishes + lanternfish_spawn
            lanternfish_spawn.clear()

        print(lanternfishes.__len__())


if __name__ == "__main__":
    main()

