def display_options():   
    options = """
        *** Welcome to the Temperature Converter App ***
            Conversion Options
            (1) Fahrenheit to Celsius
            (2) Celsius to Fahrenheit
        *************************************************
    """
    print(options)

def F_C(temperature):
    return (temperature - 32) * 5/9

def C_F(temperature):
    return (temperature*9/5) + 32
    
    
display_options()

while(True):
    while(True):
        option = int(input("Select conversion option: ")) 
        if option in [1, 2]:
            break
        else:
            print("That is not an option. Please try again")
    temp = int(input("Temperature: "))
    if option == 1:    
        converted_temp_F = round(F_C(temp), 2)
        print(f"{temp}F is {converted_temp_F}C.")
        redo = input("Would you like to calculate more?\nY/N -> ")
        if redo in ["Yes", "y", "Y", "yes"]:
            None
        elif redo in ["No", "n", "N", "no"]:
            break
    elif option == 2:    
        converted_temp_C = round(C_F(temp))
        print(f"{temp}C is {converted_temp_C}F.")
        redo = input("Would you like to calculate more?\nY/N -> ")
        if redo in ["Yes", "y", "Y", "yes"]:
            None
        elif redo in ["No", "n", "N", "no"]:
            break
    
    