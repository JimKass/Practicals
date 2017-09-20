"""
Test Guitar class
"""

from prac_07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 900)
    print("{}'s age is {}. Excepted 95".format(gibson.name, gibson.get_age()))
    print("{}'s age is {}. Expected 5".format(another_guitar.name, another_guitar.get_age()))
    print("{} is vintage: {}. Expected True".format(gibson.name, gibson.is_vintage()))
    print("{} is vintage: {}. Expected False".format(another_guitar.name, another_guitar.is_vintage()))


main()