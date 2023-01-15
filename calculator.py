# =======================================Optional Bonus Task 2 =====================================
'''This block code is calculator. this provide two choice
1. user manually enters number and operation to be performed
2. user input a file name which has set of equation that need to be evaluated
3. stop the program
All the inputed equation is printed in equation_history.txt file'''
# I have place user_input_file.txt sample file used as user input for option 2
# I have alos place equation history.txt file where all the history of the calculator is stored
from asyncio.windows_events import NULL

def add_num(num1, num2):
    '''code to add two numbers'''
    add_output = float(num1) + float(num2)
    print(f"{num1} + {num2} = {add_output}")

def subtract_num(num1, num2):
    '''code to subtract two numbers'''
    sub_output = float(num1) - float(num2)
    print(f"{num1} - {num2} = {sub_output}")

def multiply_num(num1, num2):
    '''code to multiply two numbers'''
    multiply_output = float(num1) * float(num2)
    print(f"{num1} * {num2} = {multiply_output}")

def divide_num(num1, num2):
    '''code to divide two numbers'''
    divide_output = float(num1) / float(num2)
    print(f"{num1} / {num2} = {divide_output}")

def readfromfile(filename):
    '''read from file and print the output'''
    try:
        with open(filename, "r", encoding="utf-8") as user_input_file:
            userequations_list = user_input_file.read().splitlines()
            print("Output")
            for eachequation in userequations_list:
                #eval used as literal_eval method cannot be used with arthimethic operator
                equation_result = eval(eachequation)
                print(f"{eachequation} = {equation_result}")
                writetoequationhistory(eachequation)
    except FileNotFoundError:
        print(f"file {filename} does not exist")
    return True


def writetoequationhistory(equation_string):
    '''write to equation history file'''
    try:
        with open("equation_history.txt", "a", encoding="utf-8") as equation_history_file:
            equation_history_file.write(f"{equation_string}\n")
    except FileNotFoundError:
        print("file equation_history.txt does not exist")


number_1 = NULL
number_2 = NULL
option_selected = NULL

while True:
    try:
        print("\nSelect 1 to enter the equation\n" \
            "Select 2 to read the equation from file\n" \
            "Select 3 to exit\n")
        user_choice = int(input("Enter your choice:\t"))
        if user_choice in [1, 2, 3]:
            if user_choice == 1:
                # Take input from the user
                number_1 = input("Enter first number:\t")
                number_2 = input("Enter second number:\t")
                option_selected = input("Please select operation +, -, *, / :\t")
                if option_selected not in ["+", "-", "*", "/"]:
                    print("No such option available in this calculator:")
                    break

                writetoequationhistory(f"{number_1} {option_selected} {number_2}")

                print("Output")
                if option_selected == "+":
                    add_num(number_1, number_2)
                elif option_selected == "-":
                    subtract_num(number_1, number_2)
                elif option_selected == "*":
                    multiply_num(number_1, number_2)
                elif option_selected == "/":
                    divide_num(number_1, number_2)

            if user_choice == 2:
                # read from the file
                readfromfile(input("Enter the file where equation is stored with extensions:\t"))

            if user_choice == 3:
                # exit the program
                raise SystemExit()
        else:
            print("Invalid choice entered please retry:")

    except ValueError as error:
        print("That was not a valid number, try again...")
        print(error)
