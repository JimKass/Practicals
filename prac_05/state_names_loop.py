STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Nothern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


def main():
    for state_name in STATE_NAMES.items():
        print(" {:4} is {}".format(state_name[0], state_name[1]))


main()
