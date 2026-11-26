def display_option():
    Conv_greeting = """   
            *** Welcome to the Weight Converter App ***
                Conversion Options
                (1) Pounds to Kilograms
                (2) Kilograms to Pounds
            *************************************************
            """
    print(Conv_greeting)

def lb_kg():
    return weight/2.2

def kg_lb():
    return weight*2.2

display_option()

while(True):
    while(True):
        option = int(input("Choose your conversion: "))
        if option not in [1, 2]:
            print("Invalid. Try again.")
        if option in [1, 2]:
            break
    weight = int(input("Weight: "))
    if option == 1:
        converted_temp_kg = round(float(lb_kg()), 2)
        print(f"{weight}lbs is {converted_temp_kg}kg.")
        redo = input("Would you like to calculate more?\nY/N -> ")
        if redo in ["Yes", "y", "Y", "yes"]:
            None
        elif redo in ["No", "n", "N", "no"]:
            break
    elif option == 2:
        converted_temp_lb = round(float(kg_lb()), 2)
        print(f"{weight}kg is {converted_temp_lb}lbs.")
        redo = input("Would you like to calculate more?\nY/N -> ")
        if redo in ["Yes", "y", "Y", "yes"]:
            None
        elif redo in ["No", "n", "N", "no"]:
            break
                    
print("Thank you for using the Weight Converter App.")
    

