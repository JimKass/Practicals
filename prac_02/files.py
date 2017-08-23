NAME_FILE = "name"
NUMBER_FILE = "numbers"

def add_a_name():
    file_out = open(NAME_FILE, "w")
    name = input("What is your name? ")
    print(name, file=file_out)
    file_out.close()

def find_a_name():
    file_in = open(NAME_FILE, "r")
    name = file_in.readline()
    print("Your name is {}".format(name))
    file_in.close()

def add_numbers():
    file_in = open(NUMBER_FILE, "r")
    total_number = 0
    number_list = ""

    for line in file_in:
        total_number += int(line)
        number_list += "{} ".format(line.strip())
    print("{} ({})".format(total_number, number_list))

add_numbers()
