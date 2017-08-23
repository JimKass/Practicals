NUMBERS = [3, 1, 4, 1, 5, 9, 2]

def change_to_ten():
    NUMBERS[0] = "ten"
    print(NUMBERS)

def change_to_1():
    NUMBERS[-1] = 1
    print(NUMBERS)

def get_all_elements_except_two():
    print(NUMBERS[2:])

def check_for_9():
    print(9 in NUMBERS)

get_all_elements_except_two()