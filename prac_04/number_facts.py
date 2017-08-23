
def main():
    numbers = [int(input("Number: ")) for i in range(5)]
    print("The first numbe is " + str(numbers[0]))
    print("The last number is " + str(numbers[-1]))
    print("The smallest number is " + str(min(numbers)))
    print("The largest number is " + str(max(numbers)))
    print("The average of the numbers is " + str(sum(numbers) / len(numbers)))

main()
