
UPPER_BOUND = 127
LOWER_BOUND = 33

char = input("Enter a character: ")
print("{}".format(ord(char)))
number = int(input("Enter a number between 33 and 127: "))
while number < LOWER_BOUND and number > UPPER_BOUND:
    print("Invalid Input")
    number = int(input("Enter a number between {} and {}: ".format(UPPER_BOUND, LOWER_BOUND)))
print("{}".format(chr(number)))

for letter in range(LOWER_BOUND, UPPER_BOUND):
    print("{:3d}    {}".format(letter, chr(letter)))
