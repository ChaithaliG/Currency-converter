# Coversion from US Dollars to Indian rupees.
def main():
    print("This program converts US dollars to Indian Rupees")
    print()

    dollars = eval(input("Enter the amount in dollars: "))

    INR = convert_to_indian_rupees(dollars)

    print("That is" ,INR, "Indian rupees. ")

convert_to_indian_rupees = lambda dollars: dollars * 82.92

main()