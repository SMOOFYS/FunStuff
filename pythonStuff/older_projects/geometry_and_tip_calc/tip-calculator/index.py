greeting = "Welcome to the Tip Machine!"
print(greeting)

total = float(input("What is the total amount of your order?\n-> "))
tip_percent = float(input("How much do you want to tip? (0.15 means 15%)\n-> "))

tip_amount = tip_percent*total
Overall_cost = tip_amount+total


print("Your total is: $"+round(Overall_cost, 2)+".")