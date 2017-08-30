"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    state_upper = state.upper()
    if state_upper in STATE_NAMES:
        print(state_upper, "is", STATE_NAMES[state_upper])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

