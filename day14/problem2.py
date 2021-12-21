from collections import defaultdict

def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip() for line in content]
        polymer_template = line_arr.pop(0)
        line_arr.pop(0)

        # initialize and add to insertion rules
        insertion_rules = {}
        for line in line_arr:
            pair, element = line.split(' -> ')
            insertion_rules[pair] = (pair[0]+element, element+pair[1])

        # prefill pair count with initial count of polymer template
        pair_count = defaultdict(lambda: 0)
        for i in range(len(polymer_template)-1):
            pair = polymer_template[i:i+2]
            pair_count[pair] += 1

        for _ in range(40):
            for pair, count in list(pair_count.items()):
                n_p1, n_p2 = insertion_rules[pair]
                pair_count[pair] -= count
                pair_count[n_p1] += count
                pair_count[n_p2] += count

        # Count all elements from the pairs
        element_count = defaultdict(lambda: 0)
        for pair, count in pair_count.items():
            element_count[pair[0]] += count

        # Make sure we also get the last element
        element_count[polymer_template[-1]] += 1

        print(max(element_count.values()) - min(element_count.values()))


if __name__ == "__main__":
    main()

