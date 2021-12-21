from collections import Counter

def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        line_arr = [line.strip() for line in content]
        polymer_template = line_arr.pop(0)
        line_arr.pop(0)

        insertion_rules = {}
        for line in line_arr:
            pair, element = line.split(' -> ')
            insertion_rules[pair] = element

        for _ in range(10):
            polymer_template = do_pair_insertion(polymer_template, insertion_rules)

        bincount = Counter(polymer_template)
        print(max(bincount.values()) - min(bincount.values()))


def do_pair_insertion(polymer_template, insertion_rules):
    new_polymer_template = []
    for i, char in enumerate(polymer_template):
        if i == len(polymer_template)-1:
            new_polymer_template.append(char)
        else:
            new_polymer_template.append(char)
            new_polymer_template.append('.')

    for i in range(2, len(polymer_template) + 1):
        pair = polymer_template[i - 2:i]

        if pair in insertion_rules:
            element = insertion_rules[pair]
            new_polymer_template.insert(new_polymer_template.index('.'), element)
            new_polymer_template.remove('.')

    return "".join(new_polymer_template)


if __name__ == "__main__":
    main()

