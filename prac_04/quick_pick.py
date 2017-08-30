import random


def main():
    quick_picks = []
    number_of_quick_picks = int(input("How many QuickPicks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < 6:
            number = random.randint(1, 45)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_picks.append(quick_pick)
    for quick_pick in quick_picks:
        for number in sorted(quick_pick):
            print(' {:2d} '.format(number), end="")
        print()


main()
