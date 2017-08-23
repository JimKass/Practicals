def main():
    name = get_name()
    print_name(name)


def print_name(name):
    for i, letter in enumerate(name):
        if i % 2 == 1:
            print(letter, end=" ")


def get_name():
    name = input('Enter your name: ')
    while name == "":
        print("Invalid name")
        name = input('Enter your name: ')
    return name


main()
