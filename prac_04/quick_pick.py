import random

def main():
    quick_picks = []
    number_of_quick_picks = int(input("How many QuickPicks? "))
    for i in range(1, number_of_quick_picks + 1):
        quick_pick = []
        while len(quick_pick) < 6:
            number = random.randint(1, 46)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_picks.append(quick_pick)
    for line in quick_picks:
        for number in sorted(line):
            print('{:^4d}'.format(number), end="")
        print()

main()
