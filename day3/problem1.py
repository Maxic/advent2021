def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        binary_nums = [line.strip('\n') for line in content]

        sums = [0] * binary_nums[0].__len__()
        input_length = binary_nums.__len__()

        for binary_num in binary_nums:
            for i in range(binary_num.__len__()):
                sums[i] += int(binary_num[i])

        gamma_rate = [0] * binary_nums[0].__len__()
        epsilon_rate = [0] * binary_nums[0].__len__()

        for i in range(sums.__len__()):
            if sums[i] > input_length/2:
                gamma_rate[i] = 1
                epsilon_rate[i] = 0
            else:
                gamma_rate[i] = 0
                epsilon_rate[i] = 1

        gamma_rate = ''.join(str(x) for x in gamma_rate)
        epsilon_rate = ''.join(str(x) for x in epsilon_rate)

        result = int(gamma_rate, 2) * int(epsilon_rate, 2)

        print(result)


if __name__ == "__main__":
    main()

