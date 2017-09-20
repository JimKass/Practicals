"""
Let's you collect all of the guitars in the WWWOOORRRLLLDDD!!!
"""


from prac_07.guitar import Guitar


MENU = """A - Add a guitar
D - Display a guitar"""


def main():
    print("My guitars!")
    guitars = []
    print(MENU)
    action = get_valid_string(">>> ").lower()
    while action != "q":
        if action == "a":
            guitars = add_guitar(guitars)
        elif action == "d":
            display_guitars(guitars)
        else:
            print("Invalid Input")
        print(MENU)
        action = get_valid_string(">>> ").lower()
    print("Good-bye.")


def display_guitars(guitars):
    for i, guitar in enumerate(guitars):
        vintage_string = ["{vintage)" if guitar.is_vintage() else ""]
        print("Guitar {}: {} ({}), worth ${} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))


def add_guitar(guitars):
    name = get_valid_string("Name: ")
    year = get_valid_integer("Year: ")
    cost = get_valid_integer("Cost: $")
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print("{} ({}) : ${} added".format(guitar.name, guitar.year, guitar.cost))
    return guitars


def get_valid_string(prompt):
        user_input = input(prompt)
        while user_input == "":
            print("Input cannot be blank")
            user_input = input(prompt)
        return user_input


def get_valid_integer(prompt):
    is_valid = False
    while not is_valid:
        try:
            user_input = int(input(prompt))
            is_valid = True
        except ValueError:
            print("Invalid number")
    return user_input


main()
