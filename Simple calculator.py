# This is a calculator that displays error messages when the user does not type in the desired inputs.

mode = input("Type 'import' to read calculations from a .txt file, or type 'here' to input numbers directly into the program.")
file = None

# The numbers are stored as floats because when one is divided by another, the result may not be a whole number.

# The following block of code is for when the user types numbers directly into the program.
while mode.lower() == "here":
    try:
        number_first = float(input("First, type a number."))
        number_second = float(input("Now, type another number."))
    except ValueError:
        print("Error: You did not input digits. Please try again.")
        continue

    operator = input("Now, type + to add these numbers, - to subtract them, x to multiply them, or / to divide them.")

    if operator == "+":
        addition = number_first + number_second
        print("The sum of those two numbers is " + str(addition))
        with open("calculator_results.txt", "w") as c:
            c.write(str(number_first) + " + " + str(number_second) + " = " + str(addition))
        break

    elif operator == "-":
        subtraction = number_first - number_second
        print(str(number_first) + " minus " + str(number_second) + " equals " + str(subtraction) + ".")
        with open("calculator_results.txt", "w") as c:
            c.write(str(number_first) + " - " + str(number_second) + " = " + str(subtraction))
        break
 
    elif operator.lower() == "x":
        product = number_first * number_second
        print("The product of those two numbers is " + str(product) + ".")
        with open("calculator_results.txt", "w") as c:
            c.write(str(number_first) + " * " + str(number_second) + " = " + str(product))
        break

    elif operator == "/":
        try:
            division = number_first / number_second
            print(str(number_first) + " divided by " + str(number_second) + " equals " + str(division) + ".")
            with open("calculator_results.txt", "w") as c:
                c.write(str(number_first) + " / " + str(number_second) + " = " + str(division))
            break
        except ZeroDivisionError:
            print("You cannot divide by 0.")

    else:
        print("Invalid input. Please try again.")
        break
    
# The following block of code is for when the user imports a file.
while mode.lower() == "import":
    try:
        file = open(input("Type the full path of the .txt file you want to open."), "r")
        print(file.readlines())
        break
    except FileNotFoundError:
        print("The file you are trying to open does not exist. Please restart the program.")

else:
    print("Invalid selection. Please restart the program.")