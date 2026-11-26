def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def welcome_message():
    greeting = """
    Welcome to the Calculator App! 
    In this app, you can add, subtract, multiply, and divide 2 numbers.
    """
    print(greeting)
redo = False
welcome_message()
    
while(True):
    if redo in ["No", "no", "n", "N"]:
        break
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    while(True):
        if redo in ["No", "no", "n", "N"]:
            break
        operation = """
        Choose Operation:
        (1) Addition
        (2) Subtraction
        (3) Multiplication
        (4) Division
        """
        operation_choice = input(operation + "-> ")
        if operation_choice == 1:
            total_sum = add(num_1, num_2)
            print(f"The sum of {num_1} and {num_2} is {total_sum}.")
            while(True):
                redo = input("Would you like to calculate more?\nY/N\n-> ")
                if redo in ["Yes", "yes", "y", "Y"]:
                    break
                elif redo in ["No", "no", "n", "N"]:
                    break
                else:
                    print("Your response was invalid. Please try again.")
            if redo in ["No", "no", "n", "N"]:
                break
        elif operation_choice == 2:
            total_difference = sub(num_1, num_2)
            print(f"The difference of {num_1} and {num_2} is {total_difference}.")
            while(True):
                redo = input("Would you like to calculate more?\nY/N\n-> ")
                if redo in ["Yes", "yes", "y", "Y"]:
                    break
                elif redo in ["No", "no", "n", "N"]:
                    break
                else:
                    print("Your response was invalid. Please try again.")
            if redo in ["No", "no", "n", "N"]:
                break
        elif operation_choice == 3:
            total_product = multi(num_1, num_2)
            print(f"The product of {num_1} and {num_2} is {total_product}.")
            while(True):
                redo = input("Would you like to calculate more?\nY/N\n-> ")
                if redo in ["Yes", "yes", "y", "Y"]:
                    break
                elif redo in ["No", "no", "n", "N"]:
                    break
                else:
                    print("Your response was invalid. Please try again.")
            if redo in ["No", "no", "n", "N"]:
                break
        elif operation_choice == 4:
            total_quotient = int(div(num_1, num_2))
            print(f"The quotient of {num_1} and {num_2} is {total_quotient}.")
            redo = input("Would you like to calculate more?\nY/N\n-> ")
            while(True):
                redo = input("Would you like to calculate more?\nY/N\n-> ")
                if redo in ["Yes", "yes", "y", "Y"]:
                    break
                elif redo in ["No", "no", "n", "N"]:
                    break
                else:
                    print("Your response was invalid. Please try again.")
            if redo in ["No", "no", "n", "N"]:
                break
        elif operation_choice is not [1, 2, 3, 4]:
            print("That choice is invalid, please try again.")
            
print("Thank you for using the Calculator App.")