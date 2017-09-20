"""
Let's you collect all of the guitars in the WWWOOORRRLLLDDD!!!
"""


from prac_07.guitar import Guitar


MY_GUITAR = ["Peavey AT-200", 2014, 600]
DADS_GUITAR = ["Tanglewood", 1982, 800]


def main():
    print("My guitars!")
    guitars = []
    guitars = add_guitar(guitars)


def add_guitar(guitars):
    name = get_valid_string("Name: ")
    year = get_valid_integer("Year: ")
    cost = get_valid_integer("Cost: $")
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print("{} ({}) : ${} added".format(guitar.name, guitar.year, guitar.cost))
    return guitars

    # print("Guitar {}: {:>20} ({}), worth ${:10.2f}".format(guitar.name, guitar.year, guitar.cost))

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
