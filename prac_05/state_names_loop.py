STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Nothern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    for state_short, state_long in STATE_NAMES.items():
        print(" {:4} is {}".format(state_short, state_long))


main()
