
import math

menu = """(1) Show all even numbers
(2) Show all odd numbers
(3) Show all squared numbers
(4) Exit Program"""

print(menu)
choice = input('>>> ')
while choice != '4':
    if choice == '1':
        sequence_start_number = int(input("What number do you want the sequence to start at? "))
        sequence_end_number = int(input("What number do you want the sequence to end at? "))
        for i in range(sequence_start_number, sequence_end_number + 1):
            if i%2 == 0:
                print(i, end=' ')
                print() #Prints blank line for formatting
    elif choice == '2':
        sequence_start_number = int(input("What number do you want the sequence to start at? "))
        sequence_end_number = int(input("What number do you want the sequence to end at? "))
        for i in range(sequence_start_number, sequence_end_number + 1):
            if i%2 == 1:
                print(1, end=' ')
                print() #Prints blank line for formatting
    elif choice == '3':
        sequence_start_number = int(input("What number do you want the sequence to start at? "))
        sequence_end_number = int(input("What number do you want the sequence to end at? "))
        for i in range(sequence_start_number, sequence_end_number + 1):
            if math.sqrt(i).is_integer():
                print(i, end=' ')
                print() #Prints blank line for formatting
    else:
        print('Invalid Input')
    print(menu)
    choice = input('>>> ')
