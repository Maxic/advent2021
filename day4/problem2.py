import numpy as np


def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()

        bingo_numbers = content.pop(0).strip('\n').split(',')
        bingo_cards = []
        current_number = None
        content.pop(0)

        # create bingo cards
        for i in range(0, content.__len__(), 6):
            line1 = content[i].strip('\n').split()
            line2 = content[i+1].strip('\n').split()
            line3 = content[i+2].strip('\n').split()
            line4 = content[i+3].strip('\n').split()
            line5 = content[i+4].strip('\n').split()

            card = np.array(line1 + line2 + line3 + line4 + line5)

            card = np.reshape(card, (5, 5))
            bingo_cards.append(card)

        class Found(Exception):
            pass

        solved_cards = set()
        final_card = None

        try:
            for number in bingo_numbers:
                current_number = int(number)
                bingo_cards = mark_number(number, bingo_cards)
                for i, card in enumerate(bingo_cards):
                    if bingo(card):
                        solved_cards.add(i)
                    if solved_cards.__len__() == bingo_cards.__len__():
                        final_card = card
                        raise Found
        except Found:
            card = final_card.flatten()
            clean_int_arr = [int(x) for x in np.delete(card, np.where(card == 'X'), axis=0)]

            print(current_number)
            print(sum(clean_int_arr) * current_number)


def mark_number(number, bingo_cards):
    marked_cards = []

    for bingo_card in bingo_cards:
        marked_cards.append(np.where(bingo_card == number, 'X', bingo_card))

    return marked_cards


def bingo(card):
    for i in range(5):
        mark_count_col = sum(np.char.count(card[:, i], 'X'))
        mark_count_row = sum(np.char.count(card[i], 'X'))
        if mark_count_row == 5 or mark_count_col == 5:
            return True
    # mark_count_diag = sum(np.char.count(np.diag(card), 'X'))
    # mark_count_diag1 = sum(np.char.count(np.diag(np.fliplr(card)), 'X'))
    # if mark_count_diag == 5 or mark_count_diag1 == 5:
    #     return True
    return False


if __name__ == "__main__":
    main()
