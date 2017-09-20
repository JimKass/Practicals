
"""
Test Guitar class
"""

from prac_07.guitar import Guitar

def main():
    peavy = Guitar("Peavy AT-200 Black", 2014, 600)
    another_guitar = Guitar("Another Guitar", 1945, 900)
    print("{}'s age is {}".format(peavy.name, peavy.get_age()))
    print("{}'s age is {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is vintage: {}".format(peavy.name, peavy.is_vintage()))
    print("{} is vintage: {}".format(another_guitar.name, another_guitar.is_vintage()))


main()