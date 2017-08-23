def main():
    total_income = 0
    number_of_months = int(input("How many months? "))
    incomes = [float(input("Enter income for month {}: ".format(month))) for month in range(1, number_of_months + 1)]
    print("Income Report")
    print("--------------")
    for month, income in enumerate(incomes):
        month += 1
        total_income += income
        print("Month {} - Income: $ {:10.2f} Total: $ {:10.2f}".format(month, income, total_income))

main()
