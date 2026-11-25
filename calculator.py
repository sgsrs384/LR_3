# Project 1 - Simple calculator 
# 7/18/2026 

# Version 2
# 9/3/2026

import math

# Get a valid number from user

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")



# Perform basic calculation

def calculate():
    operator = input("Enter operator (+, -, *, /, %): ")

    if operator not in ("+", "-", "*", "/", "%"):
        print(f"{operator} is not a valid operator.")
        return None

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    try:
        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2

        elif operator == "%":
            result = num1 % num2

        result = round(result, 2)

        calculation = f"{num1} {operator} {num2} = {result}"

        print(f"\nThe answer is: {result}")

        return calculation

    except ZeroDivisionError:
        print("Can't divide by zero.")
        return None



# Show calculation history


def show_history(history):

    if not history:
        print("\nNo calculations yet.")
        return

    print("\n========== HISTORY ==========")

    for number, calculation in enumerate(history, start=1):
        print(f"{number}. {calculation}")



# Save history to file


def save_history(history):

    if not history:
        print("\nThere is no history to save.")
        return

    with open("calculation_history.txt", "a") as file:

        for calculation in history:
            file.write(calculation + "\n")

    print("\nHistory saved successfully!")



# Scientific calculator


def scientific_calculator():

    print("\n========== SCIENTIFIC CALCULATOR ==========")

    print("1. Square root")
    print("2. Power")
    print("3. Factorial")
    print("4. Sine")
    print("5. Cosine")
    print("6. Tangent")
    print("7. Logarithm")
    print("8. Back to main menu")

    choice = input("\nChoose an option: ")

    try:

        if choice == "1":

            number = get_number("Enter number: ")

            if number < 0:
                print("Cannot calculate square root of a negative number.")
                return

            result = math.sqrt(number)

            print(f"√{number} = {round(result, 2)}")


        elif choice == "2":

            num1 = get_number("Enter base: ")
            num2 = get_number("Enter exponent: ")

            result = math.pow(num1, num2)

            print(f"{num1}^{num2} = {round(result, 2)}")


        elif choice == "3":

            number = get_number("Enter a whole number: ")

            if number < 0 or number != int(number):
                print("Factorial requires a non-negative whole number.")
                return

            result = math.factorial(int(number))

            print(f"{int(number)}! = {result}")


        elif choice == "4":

            number = get_number("Enter angle in degrees: ")

            result = math.sin(math.radians(number))

            print(f"sin({number}°) = {round(result, 4)}")


        elif choice == "5":

            number = get_number("Enter angle in degrees: ")

            result = math.cos(math.radians(number))

            print(f"cos({number}°) = {round(result, 4)}")


        elif choice == "6":

            number = get_number("Enter angle in degrees: ")

            result = math.tan(math.radians(number))

            print(f"tan({number}°) = {round(result, 4)}")


        elif choice == "7":

            number = get_number("Enter number: ")

            if number <= 0:
                print("Logarithm requires a number greater than zero.")
                return

            result = math.log(number)

            print(f"ln({number}) = {round(result, 4)}")


        elif choice == "8":
            return

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input.")



# Main program


def main():

    history = []

    while True:

        print("\n")
        print("========== SIMPLE CALCULATOR ==========")
        print("1. Calculate")
        print("2. View history")
        print("3. Save history")
        print("4. Scientific calculator")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            calculation = calculate()

            if calculation:
                history.append(calculation)


        elif choice == "2":

            show_history(history)


        elif choice == "3":

            save_history(history)


        elif choice == "4":

            scientific_calculator()


        elif choice == "5":

            print("\nThanks for using the calculator! 👋")
            break


        else:

            print("\nInvalid choice. Please choose 1-5.")


# Start the program

if __name__ == "__main__":
    main()