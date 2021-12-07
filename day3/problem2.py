def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        binary_arr = [line.strip('\n') for line in content]

        oxygen_rating = binary_arr
        scrubber_rating = binary_arr

        # Get oxygen rating
        for i in range(binary_arr[0].__len__()):
            bit = get_common_oxy_bit(i, oxygen_rating)
            oxygen_rating = get_rating_arrays(i, bit, oxygen_rating)
            if oxygen_rating.__len__() == 1:
                break

        # Get scrubber rating
        for i in range(binary_arr[0].__len__()):
            bit = get_common_scrub_bit(i, scrubber_rating)
            scrubber_rating = get_rating_arrays(i, bit, scrubber_rating)
            if scrubber_rating.__len__() == 1:
                break

        print(int(oxygen_rating[0], 2) * int(scrubber_rating[0], 2))


def get_common_oxy_bit(index, binary_arr):
    bit_sum = 0

    for binary_num in binary_arr:
        bit_sum += int(binary_num[index])

    if bit_sum >= binary_arr.__len__()/2:
        return '1'
    else:
        return '0'


def get_common_scrub_bit(index, binary_arr):

    bit_sum = sum([int(x[index]) for x in binary_arr])

    if bit_sum >= binary_arr.__len__()/2:
        return '0'
    else:
        return '1'


def get_rating_arrays(index, common_bit, binary_arr):
    rating_arr = []

    for binary_num in binary_arr:
        if binary_num[index] == common_bit:
            rating_arr.append(binary_num)

    return rating_arr


if __name__ == "__main__":
    main()

